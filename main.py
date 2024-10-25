from PyQt5.QtWidgets import QApplication
from asosiy import MainWindow



app = QApplication([])
win = MainWindow()
win.show()
app.exec_()