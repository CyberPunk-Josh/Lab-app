from menu_design import *
from PySide6.QtWidgets import QApplication, QMainWindow


class RModel(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.RM_Graph.clicked.connect(self.message)

    def message(self):
        print("hello world")
