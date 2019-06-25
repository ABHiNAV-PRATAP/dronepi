from drone import Drone
from utils.client import Client
from time import sleep

throttle = 0
MAX_THROTTLE = 10
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
        pFR = thrust + yaw + pitch + roll
        pFL = thrust - yaw + pitch - roll
        pBR = thrust - yaw - pitch + roll
        pBL = thrust + yaw - pitch - roll

        set(pFR, pFL, pBL, pBR)


def set(pFR, pFL, pBL, pBR):
        global drone

        drone.setAll(pFR, pFL, pBL, pBR)


def main():
        c = Client(5005, '192.168.115.103', get)
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
