from adafruit_servokit import ServoKit
# from constants import *

kit = None

def initClamp():
    global kit

    kit = ServoKit(channels=16)

    kit.servo[0].set_pulse_width_range(750, 2250)
    kit.servo[1].set_pulse_width_range(750, 2250)

    # kit.servo[0].angle = CLAMP_INIT
    # kit.servo[1].angle = CLAMP_INIT

def moveClamp(angle):
    kit.servo[0].angle = angle
    kit.servo[1].angle = angle

def clamp():
    moveClamp(15)

def release():
    moveClamp(0)

