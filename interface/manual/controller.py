import sys
from PySide2 import QtWidgets
from interface.joystick import Joystick
from interface.throttle import Throttle
from interface.yaw import YawController

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = QtWidgets.QWidget()

    throttle = Throttle()
    joystick = Joystick()
    yaw = YawController()

    layout = QtWidgets.QHBoxLayout()
    layout.addWidget(throttle)
    layout.addWidget(yaw)
    layout.addWidget(joystick)
    layout.setSpacing(10)

    win.setLayout(layout)
    win.show()
    win.setWindowTitle('Manual Control')
    sys.exit(app.exec_())
