from adafruit_servokit import ServoKit

kit = None

def initClamp():
    global kit

    kit = ServoKit(channels=16)

    kit.servo[0].set_pulse_width_range(400, 2400)
    kit.servo[1].set_pulse_width_range(400, 2400)

    kit.servo[0].angle = 180
    kit.servo[1].angle = 180

def moveClamp(angle):
    kit.servo[0].angle = angle
    kit.servo[1].angle = angle

def clamp():
    moveClamp(140)

def release():
    moveClamp(180)

