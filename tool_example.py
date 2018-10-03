from Qt import QtCore, QtWidgets, QtGui
from Qt.QtCore import QThread
import time


"""
https://stackoverflow.com/questions/42785859/pyqt-progress-bar-update-with-threads
"""


class progressThread(QtCore.QThread):

    progress_update = QtCore.Signal(int) # or pyqtSignal(int)

    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self.wait()


    def run(self):
        # your logic here
        while 1:
            maxVal = 1 # NOTE THIS CHANGED to 1 since updateProgressBar was updating the value by 1 every time
            self.progress_update.emit(maxVal) # self.emit(SIGNAL('PROGRESS'), maxVal)
            # Tell the thread to sleep for 1 second and let other things run
            time.sleep(1)


def updateProgressBar(self, maxVal):
    self.ui.progressBar.setValue(self.ui.progressBar.value() + maxVal)
    if maxVal == 0:
        self.ui.progressBar.setValue(100)

class Tool(QtCore.QObject):

    def __init__(self):
        self.ui = UI(self)


    def slow_process(self):
        for i in range(100):
            print i
            time.sleep(1)

    def on_start_clicked(self):
        print "start!"
        # self.slow_process()

    def on_stop_clicked(self):
        print "stop!"
        # self.slow_process()

    def show(self):
        self.ui.start_clicked_signal.connect(self.on_start_clicked)
        self.ui.stop_clicked_signal.connect(self.on_stop_clicked)
        self.ui.show_self()

class UI(QtWidgets.QWidget):

    start_clicked_signal = QtCore.Signal(str)
    stop_clicked_signal = QtCore.Signal(str)

    def __init__(self, controller, parent=None):
        super(UI, self).__init__(parent)

        self.start_btn=QtWidgets.QPushButton("start")
        self.stop_btn = QtWidgets.QPushButton("stop")
        self.status=QtWidgets.QLabel("...")
        self.bar=QtWidgets.QProgressBar()

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.start_btn)
        self.layout.addWidget(self.stop_btn)
        self.layout.addWidget(self.status)
        self.layout.addWidget(self.bar)

        self.start_btn.clicked.connect(self.on_start_clicked)
        self.stop_btn.clicked.connect(self.on_stop_clicked)

    def on_start_clicked(self):
        self.start_clicked_signal.emit('on_start_clicked')

    def on_stop_clicked(self):
        self.stop_clicked_signal.emit('on_stop_clicked')

    def show_self(self):
        global UI

        try:
            UI.close()
            UI.deleteLater()
        except:
            pass
        UI = self
        UI.show()


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication([])
    tool=Tool()
    tool.show()
    sys.exit(app.exec_())
