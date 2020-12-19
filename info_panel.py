import time
import threading

from playsound import playsound

from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QProgressBar,
    QVBoxLayout,
)
from PyQt5 import QtCore
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

    def change_info(self, title: str, time: str):
        self.title_label.setText(title)
        self.timer_label.setText(time)
        # self.cycle_thread = threading.Thread(target=self.cycle, daemon=True)
        # self.cycle_thread.start()
        # self.cycle_thread.join()

    def cycle(self):
        seconds = 0.0
        step = 0.1
        while(True):
            time.sleep(step)
            seconds += step
            self.update_progressbar(seconds)
            if(seconds >= 4):
                return

    def update_progressbar(self, seconds: int):
        self.progressbar.setValue((seconds / 4.0) * 100)

    def alarm(self, desc: str) -> bool:
        self.title_label.setText(desc)
        playsound("res/alarm.wav")
        time.sleep(5)
        self.title_label.setText("")
