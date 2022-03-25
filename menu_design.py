# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menuIJLXal.ui'
##
## Created by: Qt User Interface Compiler version 6.1.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

from pyqtgraph import PlotWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1250, 950)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_superior = QFrame(self.centralwidget)
        self.frame_superior.setObjectName(u"frame_superior")
        self.frame_superior.setMaximumSize(QSize(16777215, 40))
        self.frame_superior.setSizeIncrement(QSize(0, 40))
        self.frame_superior.setStyleSheet(u"background-color:rgb(52, 152, 219)")
        self.frame_superior.setFrameShape(QFrame.StyledPanel)
        self.frame_superior.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_superior)
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.bt_menu = QPushButton(self.frame_superior)
        self.bt_menu.setObjectName(u"bt_menu")
        self.bt_menu.setMinimumSize(QSize(200, 35))
        self.bt_menu.setMaximumSize(QSize(16777215, 35))
        self.bt_menu.setStyleSheet(u"QPushButton{\n"
"background-color: #aa00ff;\n"
"font:87 12pt *Arial Black*;\n"
"border-radius:0px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #ffff;\n"
"font:87 12pt *Arial Black*;\n"
"}")
        icon = QIcon()
        icon.addFile(u"images/barra-de-menus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_menu.setIcon(icon)
        self.bt_menu.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.bt_menu)

        self.horizontalSpacer = QSpacerItem(430, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.bt_minimizar = QPushButton(self.frame_superior)
        self.bt_minimizar.setObjectName(u"bt_minimizar")
        self.bt_minimizar.setMaximumSize(QSize(16777215, 35))
        self.bt_minimizar.setStyleSheet(u"QPushButton{\n"
"border:0px;\n"
"}\n"
"QPushButton:hover{\n"
"border:5px solid #aa00ff;\n"
"background-color:#ffff00;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"images/minimizar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_minimizar.setIcon(icon1)
        self.bt_minimizar.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.bt_minimizar)

        self.bt_cerrar = QPushButton(self.frame_superior)
        self.bt_cerrar.setObjectName(u"bt_cerrar")
        self.bt_cerrar.setMaximumSize(QSize(16777215, 35))
        self.bt_cerrar.setStyleSheet(u"color: rgb(255, 255, 255);")
        icon2 = QIcon()
        icon2.addFile(u"images/cerrar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_cerrar.setIcon(icon2)
        self.bt_cerrar.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.bt_cerrar)


        self.verticalLayout.addWidget(self.frame_superior)

        self.frame_inferior = QFrame(self.centralwidget)
        self.frame_inferior.setObjectName(u"frame_inferior")
        self.frame_inferior.setFrameShape(QFrame.StyledPanel)
        self.frame_inferior.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_inferior)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_lateral = QFrame(self.frame_inferior)
        self.frame_lateral.setObjectName(u"frame_lateral")
        self.frame_lateral.setMinimumSize(QSize(0, 0))
        self.frame_lateral.setMaximumSize(QSize(0, 16777215))
        self.frame_lateral.setStyleSheet(u"QFrame{\n"
"background-color:#3498DB \n"
"}\n"
"QPushButton{\n"
"background-color:#aa55ff;\n"
"border-top-left-radius:20px;\n"
"border-bottom-left-radius:20px;\n"
"font:75 12pt*Arial Narrow*;\n"
"}\n"
"QPushButton:hover:{\n"
"background-color:white;\n"
"border-top-left-radius:20px;\n"
"border-bottom-left-radius:20px;\n"
"font:75 12pt *Arial Narrow*;\n"
"}")
        self.frame_lateral.setFrameShape(QFrame.StyledPanel)
        self.frame_lateral.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_lateral)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.bt_inicio = QPushButton(self.frame_lateral)
        self.bt_inicio.setObjectName(u"bt_inicio")
        self.bt_inicio.setMinimumSize(QSize(0, 40))
        self.bt_inicio.setMaximumSize(QSize(16777215, 40))
        icon3 = QIcon()
        icon3.addFile(u"images/reological_model.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_inicio.setIcon(icon3)
        self.bt_inicio.setIconSize(QSize(32, 32))

        self.verticalLayout_3.addWidget(self.bt_inicio)

        self.bt_uno = QPushButton(self.frame_lateral)
        self.bt_uno.setObjectName(u"bt_uno")
        self.bt_uno.setMinimumSize(QSize(0, 40))
        self.bt_uno.setMaximumSize(QSize(16777215, 40))
        icon4 = QIcon()
        icon4.addFile(u"images/database.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_uno.setIcon(icon4)
        self.bt_uno.setIconSize(QSize(32, 32))

        self.verticalLayout_3.addWidget(self.bt_uno)

        self.bt_2 = QPushButton(self.frame_lateral)
        self.bt_2.setObjectName(u"bt_2")
        self.bt_2.setMinimumSize(QSize(0, 40))
        self.bt_2.setMaximumSize(QSize(16777215, 40))
        icon5 = QIcon()
        icon5.addFile(u"images/deltap.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_2.setIcon(icon5)
        self.bt_2.setIconSize(QSize(32, 32))

        self.verticalLayout_3.addWidget(self.bt_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.frame_lateral)

        self.frame_contenedor = QFrame(self.frame_inferior)
        self.frame_contenedor.setObjectName(u"frame_contenedor")
        self.frame_contenedor.setFrameShape(QFrame.StyledPanel)
        self.frame_contenedor.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_contenedor)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame_contenedor)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.RM_Widget = PlotWidget(self.page)
        self.RM_Widget.setObjectName(u"RM_Widget")
        self.RM_Widget.setGeometry(QRect(380, 30, 701, 801))
        self.gridLayoutWidget = QWidget(self.page)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(30, 580, 321, 251))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.RM_Va = QSpinBox(self.gridLayoutWidget)
        self.RM_Va.setObjectName(u"RM_Va")
        self.RM_Va.setReadOnly(True)

        self.gridLayout.addWidget(self.RM_Va, 1, 1, 1, 1)

        self.RM_Vp = QSpinBox(self.gridLayoutWidget)
        self.RM_Vp.setObjectName(u"RM_Vp")
        self.RM_Vp.setReadOnly(True)

        self.gridLayout.addWidget(self.RM_Vp, 2, 1, 1, 1)

        self.RM_Pc = QSpinBox(self.gridLayoutWidget)
        self.RM_Pc.setObjectName(u"RM_Pc")
        self.RM_Pc.setReadOnly(True)

        self.gridLayout.addWidget(self.RM_Pc, 3, 1, 1, 1)

        self.verticalLayoutWidget = QWidget(self.page)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(30, 20, 331, 521))
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_4)

        self.RM_ComboBox = QComboBox(self.verticalLayoutWidget)
        self.RM_ComboBox.setObjectName(u"RM_ComboBox")

        self.verticalLayout_4.addWidget(self.RM_ComboBox)

        self.RM_TableWidget = QTableWidget(self.verticalLayoutWidget)
        if (self.RM_TableWidget.columnCount() < 2):
            self.RM_TableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.RM_TableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.RM_TableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.RM_TableWidget.rowCount() < 6):
            self.RM_TableWidget.setRowCount(6)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.RM_TableWidget.setVerticalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.RM_TableWidget.setVerticalHeaderItem(1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.RM_TableWidget.setVerticalHeaderItem(2, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.RM_TableWidget.setVerticalHeaderItem(3, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.RM_TableWidget.setVerticalHeaderItem(4, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.RM_TableWidget.setVerticalHeaderItem(5, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem8.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable);
        self.RM_TableWidget.setItem(0, 0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem9.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable);
        self.RM_TableWidget.setItem(1, 0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem10.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable);
        self.RM_TableWidget.setItem(2, 0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem11.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable);
        self.RM_TableWidget.setItem(3, 0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem12.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable);
        self.RM_TableWidget.setItem(4, 0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem13.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable);
        self.RM_TableWidget.setItem(5, 0, __qtablewidgetitem13)
        self.RM_TableWidget.setObjectName(u"RM_TableWidget")

        self.verticalLayout_4.addWidget(self.RM_TableWidget)

        self.RM_Graph = QPushButton(self.verticalLayoutWidget)
        self.RM_Graph.setObjectName(u"RM_Graph")

        self.verticalLayout_4.addWidget(self.RM_Graph)

        self.RM_Clear = QPushButton(self.verticalLayoutWidget)
        self.RM_Clear.setObjectName(u"RM_Clear")

        self.verticalLayout_4.addWidget(self.RM_Clear)

        self.RM_Save = QPushButton(self.verticalLayoutWidget)
        self.RM_Save.setObjectName(u"RM_Save")

        self.verticalLayout_4.addWidget(self.RM_Save)

        self.stackedWidget.addWidget(self.page)
        self.page_uno = QWidget()
        self.page_uno.setObjectName(u"page_uno")
        self.pushButton_2 = QPushButton(self.page_uno)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(210, 180, 231, 171))
        self.stackedWidget.addWidget(self.page_uno)
        self.page_dos = QWidget()
        self.page_dos.setObjectName(u"page_dos")
        self.pushButton_3 = QPushButton(self.page_dos)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(190, 190, 231, 141))
        self.stackedWidget.addWidget(self.page_dos)
        self.page_tres = QWidget()
        self.page_tres.setObjectName(u"page_tres")
        self.pushButton_4 = QPushButton(self.page_tres)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(180, 170, 221, 141))
        self.stackedWidget.addWidget(self.page_tres)
        self.page_cuatro = QWidget()
        self.page_cuatro.setObjectName(u"page_cuatro")
        self.pushButton_5 = QPushButton(self.page_cuatro)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(170, 210, 241, 121))
        self.stackedWidget.addWidget(self.page_cuatro)
        self.page_cinco = QWidget()
        self.page_cinco.setObjectName(u"page_cinco")
        self.pushButton_12 = QPushButton(self.page_cinco)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setGeometry(QRect(180, 210, 231, 111))
        self.stackedWidget.addWidget(self.page_cinco)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.frame_contenedor)


        self.verticalLayout.addWidget(self.frame_inferior)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.bt_menu.setText(QCoreApplication.translate("MainWindow", u"  MENU", None))
        self.bt_minimizar.setText("")
        self.bt_cerrar.setText("")
        self.bt_inicio.setText(QCoreApplication.translate("MainWindow", u" Modelo R", None))
        self.bt_uno.setText(QCoreApplication.translate("MainWindow", u" Base de Datos", None))
        self.bt_2.setText(QCoreApplication.translate("MainWindow", u"DEC", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Viscosidad Aparente", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Punto de Cedencia", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Viscosidad Pl\u00e0stica", None))
        self.RM_Va.setSuffix(QCoreApplication.translate("MainWindow", u" cp", None))
        self.RM_Va.setPrefix("")
        self.RM_Vp.setSuffix(QCoreApplication.translate("MainWindow", u" cp", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Temperatura", None))
        ___qtablewidgetitem = self.RM_TableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"RPM", None));
        ___qtablewidgetitem1 = self.RM_TableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u03a6", None));
        ___qtablewidgetitem2 = self.RM_TableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem3 = self.RM_TableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem4 = self.RM_TableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem5 = self.RM_TableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem6 = self.RM_TableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem7 = self.RM_TableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"6", None));

        __sortingEnabled = self.RM_TableWidget.isSortingEnabled()
        self.RM_TableWidget.setSortingEnabled(False)
        ___qtablewidgetitem8 = self.RM_TableWidget.item(0, 0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem9 = self.RM_TableWidget.item(1, 0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem10 = self.RM_TableWidget.item(2, 0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"100", None));
        ___qtablewidgetitem11 = self.RM_TableWidget.item(3, 0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"200", None));
        ___qtablewidgetitem12 = self.RM_TableWidget.item(4, 0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"300", None));
        ___qtablewidgetitem13 = self.RM_TableWidget.item(5, 0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"600", None));
        self.RM_TableWidget.setSortingEnabled(__sortingEnabled)

        self.RM_Graph.setText(QCoreApplication.translate("MainWindow", u"Gr\u00e0fico", None))
        self.RM_Clear.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.RM_Save.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"5", None))
    # retranslateUi

