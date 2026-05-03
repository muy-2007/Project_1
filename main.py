from logic import *

def main():
    application = QApplication([])
    window = Logic()
    window.show()
    application.exec_()


if __name__ == '__main__':
    main()