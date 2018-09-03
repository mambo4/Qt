import sys
# from PyQt.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QApplication, QWidget, QTabWidget

class Widget(QTabWidget):

    def __init__(self):
        super(Widget,self).__init__()
        self.title="Andrea <3"
        self.top=100
        self.left=300
        self.width=640
        self.height=480
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    print(app,type(app))
    w = Widget()
    sys.exit(app.exec_())