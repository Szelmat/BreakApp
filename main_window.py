import sys

from PyQt5.QtWidgets import (
    QWidget,
    QDesktopWidget,
    QApplication,
    QGridLayout,
)

from timer_panel import TimerPanel
from info_panel import InfoPanel


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.center_panel = InfoPanel()
        self.init_ui()
        self.middle_panel = InfoPanel()
        self.middle_panel.alarm("Test")

    def init_ui(self):
        self.resize(1200, 700)
        self.build_layout()
        self.center()
        self.setWindowTitle('BreakApp')
        self.show()

    def build_layout(self):
        '''Add elements to the window to the correct place'''
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.layout.addWidget(TimerPanel("Relax Eyes", 900), 0, 0, 1, 3)
        self.layout.addWidget(TimerPanel("Rest Hands", 2400), 1, 0)

        self.layout.addWidget(self.center_panel, 1, 1)

        self.layout.addWidget(TimerPanel("Stand up", 3600), 1, 2)
        self.layout.addWidget(TimerPanel("Stretch", 7200), 2, 0, 1, 3)

    def center(self):
        '''Center the window'''
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec_())
