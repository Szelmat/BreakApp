import time
from playsound import playsound

from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QProgressBar,
    QVBoxLayout,
)
from PyQt5 import QtCore
from PyQt5.QtCore import QThread
from PyQt5.QtGui import QFont


class InfoPanel(QWidget):
    def __init__(self):
        super().__init__()
        self.title_label = QLabel("")
        self.title_label.setFont(QFont('Segoe UI', 13))
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.timer_label = QLabel("")
        self.timer_label.setFont(QFont('Segoe UI', 11))
        self.timer_label.setAlignment(QtCore.Qt.AlignCenter)

        self.progressbar = QProgressBar()
        self.progressbar.setFormat("")
        self.progressbar.setAlignment(QtCore.Qt.AlignCenter)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.layout.addWidget(self.title_label)
        self.layout.addWidget(self.timer_label)
        self.layout.addWidget(self.progressbar)

    def alarm(self, desc: str) -> bool:
        '''Play the alarm sound and display the prompt'''
        self.title_label.setText(desc)
        playsound("res/alarm.wav")
        self.change_info(desc)

    def change_info(self, title: str):
        '''Show the current action on the middle panel'''
        self.title_label.setText(title)
        self.thread = Thread()
        self.thread._signal.connect(self.signal_accept)
        self.thread.start()

    def signal_accept(self, msg):
        '''Get the current value of the progressbar and display it'''
        self.progressbar.setValue(int(msg))
        if self.progressbar.value() == 99:
            self.progressbar.setValue(0)
            self.title_label.setText("")


class Thread(QThread):
    _signal = QtCore.pyqtSignal(int)

    def __init__(self):
        super(Thread, self).__init__()

    def __del__(self):
        self.wait()

    def run(self):
        '''Wait and send the current progress of the timeout'''
        seconds = 0.0
        STEP = 0.2
        while(True):
            val = (seconds / 4.0) * 100
            self._signal.emit(val)
            if(val >= 99):
                self._signal.emit(99)
                return
            time.sleep(0.1)
            seconds += STEP
