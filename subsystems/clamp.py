from adafruit_servokit import ServoKit

kit = None

def initClamp():
    global kit

    kit = ServoKit(channels=16)

    kit.servo[0].set_pulse_width_range(1000, 2000)
    kit.servo[1].set_pulse_width_range(1000, 2000)

    for i in range(0, 180):
        kit.servo[0].angle = i
        kit.servo[1].angle = i

def moveClamp(angle):
    kit.servo[0].angle = angle
    kit.servo[1].angle = angle

def clamp():
    moveClamp(15)

def release():
    moveClamp(0)

