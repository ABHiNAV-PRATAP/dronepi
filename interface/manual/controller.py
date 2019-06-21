import sys
from PySide2 import QtWidgets
from interface.joystick import Joystick
from interface.throttle import Throttle
from interface.yaw import YawController


class eStop(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(eStop, self).__init__(parent)

        self.layout = QtWidgets.QVBoxLayout()

        self.button = QtWidgets.QPushButton('E-STOP')
        self.button.setStyleSheet("background-color: red; color: white")

        self.layout.addWidget(self.button)
        self.button.clicked.connect(self.stop)
        self.setLayout(self.layout)

    def stop(self):
        print('STOPPPPPPPPPPPPPPPPPPPPPPPPP')


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = QtWidgets.QWidget()

    throttle = Throttle()
    joystick = Joystick()
    yaw = YawController()
    eStop = eStop()

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
