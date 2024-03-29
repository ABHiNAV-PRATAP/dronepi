import time

import utils.IMU as imu
from subsystems.drone import Drone
import subsystems.clamp as clamp
from utils.client import Client
from utils.pid_controller import pid_controller as PID
from constants import *

manual = True

drone = Drone(FR_PIN, BR_PIN, FL_PIN, BL_PIN)

t_pid = PID(THROTTLE_KP, THROTTLE_KD, THROTTLE_KDT)
r_pid = PID(ROLL_KP, ROLL_KD, ROLL_KDT)
p_pid = PID(PITCH_KP, PITCH_KD, PITCH_KDT)
y_pid = PID(YAW_KP, YAW_KD, YAW_KDT)

poll_interval = imu.getRate()
clamp.initClamp()

def translate(value, leftMin, leftMax, rightMin, rightMax):
        # Figure out how 'wide' each range is
        leftSpan = leftMax - leftMin
        rightSpan = rightMax - rightMin

        # Convert the left range into a 0-1 range (float)
        valueScaled = float(value - leftMin) / float(leftSpan)

        # Convert the 0-1 range into a value in the right range.
        return rightMin + (valueScaled * rightSpan)


def get(x, y, t, yw):
        x_scaled = translate(x, -1, 1, -20, 20)
        y_scaled = translate(y, -1, 1, -20, 20)
        yw_scaled = translate(yw, -1, 1, -180, 180)

        while True:
                rpy = imu.getRPY()

                if rpy == -1:
                        continue

                yaw = y_pid.updateOutput(rpy.yaw, yw_scaled)
                pitch = p_pid.updateOutput(rpy.pitch, y_scaled)
                roll = r_pid.updateOutput(rpy.roll, x_scaled)

                if manual:
                        compute(yaw, pitch, roll, t)
                else:
                        throttle = t_pid.updateOutput(imu.getAltitude(), t)
                        compute(yaw, pitch, roll, throttle)

                time.sleep(poll_interval * 1.0 / 1000.0)


def compute(yaw, pitch, roll, thrust):
        pFR = thrust + yaw + pitch + roll
        pFL = thrust - yaw + pitch - roll
        pBR = thrust - yaw - pitch + roll
        pBL = thrust + yaw - pitch - roll

        if DEBUG:
                print('pFR: %f, pFL: %f, pBR: %f, pBL: %f' % (pFR, pFL, pBR, pBL))

        set(pFR, pFL, pBL, pBR)


def set(pFR, pFL, pBL, pBR):
        global drone

        drone.setAll(pFR, pFL, pBL, pBR)


def initCamera():
        print('initializing camera')
        # TODO: initialize camera to return (x,y) position of target


def initManual():
        print('manual mode')
        c = Client(PORT, IP_ADDRESS, get)
        while True:
                print('Connecting to server...')
                rc = c.client.connect()
                time.sleep(0.01)
                if rc:
                        isConnected = True
                        while isConnected:
                                time.sleep(0.001)
                else:
                        print("Connection failed")
                        time.sleep(0.1)


def initAuto():
        print('autonomous mode')
        while True:
                print('')
                # TODO: start looping PID with given desired position from camera


if manual:
        initManual()
else:
        initAuto()
