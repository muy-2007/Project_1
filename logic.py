from PyQt6.QtWidgets import *
from gui import *


class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Logic, self).__init__()
        self.setupUi(self)

        self.button_power.clicked.connect(lambda : self.power())

    def power(self):
        screen = self.screen()
        screen.
