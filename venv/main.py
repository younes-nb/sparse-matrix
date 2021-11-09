import sys
from PyQt6.QtWidgets import QApplication
from Controller import Controller

app = QApplication(sys.argv)
window = Controller()
window.view.show()
sys.exit(app.exec())
