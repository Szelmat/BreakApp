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

from timer_panel import TimerPanel


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

        self.timer_panels = (
            TimerPanel("Relax Eyes", 5),  # 900
            TimerPanel("Rest Hands", 2400),
            TimerPanel("Stand up", 3600),
            TimerPanel("Stretch", 7200),
        )

        alarm_checker_thread = threading.Thread(target=self.check_alarms, daemon=True)
        alarm_checker_thread.start()

    def check_alarms(self):
        while(True):
            for timer_panel in self.timer_panels:
                if timer_panel.finished:
                    self.alarm("test")
                    timer_panel.reset()
            time.sleep(0.1)

    def alarm(self, desc: str) -> bool:
        '''Play the alarm sound and display the prompt'''
        self.title_label.setText(desc)
        playsound("res/alarm.wav")
        self.change_info(desc)
        pb_thread = threading.Thread(target=self.timeout, daemon=True)
        pb_thread.start()
        pb_thread.join()
        self.change_info('')

    def change_info(self, desc: str):
        self.title_label.setText(desc)

    def timeout(self):
        i = 0.1
        while(i < 5):
            self.progressbar.setValue(i / 5 * 100)
            time.sleep(0.1)
            i += 0.1
