import sys
from PyQt5 import QtWidgets
from fiets_ui import Ui_MainWindow

class Program(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()

app = QtWidgets.QApplication(sys.argv)
w = Program()
w.show()
sys.exit(app.exec_())
