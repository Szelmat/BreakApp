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

from info_panel import InfoPanel


class TimerPanel(QWidget):
    def __init__(self, name: str, seconds: int, middle_panel: InfoPanel):
        super().__init__()
        self.name = name
        self.seconds_original = self.seconds = seconds
        self.build_widget()
        self.countdown_thread = threading.Thread(
            target=self.countdown,
            daemon=True
        )
        self.countdown_thread.start()
        self.middle_panel = middle_panel

    def build_widget(self):
        self.title_label = self.get_title_label(self.name)
        self.time_label = self.get_time_label()
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.layout.addWidget(self.title_label)
        self.layout.addWidget(self.time_label)

    def get_title_label(self, title: str) -> QLabel:
        label = QLabel(f"{title}")
        label.setFont(QFont('Segoe UI', 13))
        label.setAlignment(QtCore.Qt.AlignCenter)
        return label

    def get_time_label(self) -> QLabel:
        label = QLabel(self.format_time())
        label.setFont(QFont('Segoe UI', 11))
        label.setAlignment(QtCore.Qt.AlignCenter)
        return label

    def format_time(self) -> str:
        hours, mins, secs = self.calculate_time()
        if hours > 0:
            return (
                f"{str(hours).zfill(2)}:{str(mins).zfill(2)}:"
                f"{str(secs).zfill(2)}"
            )
        else:
            return f"{str(mins).zfill(2)}:{str(secs).zfill(2)}"

    def calculate_time(self) -> list:
        hours_minutes_seconds = []
        hours = math.floor(self.seconds / 3600)
        hours_minutes_seconds.append(hours)
        hours_minutes_seconds.append(
            math.floor(self.seconds / 60) - hours * 60
        )
        hours_minutes_seconds.append(self.seconds % 60)
        return hours_minutes_seconds

    def countdown(self):
        self.finished = False
        while(True):
            self.seconds -= 1
            self.time_label.setText(self.format_time())
            time.sleep(1)
            if self.seconds <= 0:
                self.finished = True
                self.middle_panel.alarm(self.name)
                self.seconds = self.seconds_original
