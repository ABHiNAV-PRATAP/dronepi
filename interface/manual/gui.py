import sys
from PySide2 import QtWidgets
from interface.joystick import Joystick
from interface.throttle import Throttle
from interface.yaw import YawController
from utils.server import Server


class eStop(QtWidgets.QWidget):
    def __init__(self, server, parent=None):
        super(eStop, self).__init__(parent)
        self.s = server

        self.layout = QtWidgets.QVBoxLayout()

        self.button = QtWidgets.QPushButton('E-STOP')
        self.button.setStyleSheet("background-color: red; color: white")

        self.layout.addWidget(self.button)
        self.button.clicked.connect(self.stop)
        self.setLayout(self.layout)

    def stop(self):
        self.s.send('ESTOP')


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    s = Server(22000)
    win = QtWidgets.QWidget()

    throttle = Throttle(s)
    joystick = Joystick(s)
    yaw = YawController(s)
    eStop = eStop(s)

    vbox = QtWidgets.QVBoxLayout()
    vbox.addWidget(eStop)
    vbox.addWidget(yaw)

    layout = QtWidgets.QHBoxLayout()
    layout.addWidget(throttle)
    layout.addLayout(vbox)
    layout.addWidget(joystick)
    layout.setSpacing(10)

    win.setLayout(layout)
    win.show()
    win.setWindowTitle('Manual Control')
    sys.exit(app.exec_())
