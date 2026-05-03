from PyQt6.QtWidgets import *
from gui import *


class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        '''
        Used to create the main window
        param: self
        return: None
        '''
        super(Logic, self).__init__()
        self.setupUi(self)


