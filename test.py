import time

import utils.IMU as imu

poll_interval = imu.getRate()

while True:
    rpy = imu.getRPY()

    if rpy is not -1:
        print('roll: %f / pitch: %f / yaw: %f' % (rpy.roll, rpy.pitch, rpy.yaw))

    time.sleep(poll_interval * 1.0 / 1000.0)
