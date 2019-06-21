import sys
from PySide2 import QtCore, QtWidgets, QtGui
from interface.joystick import Joystick


class Throttle(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)

        self.slider = QtWidgets.QSlider(QtCore.Qt.Vertical)
        self.text = QtWidgets.QLabel('0')
        self.text.setAlignment(QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.slider)
        self.setLayout(self.layout)


class DPad(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)

        self.left = QtWidgets.QPushButton('left')
        self.right = QtWidgets.QPushButton('right')
        self.forward = QtWidgets.QPushButton('front')
        self.back = QtWidgets.QPushButton('back')

        self.layout = QtWidgets.QVBoxLayout()
        self.hbox = QtWidgets.QHBoxLayout()

        self.hbox.addWidget(self.left)
        self.hbox.addWidget(self.right)

        self.layout.addWidget(self.forward)
        self.layout.addLayout(self.hbox)
        self.layout.addWidget(self.back)
        self.setLayout(self.layout)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = QtWidgets.QWidget()

    throttle = Throttle()

    layout = QtWidgets.QHBoxLayout()
    layout.addWidget(throttle)

    # Create joystick
    joystick = Joystick()

    # ml.addLayout(joystick.get_joystick_layout(),0,0)
    layout.addWidget(joystick)

    win.setLayout(layout)
    win.show()
    sys.exit(app.exec_())
