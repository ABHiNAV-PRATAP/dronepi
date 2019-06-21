
from drone import Drone

pFR = 0
pFL = 0
pBR = 0
pBL = 0

yaw = 0
pitch = 0
roll = 0
thrust = 0

def setThrottle(t):
        thrust = t
        pFR, pFL, pBR, pBL = thrust, thrust, thrust, thrust

def setPitch(y):
        pitch = abs(y) * 100

        if y > 0: # forward
                pBL += pitch
                pBR += pitch
                pFL -= pitch
                pFR -= pitch
        elif y < 0: # backward
                pFR += pitch
                pFL += pitch
                pBR -= pitch
                pBL -= pitch

def setRoll(x):
        roll = abs(x) * 100
        
        if x > 0:
                pBR -= roll
                pFR -= roll
                pFL += roll
                pBL += roll
        elif x < 0:
                pBR += roll
                pFR += roll
                pBL -= roll
                pFL -= roll

def setYaw(x):
        yaw = abs(x) * 100
        
        if x > 0:
                pFR += yaw
                pBL += yaw
                pFL -= yaw
                pBR-= yaw
        elif x < 0:
                pFR -= yaw
                pBL -= yaw
                pFL += yaw
                pBR += yaw

def set(x, y, throttle, yaww):
        setThrottle(throttle)
        setYaw(yaww)
        setRoll(x)
        setPitch(y)
        Drone.setAll(pFR, pFL, pBL, pBR)

