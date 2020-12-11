import math
import time
import threading

from PyQt5 import QtCore
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
)


class TimerPanel(QWidget):
    def __init__(self, name: str, seconds: int):
        super().__init__()
        self.name = name
        self.seconds = seconds
        self.build_widget()
        x = threading.Thread(target=self.countdown, daemon=True)
        x.start()

    def build_widget(self):
        self.title_label = self.get_title_label(self.name)
        self.time_label = self.get_time_label()
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.layout.addWidget(self.title_label)
        self.layout.addWidget(self.time_label)

    def get_title_label(self, title: str) -> QLabel:
        label = QLabel(f"{title}")
        label.setFont(QFont('Segoe UI', 18))
        label.setAlignment(QtCore.Qt.AlignCenter)
        return label

    def get_time_label(self) -> QLabel:
        label = QLabel(self.format_time())
        label.setFont(QFont('Segoe UI', 15))
        label.setAlignment(QtCore.Qt.AlignCenter)
        return label

    def calculate_time(self):
        minutes_seconds = []
        minutes_seconds.append(math.floor(self.seconds / 60))
        minutes_seconds.append(self.seconds % 60)
        return minutes_seconds

    def format_time(self) -> str:
        mins, secs = self.calculate_time()
        return f"{str(mins).zfill(2)}:{str(secs).zfill(2)}"

    def countdown(self):
        while(True):
            self.seconds -= 1
            self.time_label.setText(self.format_time())
            time.sleep(1)
