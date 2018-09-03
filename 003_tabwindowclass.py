import sys
# from PyQt.QtWidgets import QApplication, QWidget
from Qt.QtWidgets import QApplication, QWidget, QTabWidget,QVBoxLayout,QPushButton,QApplication,QLabel

class Widget(QTabWidget):

    def __init__(self):
        super(Widget,self).__init__()
        self.title="Andrea <3"
        self.top=100
        self.left=300
        self.width=200
        self.height=480
        self.msg="Nothing going on..."
        self.label=QLabel()
        self.label.setText(self.msg)
        self.build_button1()
        self.build_tab1()
        self.build_tab2()

        self.init_ui()

    def button1_clicked(self):
        self.msg="Button 1 has been clicked."
        self.label.setText(self.msg)
        print(self.msg)

    def build_button1(self):
        self.button1=QPushButton("Button1")
        self.button1.clicked.connect(self.button1_clicked)

    def build_tab1(self):
        self.tab1=QWidget()
        self.tab1.layout=QVBoxLayout(self)
        self.tab1.layout.addWidget(self.button1)
        self.tab1.setLayout(self.tab1.layout)

    def build_tab2(self):
        self.tab2=QWidget()
        self.tab2.layout=QVBoxLayout(self)
        self.tab2.layout.addWidget(self.label)
        self.tab2.setLayout(self.tab2.layout)
        
    def init_ui(self):
        self.setWindowTitle(self.title)
        self.addTab(self.tab1,"tab 1")
        self.addTab(self.tab2,"tab 2")
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    print(app,type(app))
    w = Widget()
    sys.exit(app.exec_())