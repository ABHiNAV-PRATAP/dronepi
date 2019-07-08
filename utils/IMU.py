import RTIMU
import os
import sys
import math


class RPY:
    roll = 0
    pitch = 0
    yaw = 0


class Quaternion:
    x = 0
    y = 0
    z = 0
    w = 0


imu = None
pressure = None

s = RTIMU.Settings('RTIMULib')
imu = RTIMU.RTIMU(s)
pressure = RTIMU.RTPressure(s)

if not imu.IMUInit():
    print("IMU Init Failed")
    sys.exit(1)
else:
    print("IMU Init Succeeded");

# set fusion parameters
imu.setSlerpPower(0.02)
imu.setGyroEnable(True)
imu.setAccelEnable(True)
imu.setCompassEnable(True)

if not pressure.pressureInit():
    print("Pressure sensor init Failed")
    sys.exit(1)
else:
    print("Pressure sensor init Succeeded")


def computeHeight(pressure):
    return 44330.8 * (1 - pow(pressure / 1013.25, 0.190263))


def getRPY():
    global imu

    if imu.IMURead():
        data = imu.getIMUData()
        fusionPose = data["fusionPose"]
        rpy = RPY()
        rpy.roll = math.degrees(fusionPose[0])
        rpy.pitch = math.degrees(fusionPose[1])
        rpy.yaw = math.degrees(fusionPose[2])

        return rpy

    else:
        print('ERROR: cannot read from IMU')
        return -1


def getAltitude():
    global pressure

    pressureValid, pressure, _, _ = pressure.pressureRead()
    if pressureValid:
        return computeHeight(pressure)
    else:
        return -1


def getQuaternion():
    global imu

    if imu.IMURead():
        # x, y, z = imu.getFusionData()
        # print("%f %f %f" % (x,y,z))
        data = imu.getIMUData()
        fusionQPose = data["fusionQPose"]
        quat = Quaternion()

        quat.w = fusionQPose[0]
        quat.x = fusionQPose[1]
        quat.y = fusionQPose[2]
        quat.z = fusionQPose[3]

        return quat

    else:
        print('ERROR: cannot read from IMU')
        return -1


def getRate():
    global imu

    return imu.IMUGetPollInterval()
