import math

from PyQt5 import QtCore
from PyQt5.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
)

class TimerPanel(QWidget):
    def __init__(self, name:str, seconds:int):
        super().__init__()
        self.name = name
        self.seconds = seconds
        self.build_widget()

    def build_widget(self):
        self.title_label = self.get_title_label(self.name)
        self.time_label = self.get_time_label(self.seconds)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.layout.addWidget(self.title_label)
        self.layout.addWidget(self.time_label)

    def get_title_label(self, title:str) -> QLabel:
        label = QLabel(f"<h1>{title}</h1>")
        label.setAlignment(QtCore.Qt.AlignCenter)
        return label

    def get_time_label(self, seconds:int) -> QLabel:
        mins, secs = self.calculate_time()
        label = QLabel(f"<h2>{str(mins)}:{str(secs)}</h2>")
        label.setAlignment(QtCore.Qt.AlignCenter)
        return label

    def calculate_time(self):
        minutes_seconds = []
        minutes_seconds.append(math.floor(self.seconds / 60))
        minutes_seconds.append(self.seconds % 60)
        return minutes_seconds