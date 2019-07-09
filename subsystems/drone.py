import RPi.GPIO as GPIO
import time


class Drone:
    def __init__(self, frontRightPin, backRightPin, frontLeftPin, backLeftPin, auxPin, max_throttle):
        self.frontRightPin = frontRightPin
        self.backRightPin = backRightPin
        self.frontLeftPin = frontLeftPin
        self.backLeftPin = backLeftPin

        self.auxPin = auxPin

        self.min_throttle = 4
        self.max_throttle = max_throttle

        GPIO.cleanup()
        GPIO.setmode(GPIO.BOARD)

        GPIO.setup(self.frontRightPin, GPIO.OUT)
        GPIO.setup(self.backRightPin, GPIO.OUT)
        GPIO.setup(self.frontLeftPin, GPIO.OUT)
        GPIO.setup(self.backLeftPin, GPIO.OUT)
        GPIO.setup(self.auxPin, GPIO.OUT)

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

    def translate(self, value, leftMin, leftMax, rightMin, rightMax):
        # Figure out how 'wide' each range is
        leftSpan = leftMax - leftMin
        rightSpan = rightMax - rightMin

        # Convert the left range into a 0-1 range (float)
        valueScaled = float(value - leftMin) / float(leftSpan)

        # Convert the 0-1 range into a value in the right range.
        return rightMin + (valueScaled * rightSpan)

    def setMotor(self, p, motor):
        dutyCycle = self.translate(p, 0, 100, self.min_throttle, self.max_throttle)
        motor.ChangeDutyCycle(dutyCycle)
        return

    def arm(self, p):
            print("Arm sequence.......")
            self.setMotor(p, self.mFR)
            self.setMotor(p, self.mBR)
            self.setMotor(p, self.mFL)
            self.setMotor(p, self.mBL)
            time.sleep(1)

    def setAll(self, pFR, pFL, pBL, pBR):
            self.setMotor(pFR, self.mFR)
            self.setMotor(pFL, self.mFL)
            self.setMotor(pBL, self.mBL)
            self.setMotor(pBR, self.mBR)
