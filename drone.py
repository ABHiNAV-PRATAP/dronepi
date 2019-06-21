import RPi.GPIO as GPIO
import time

class Drone:
    def __init__(self, frontRightPin, backRightPin, frontLeftPin, backLeftPin, auxPin, max_throttle):
        self.frontRightPin = frontRightPin
        self.backRightPin = backRightPin
        self.frontLeftPin = frontLeftPin
        self.backLeftPin = backLeftPin

        self.auxPin = auxPin

        self.min_throttle = 5
        self.max_throttle = max_throttle

        self.pFR = 0
        self.pBR = 0
        self.pFL = 0
        self.pBL = 0

        GPIO.cleanup()
        GPIO.setmode(GPIO.BOARD)

        GPIO.setup(self.frontRightPin,GPIO.OUT)
        GPIO.setup(self.backRightPin,GPIO.OUT)
        GPIO.setup(self.frontLeftPin,GPIO.OUT)
        GPIO.setup(self.backLeftPin,GPIO.OUT)
        GPIO.setup(self.aux,GPIO.OUT)

        self.mFR = GPIO.PWM(self.frontRightPin, 50)
        self.mBR = GPIO.PWM(self.backRightPin, 50)
        self.mFL = GPIO.PWM(self.frontLeftPin, 50)
        self.mBL = GPIO.PWM(self.backLeftPin, 50)
        self.aux = GPIO.PWM(self.auxPin, 50)

        self.mFR.start(0)
        self.mBR.start(0)
        self.mFL.start(0)
        self.mBL.start(0)
        self.aux.start(7)

    def translate(value, leftMin, leftMax, rightMin, rightMax):
        # Figure out how 'wide' each range is
        leftSpan = leftMax - leftMin
        rightSpan = rightMax - rightMin

        # Convert the left range into a 0-1 range (float)
        valueScaled = float(value - leftMin) / float(leftSpan)

        # Convert the 0-1 range into a value in the right range.
        return rightMin + (valueScaled * rightSpan)

        
    def setMotor(self, p, motor):
        dutyCycle = translate(p, 0, 100, self.min_throttle, self.max_throttle)
        motor.ChangeDutyCycle(dutyCycle)
        return

    def arm(self, p):
            print("Arm sequence.......")
            print("frontRight")
            self.setMotor(p, self.mFR)
            time.sleep(1)
            print("backRight")
            self.setMotor(p, self.mBR)
            time.sleep(1)
            print("frontLeft")
            self.setMotor(p, self.mFL)
            time.sleep(1)
            print("backLeft")
            self.setMotor(p, self.mBL)
            time.sleep(1)

    def setAll(self, pFR, pFL, pBL, pBR):
            dcFR = translate(pFR, 0, 100, self.min_throttle, self.max_throttle)
            dcFL = translate(pFL, 0, 100, self.min_throttle, self.max_throttle)
            dcBR = translate(pBR, 0, 100, self.min_throttle, self.max_throttle)
            dcBL = translate(pBL, 0, 100, self.min_throttle, self.max_throttle)
            self.mFR.ChangeDutyCycle(dcFR)
            self.mBR.ChangeDutyCycle(dcBR)
            self.mFL.ChangeDutyCycel(dcFL)
            self.mBL.ChangeDutyCycle(dcBL)

