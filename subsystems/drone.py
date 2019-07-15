from board import SCL, SDA
import busio

# Import the PCA9685 module.
from adafruit_pca9685 import PCA9685
import time

class Drone:


    def __init__(self, frontRightPin, backRightPin, frontLeftPin, backLeftPin):
        self.mFR = frontRightPin
        self.mBR = backRightPin
        self.mFL = frontLeftPin
        self.mBL = backLeftPin

        # Create the I2C bus interface.
        self.i2c_bus = busio.I2C(SCL, SDA)

        # Create a simple PCA9685 class instance.
        self.pca = PCA9685(self.i2c_bus)

        # Set the PWM frequency to 50hz.
        self.pca.frequency = 50

        # Set the PWM duty cycle for channel zero to 50%. duty_cycle is 16 bits to match other PWM objects
        # but the PCA9685 will only actually give 12 bits of resolution.
        self.pca.channels[self.mFR].duty_cycle = 0x0000
        self.pca.channels[self.mBR].duty_cycle = 0x0000
        self.pca.channels[self.mFL].duty_cycle = 0x0000
        self.pca.channels[self.mBL].duty_cycle = 0x0000

    def translate(self, value, leftMin, leftMax, rightMin, rightMax):
        # Figure out how 'wide' each range is
        leftSpan = leftMax - leftMin
        rightSpan = rightMax - rightMin

        # Convert the left range into a 0-1 range (float)
        valueScaled = float(value - leftMin) / float(leftSpan)

        # Convert the 0-1 range into a value in the right range.
        return rightMin + (valueScaled * rightSpan)

    def setMotor(self, p, motor):
        dutyCycle = self.translate(p, 0, 100, 0, 6553)
        hexValue = int(hex(dutyCycle), 16)
        self.pca.channels[motor].duty_cycle = hexValue
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
