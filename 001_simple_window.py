#!/usr/bin/env python3
import sys
from Qt.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    
    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle('Logan')
    w.show()
    
    sys.exit(app.exec_())
