from threading import Thread
from time import sleep
import math

import utils.BerryIMU.berryIMU as IMU
from drone import Drone
from utils.client import Client
from utils.pid_controller import pid_controller as PID
import utils.BerryIMU.bmp280 as barometer

throttle = 0
MAX_THROTTLE = 10
MAX_MSPEED = 20

drone = Drone(40, 38, 36, 37, 31, MAX_THROTTLE)

t_pid = PID(0.1, 0.001, 0.1)
r_pid = PID(0.1, 0.001, 0.1)
p_pid = PID(0.1, 0.001, 0.1)
y_pid = PID(0.1, 0.001, 0.1)

IMU.initIMU()

def translate(value, leftMin, leftMax, rightMin, rightMax):
        # Figure out how 'wide' each range is
        leftSpan = leftMax - leftMin
        rightSpan = rightMax - rightMin

        # Convert the left range into a 0-1 range (float)
        valueScaled = float(value - leftMin) / float(leftSpan)

        # Convert the 0-1 range into a value in the right range.
        return rightMin + (valueScaled * rightSpan)

def getAltitude(bar):
        return (10**(math.log10(barometer.read().pressure/ 1013.25)/ 5.2558797) - 1)/ (-6.8755856 * 10**-6)

def get(x, y, t, yw):
        global throttle
        # global MAX_MSPEED

        yaw = y_pid.updateOutput(IMU.read().yaw, yw)
        pitch = p_pid.updateOutput(IMU.read().pitch, y)
        roll = r_pid.updateOutput(IMU.read().roll, x)
        throttle = t_pid.updateOutput(getAltitude, t)

        compute(yaw, pitch, roll, throttle)


def compute(yaw, pitch, roll, thrust):
        pFR = thrust + yaw + pitch + roll
        pFL = thrust - yaw + pitch - roll
        pBR = thrust - yaw - pitch + roll
        pBL = thrust + yaw - pitch - roll

        max_p = max([pFR, pFL, pBR, pBL])

        if max_p > 100:

              pFR = translate(pFR, .1, max_p, .1, 100)
              pFL = translate(pFL, .1, max_p, .1, 100)
              pBR = translate(pBR, .1, max_p, .1, 100)
              pBL = translate(pBL, .1, max_p, .1, 100)

        set(pFR, pFL, pBL, pBR)


def set(pFR, pFL, pBL, pBR):
        global drone

        drone.setAll(pFR, pFL, pBL, pBR)


def main():
        c = Client(5005, '192.168.2.15', get)
        while True:
                print('Connecting...')
                rc = c.client.connect()
                sleep(0.01)
                if rc:
                        isConnected = True
                        while isConnected:
                                sleep(0.001)
                else:
                        print("Client:-- Connection failed")
                        sleep(0.1)

main()
