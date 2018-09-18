import sys
# from PyQt.QtWidgets import QApplication, QWidget
import Qt.QtWidgets as QtWidgets
import Qt
class Widget(QtWidgets.QWidget):

    def __init__(self):
        super(Widget,self).__init__()
        self.title="Folder Stub"
        self.top=100
        self.left=300
        self.width=640
        self.height=480
        self.asset_types=["characters","monsters","objects","player"]
        self.set_widgets()
        self.set_layout()
        self.set_window()
        

    def set_widgets(self):
        self.assetname_lable=QtWidgets.QLabel("Asset Name")
        self.assetname_editText=QtWidgets.QLineEdit()
        self.assettype_lable=QtWidgets.QLabel("Asset Type")
        self.assettype_combobox=QtWidgets.QComboBox()
        self.assettype_combobox.addItems(self.asset_types)

    def set_layout(self):
        self.layout =QtWidgets.QHBoxLayout()
        self.layout.addWidget(self.assetname_lable)
        self.layout.addWidget(self.assetname_editText)
        self.layout.addWidget(self.assettype_lable)
        self.layout.addWidget(self.assettype_combobox)
 
    def set_window(self):
        self.setWindowTitle(self.title)
        self.setLayout(self.layout)

        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()

if __name__ == '__main__':
    
    app = QtWidgets.QApplication(sys.argv)
    print(app,type(app))
    w = Widget()
    sys.exit(app.exec_())