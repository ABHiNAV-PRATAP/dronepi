from drone import Drone
from utils.client import Client
from time import *

throttle = 0
MAX_THROTTLE = 8
MAX_MSPEED = 20

drone = Drone(0, 0, 0, 0, 0, MAX_THROTTLE)


def get(x, y, t, yw):
        global throttle
        global MAX_MSPEED

        yaw = yw * MAX_MSPEED
        pitch = y * MAX_MSPEED
        roll = x * MAX_MSPEED
        if t is not None:
                throttle = t

        compute(yaw, pitch, roll, throttle)


def compute(yaw, pitch, roll, thrust):
        pFR = thrust - pitch - roll + yaw
        pFL = thrust - pitch + roll - yaw
        pBR = thrust + pitch - roll - yaw
        pBL = thrust + pitch + roll + yaw

        set(pFR, pFL, pBL, pBR)


def set(pFR, pFL, pBL, pBR):
        global drone

        drone.setAll(pFR, pFL, pBL, pBR)

def main():
        client = Client(5005, '192.168.115.103', get)
        while True:
                print('Connecting...')
                rc = client.client.connect()
                sleep(0.01)
                if rc:
                        isConnected = True
                        while isConnected:
                                sleep(0.001)
                else:
                        print("Client:-- Connection failed")
                        sleep(0.1)

main()
