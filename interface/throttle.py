from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *


class Throttle(QWidget):
    def __init__(self, server):
        QWidget.__init__(self)
        self.s = server
        self.slider = QSlider(Qt.Vertical)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.setMinimumSize(QSize(50, 200))
        self.text = QLabel('0%')
        self.text.setFont(QFont('SansSerif', 11))
        self.text.setAlignment(Qt.AlignCenter)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.slider)
        self.slider.sliderMoved.connect(self.slider_moved)
        self.setLayout(self.layout)

    def slider_moved(self):
        t = self.slider.value()
        self.text.setText(str(t) + '%')
        self.s.send('throttle>' + str(t))



