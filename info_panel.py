import threading

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
        self.title_label.setFont(QFont('Segoe UI', 18))
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.timer_label = QLabel("")
        self.timer_label.setFont(QFont('Segoe UI', 18))
        self.timer_label.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar = QProgressBar()

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.layout.addWidget(self.title_label)
        self.layout.addWidget(self.timer_label)
        self.layout.addWidget(self.progressBar)

    def change_info(self, title: str, time: str):
        self.titleLabel.setText(title)
        self.timerLabel.setText(time)
        self.cycle_thread = threading.Thread(target=self.cycle)
        self.cycle_thread.start()
        self.cycle_thread.join()

    def cycle(self):
        
