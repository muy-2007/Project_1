from PyQt6.QtWidgets import *
from gui import *


class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Logic, self).__init__()
        self.setupUi(self)

        self.button_power.clicked.connect(lambda : self.power())
        self.slider_volume.sliderMoved.connect(lambda : self.volume())
        self.slider_channel.sliderMoved.connect(lambda: self.channel())
        self.radioButton.clicked.connect(lambda : self.mute())

        self.button_0.clicked.connect(lambda : self.channel_0())
        self.button_1.clicked.connect(lambda: self.channel_1())
        self.button_2.clicked.connect(lambda: self.channel_2())
        self.button_3.clicked.connect(lambda: self.channel_3())
        self.button_4.clicked.connect(lambda: self.channel_4())
        self.button_5.clicked.connect(lambda: self.channel_5())

    def power(self):
        pass

    def volume(self):
        pass

    def channel(self):
        pass

    def mute(self):
        pass

    def channel_0(self):
        pass
    def channel_1(self):
        pass
    def channel_2(self):
        pass
    def channel_3(self):
        pass
    def channel_4(self):
        pass
    def channel_5(self):
        pass