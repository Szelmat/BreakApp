import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle('Break App')
    window.setGeometry(100, 100, 800, 800)
    window.move(60, 15)
    
    window.show()
    sys.exit(app.exec_())