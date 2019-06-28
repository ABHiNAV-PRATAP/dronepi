import RTIMU
import os
import sys
import math

class RPY():
    roll = 0
    pitch = 0
    yaw = 0

class RTIMU:
    def __init__(self, SETTINGS_FILE):
        print("Using settings file " + SETTINGS_FILE + ".ini")
        if not os.path.exists(SETTINGS_FILE + ".ini"):
            print("Settings file does not exist, will be created")

        s = RTIMU.Settings(SETTINGS_FILE)
        self.IMU = RTIMU.RTIMU(s)
        self.pressure = RTIMU.RTPressure(s)

        if (not IMU.IMUInit()):
            print("IMU Init Failed")
            sys.exit(1)
        else:
            print("IMU Init Succeeded");

        # set fusion parameters
        self.imu.setSlerpPower(0.02)
        self.imu.setGyroEnable(True)
        self.imu.setAccelEnable(True)
        self.imu.setCompassEnable(True)

        if not self.pressure.pressureInit():
            print("Pressure sensor init Failed")
            sys.exit(1)
        else:
            print("Pressure sensor init Succeeded")

        poll_interval = self.imu.IMUGetPollInterval()
        print("Recommended Poll Interval: %dmS\n" % poll_interval)

    def computeHeight(pressure):
        return 44330.8 * (1 - pow(pressure / 1013.25, 0.190263))

    def getRPY(self):
        if self.imu.IMURead():
            # x, y, z = imu.getFusionData()
            # print("%f %f %f" % (x,y,z))
            data = self.imu.getIMUData()
            fusionPose = data["fusionPose"]
            rpy = RPY()
            rpy.roll = math.degrees(fusionPose[0])
            rpy.pitch = math.degrees(fusionPose[1])
            rpy.yaw = math.degrees(fusionPose[2])

            return rpy

    def getAltitude(self):
        pressureValid, pressure, _, _ = self.pressure.pressureRead()
        if pressureValid
            return self.computeHeight(pressure)
        else:
            return -1

    def getRate(self):
        return self.imu.IMUGetPollInterval()
