from menu_design import *
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Qt, QEasingCurve

# Local files
from reologicalOne.reological import RModel
from reologicalTwo.reologicalDB import RModelDB
from density.density import Density


import sys


# class for menu
class MiApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # eliminar barra y de titulo - opacidad
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowOpacity(1)

        # mover ventana
        self.frame_superior.mouseMoveEvent = self.mover_ventana

        # acceder a las paginas
        self.bt_inicio.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page))
        self.bt_uno.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_uno))
        self.bt_2.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_dos))

        # control barra de titulos
        self.bt_minimizar.clicked.connect(self.control_bt_minimizar)
        self.bt_cerrar.clicked.connect(lambda: self.close())

        # menu lateral
        self.bt_menu.clicked.connect(self.mover_menu)

        # reological model
        # self.RM_Graph.clicked.connect(self.message)

    def control_bt_minimizar(self):
        self.showMinimized()

    def control_bt_normal(self):
        self.showNormal()

    def mover_menu(self):
        if True:
            width = self.frame_lateral.width()
            normal = 0
            if width == 0:
                extender = 200
            else:
                extender = normal
            self.animacion = QPropertyAnimation(self.frame_lateral, b'minimumWidth')
            self.animacion.setDuration(300)
            self.animacion.setStartValue(width)
            self.animacion.setEndValue(extender)
            self.animacion.setEasingCurve(QEasingCurve.InOutQuart)
            self.animacion.start()

    ## mover ventana
    def mousePressEvent(self, event):
        self.clickPosition = event.globalPosition().toPoint()

    def mover_ventana(self, event):
        if self.isMaximized() == False:
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPosition().toPoint() - self.clickPosition)
                self.clickPosition = event.globalPosition().toPoint()
                event.accept()
        else:
            self.showNormal()


class Global(Density, RModelDB, RModel, MiApp):
    def __init__(self):
        super().__init__()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mi_app = Global()
    mi_app.show()
    sys.exit(app.exec())
