from PySide2.QtCore import *
from PySide2.QtWidgets import *


class YawController(QWidget):
    def __init__(self, server, parent=None):
        super(YawController, self).__init__(parent)
        self.s = server
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(-10)
        self.slider.setMaximum(10)
        self.slider.setValue(0)
        self.slider.setTickInterval(1)
        self.slider.setMinimumSize(QSize(200, 50))

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.slider)
        self.slider.sliderReleased.connect(self.slider_released)
        self.slider.sliderMoved.connect(self.slider_drag)
        self.setLayout(self.layout)

    def slider_released(self):
        self.slider.setSliderPosition(0)

    def slider_drag(self):
        self.s.send('yaw>' + str(self.slider.value()/10))