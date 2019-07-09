import time

import utils.IMU as imu

poll_interval = imu.getRate()

while True:
    rpy = imu.getRPY()
    quat = imu.getQuaternion()

    if rpy is not -1:
        print('roll: %f / pitch: %f / yaw: %f' % (rpy.roll, rpy.pitch, rpy.yaw))

    if quat is not -1:
        print('x: %f / y: %f / z: %f / w: %f' % (quat.x, quat.y, quat.z, quat.w))

    time.sleep(poll_interval * 1.0 / 1000.0)