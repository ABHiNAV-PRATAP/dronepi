import RPi.GPIO as GPIO
import time

#set pins
frontRight = 40 
backRight = 38
frontLeft = 36
backLeft = 3

aux = 13

min_throttle = 5
max_throttle = 9

percent = 0

GPIO.cleanup()

GPIO.setmode(GPIO.BOARD)

GPIO.setup(frontRight,GPIO.OUT)
GPIO.setup(backRight,GPIO.OUT)
GPIO.setup(frontLeft,GPIO.OUT)
GPIO.setup(backLeft,GPIO.OUT)
GPIO.setup(aux,GPIO.OUT)

m1 = GPIO.PWM(frontRight, 50)
m2 = GPIO.PWM(backRight, 50)
m3 = GPIO.PWM(frontLeft, 50)
m4 = GPIO.PWM(backLeft, 50)
aux1 = GPIO.PWM(aux, 50)

m1.start(0)
m2.start(0)
m3.start(0)
m4.start(0)
aux1.start(7)

def translate(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)

def arm(p):
	dutyCycle = translate(p, 0, 100, min_throttle, max_throttle)
	print("Arm sequence.......")
	print("frontRight")
	m1.ChangeDutyCycle(dutyCycle)
	time.sleep(1)
	print("backRight")
	m2.ChangeDutyCycle(dutyCycle)
	time.sleep(1)
	print("frontLeft")
	m3.ChangeDutyCycle(dutyCycle)
	time.sleep(1)
	print("backLeft")
	m4.ChangeDutyCycle(dutyCycle)
	time.sleep(1)

arm(5)

time.sleep(1)

def set(p):
	dutyCycle = translate(p, 0, 100, min_throttle, max_throttle)
	m1.ChangeDutyCycle(dutyCycle)
	m2.ChangeDutyCycle(dutyCycle)
	m3.ChangeDutyCycle(dutyCycle)
	m4.ChangeDutyCycle(dutyCycle)
	print("Speed: " + str(p) + "% / " + str(dutyCycle))
	return

while True:
	inp =  input()
	if inp == "i":
		percent += 10
	elif inp == "d":
		percent -= 10
	elif inp == "stop":
		percent = 0
		set(percent)
		break 
	set(percent)

GPIO.cleanup()
