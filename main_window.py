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
        self.middle_panel = InfoPanel()
        self.init_ui()

    def init_ui(self):
        self.resize(1200, 700)
        self.build_layout()
        self.setWindowTitle('BreakApp')
        self.show()

    def build_layout(self):
        '''Add elements to the window to the correct place'''
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.layout.addWidget(
            TimerPanel("Relax Eyes", 900, self.middle_panel), 0, 0, 1, 3)
        self.layout.addWidget(
            TimerPanel("Rest Hands", 2400, self.middle_panel), 1, 0)
        self.layout.addWidget(
            TimerPanel("Stand up", 3600, self.middle_panel), 1, 2)
        self.layout.addWidget(
            TimerPanel("Stretch", 7200, self.middle_panel), 2, 0, 1, 3)

        self.layout.addWidget(self.middle_panel, 1, 1)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec_())
