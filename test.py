import time

import utils.IMU as imu

poll_interval = imu.getRate()

while True:
    rpy = imu.getRPY()
    quat = imu.getQuaternion()

    if rpy is not -1 and quat is not -1:
        print('roll: %s / pitch: %s / yaw: %s', rpy.roll, rpy.pitch, rpy.yaw)
        print('x: %s / y: %s / z: %s / w: %S', quat.x, quat.y, quat.z, quat.w)

    time.sleep(poll_interval * 1.0 / 1000.0)