import RPi.GPIO as GPIO
import time

#set pins
frontRightPin = 40 # 1
backRightPin = 38 # 2
frontLeftPin = 36 # 3
backLeftPin = 3 # 4

aux = 13

min_throttle = 5
max_throttle = 9

percent = 0

GPIO.cleanup()

GPIO.setmode(GPIO.BOARD)

GPIO.setup(frontRightPin,GPIO.OUT)
GPIO.setup(backRightPin,GPIO.OUT)
GPIO.setup(frontLeftPin,GPIO.OUT)
GPIO.setup(backLeftPin,GPIO.OUT)
GPIO.setup(aux,GPIO.OUT)

mFR = GPIO.PWM(frontRightPin, 50)
mBR = GPIO.PWM(backRightPin, 50)
mFL = GPIO.PWM(frontLeftPin, 50)
mBL = GPIO.PWM(backLeftPin, 50)
aux1 = GPIO.PWM(aux, 50)

mFR.start(0)
mBR.start(0)
mFL.start(0)
mBL.start(0)
aux1.start(7)

def translate(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)

    
def setMotor(p, motor):
    dutyCycle = translate(p, 0, 100, min_throttle, max_throttle)
    motor.ChangeDutyCycle(dutyCycle)
    return

def arm(p):
	print("Arm sequence.......")
	print("frontRight")
	setMotor(p, mFR)
	time.sleep(1)
	print("backRight")
	setMotor(p, mBR)
	time.sleep(1)
	print("frontLeft")
	setMotor(p, mFL)
	time.sleep(1)
	print("backLeft")
	setMotor(p, mBL)
	time.sleep(1)

def setAll(p):
	dutyCycle = translate(p, 0, 100, min_throttle, max_throttle)
	mFR.ChangeDutyCycle(dutyCycle)
	mBR.ChangeDutyCycle(dutyCycle)
	mFL.ChangeDutyCycle(dutyCycle)
	mBL.ChangeDutyCycle(dutyCycle)
	print("Speed: " + str(p) + "% / " + str(dutyCycle))
	return

arm(5)

time.sleep(1)

while True:
	inp =  input()
	if inp == "i":
		percent += 10
	elif inp == "d":
		percent -= 10
	elif inp == "stop":
		percent = 0
		setAll(percent)
		break 
	setAll(percent)

GPIO.cleanup()
