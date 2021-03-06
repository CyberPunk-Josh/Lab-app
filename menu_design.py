# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menuHIDrhc.ui'
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
        self.gridLayoutWidget.setGeometry(QRect(30, 590, 321, 251))
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
        self.verticalLayoutWidget.setGeometry(QRect(30, 20, 331, 561))
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

        self.RM_Rep = QPushButton(self.verticalLayoutWidget)
        self.RM_Rep.setObjectName(u"RM_Rep")

        self.verticalLayout_4.addWidget(self.RM_Rep)

        self.stackedWidget.addWidget(self.page)
        self.page_uno = QWidget()
        self.page_uno.setObjectName(u"page_uno")
        self.verticalLayoutWidget_2 = QWidget(self.page_uno)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(10, 10, 331, 521))
        self.verticalLayout_5 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.verticalLayoutWidget_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_5)

        self.RM_ComboBoxBD = QComboBox(self.verticalLayoutWidget_2)
        self.RM_ComboBoxBD.setObjectName(u"RM_ComboBoxBD")

        self.verticalLayout_5.addWidget(self.RM_ComboBoxBD)

        self.RM_TableWidgetDB = QTableWidget(self.verticalLayoutWidget_2)
        if (self.RM_TableWidgetDB.columnCount() < 2):
            self.RM_TableWidgetDB.setColumnCount(2)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.RM_TableWidgetDB.setHorizontalHeaderItem(0, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.RM_TableWidgetDB.setHorizontalHeaderItem(1, __qtablewidgetitem15)
        if (self.RM_TableWidgetDB.rowCount() < 6):
            self.RM_TableWidgetDB.setRowCount(6)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.RM_TableWidgetDB.setVerticalHeaderItem(0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.RM_TableWidgetDB.setVerticalHeaderItem(1, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.RM_TableWidgetDB.setVerticalHeaderItem(2, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.RM_TableWidgetDB.setVerticalHeaderItem(3, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.RM_TableWidgetDB.setVerticalHeaderItem(4, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.RM_TableWidgetDB.setVerticalHeaderItem(5, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        __qtablewidgetitem22.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem22.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable);
        self.RM_TableWidgetDB.setItem(0, 0, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        __qtablewidgetitem23.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem23.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable);
        self.RM_TableWidgetDB.setItem(0, 1, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        __qtablewidgetitem24.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem24.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable);
        self.RM_TableWidgetDB.setItem(1, 0, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        __qtablewidgetitem25.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem25.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable);
        self.RM_TableWidgetDB.setItem(1, 1, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        __qtablewidgetitem26.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem26.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable);
        self.RM_TableWidgetDB.setItem(2, 0, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        __qtablewidgetitem27.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem27.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable);
        self.RM_TableWidgetDB.setItem(2, 1, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        __qtablewidgetitem28.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem28.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable);
        self.RM_TableWidgetDB.setItem(3, 0, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        __qtablewidgetitem29.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem29.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable);
        self.RM_TableWidgetDB.setItem(3, 1, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        __qtablewidgetitem30.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem30.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable);
        self.RM_TableWidgetDB.setItem(4, 0, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        __qtablewidgetitem31.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem31.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable);
        self.RM_TableWidgetDB.setItem(4, 1, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        __qtablewidgetitem32.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem32.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable);
        self.RM_TableWidgetDB.setItem(5, 0, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        __qtablewidgetitem33.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem33.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable);
        self.RM_TableWidgetDB.setItem(5, 1, __qtablewidgetitem33)
        self.RM_TableWidgetDB.setObjectName(u"RM_TableWidgetDB")

        self.verticalLayout_5.addWidget(self.RM_TableWidgetDB)

        self.RM_GraphDB = QPushButton(self.verticalLayoutWidget_2)
        self.RM_GraphDB.setObjectName(u"RM_GraphDB")

        self.verticalLayout_5.addWidget(self.RM_GraphDB)

        self.RM_DeleteDB = QPushButton(self.verticalLayoutWidget_2)
        self.RM_DeleteDB.setObjectName(u"RM_DeleteDB")

        self.verticalLayout_5.addWidget(self.RM_DeleteDB)

        self.RM_UpdateDB = QPushButton(self.verticalLayoutWidget_2)
        self.RM_UpdateDB.setObjectName(u"RM_UpdateDB")

        self.verticalLayout_5.addWidget(self.RM_UpdateDB)

        self.gridLayoutWidget_2 = QWidget(self.page_uno)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(20, 540, 321, 141))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.gridLayoutWidget_2)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 1, 0, 1, 1)

        self.label_7 = QLabel(self.gridLayoutWidget_2)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 3, 0, 1, 1)

        self.label_8 = QLabel(self.gridLayoutWidget_2)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 2, 0, 1, 1)

        self.RM_VaDB = QSpinBox(self.gridLayoutWidget_2)
        self.RM_VaDB.setObjectName(u"RM_VaDB")
        self.RM_VaDB.setReadOnly(True)

        self.gridLayout_2.addWidget(self.RM_VaDB, 1, 1, 1, 1)

        self.RM_VpDB = QSpinBox(self.gridLayoutWidget_2)
        self.RM_VpDB.setObjectName(u"RM_VpDB")
        self.RM_VpDB.setReadOnly(True)

        self.gridLayout_2.addWidget(self.RM_VpDB, 2, 1, 1, 1)

        self.RM_PcDB = QSpinBox(self.gridLayoutWidget_2)
        self.RM_PcDB.setObjectName(u"RM_PcDB")
        self.RM_PcDB.setReadOnly(True)

        self.gridLayout_2.addWidget(self.RM_PcDB, 3, 1, 1, 1)

        self.RM_WidgetDB = PlotWidget(self.page_uno)
        self.RM_WidgetDB.setObjectName(u"RM_WidgetDB")
        self.RM_WidgetDB.setGeometry(QRect(370, 10, 701, 681))
        self.RM_WidgetDB.setStyleSheet(u"/*\n"
"Aqua Style Sheet for QT Applications\n"
"Author: Jaime A. Quiroga P.\n"
"Company: GTRONICK\n"
"Last updated: 22/01/2019, 07:55.\n"
"Available at: https://github.com/GTRONICK/QSS/blob/master/Aqua.qss\n"
"*/\n"
"QWidget#window, QMainWindow {\n"
"	background-color:#ececec;\n"
"}\n"
"QTextEdit {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"QPlainTextEdit {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"QToolButton {\n"
"	border-style: solid;\n"
"	border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"	border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));\n"
""
                        "	border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));\n"
"	border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"	color: rgb(0,0,0);\n"
"	padding: 2px;\n"
"	background-color: rgb(255,255,255);\n"
"}\n"
"QToolButton:hover{\n"
"	border-style: solid;\n"
"	border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(195, 195, 195), stop:1 rgb(222, 222, 222));\n"
"	border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(197, 197, 197), stop:1 rgb(227, 227, 227));\n"
"	border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(197, 197, 197));\n"
"	border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(195, 195, 195), stop:1 rgb(222, 222, 222));\n"
"	border-width: 1px;\n"
""
                        "	border-radius: 5px;\n"
"	color: rgb(0,0,0);\n"
"	padding: 2px;\n"
"	background-color: rgb(255,255,255);\n"
"}\n"
"QToolButton:pressed{\n"
"	border-style: solid;\n"
"	border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"	border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));\n"
"	border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));\n"
"	border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"	color: rgb(0,0,0);\n"
"	padding: 2px;\n"
"	background-color: rgb(142,142,142);\n"
"}\n"
"QPushButton{\n"
"	border-style: solid;\n"
"	border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"	"
                        "border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));\n"
"	border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));\n"
"	border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"	color: rgb(0,0,0);\n"
"	padding: 2px;\n"
"	background-color: rgb(255,255,255);\n"
"}\n"
"QPushButton::default{\n"
"	border-style: solid;\n"
"	border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"	border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));\n"
"	border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));\n"
"	border-bottom-color: "
                        "qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"	color: rgb(0,0,0);\n"
"	padding: 2px;\n"
"	background-color: rgb(255,255,255);\n"
"}\n"
"QPushButton:hover{\n"
"	border-style: solid;\n"
"	border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(195, 195, 195), stop:1 rgb(222, 222, 222));\n"
"	border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(197, 197, 197), stop:1 rgb(227, 227, 227));\n"
"	border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(197, 197, 197));\n"
"	border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(195, 195, 195), stop:1 rgb(222, 222, 222));\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"	color: rgb(0,0,0);\n"
"	padding: 2px;\n"
"	background-color: rgb(255,255,255);\n"
"}\n"
"QPushButton:pressed{\n"
"	border-style: s"
                        "olid;\n"
"	border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"	border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));\n"
"	border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));\n"
"	border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"	color: rgb(0,0,0);\n"
"	padding: 2px;\n"
"	background-color: rgb(142,142,142);\n"
"}\n"
"QPushButton:disabled{\n"
"	border-style: solid;\n"
"	border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"	border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));\n"
"	border-left"
                        "-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));\n"
"	border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"	color: #808086;\n"
"	padding: 2px;\n"
"	background-color: rgb(142,142,142);\n"
"}\n"
"QLineEdit {\n"
"	border-width: 1px; border-radius: 4px;\n"
"	border-style: solid;\n"
"	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"QLabel {\n"
"	color: #000000;\n"
"}\n"
"QLCDNumber {\n"
"	color: rgb(0, 113, 255, 255);\n"
"}\n"
"QProgressBar {\n"
"	text-align: center;\n"
"	color: rgb(240, 240, 240);\n"
"	border-width: 1px; \n"
"	border-radius: 10px;\n"
"	border-color: rgb(230, 230, 230);\n"
"	border-style: solid;\n"
"	background-color:rgb(207,207,207);\n"
"}\n"
"QProgressBar::chunk {\n"
"	background-color: qlineargradient(s"
                        "pread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(49, 147, 250, 255), stop:1 rgba(34, 142, 255, 255));\n"
"	border-radius: 10px;\n"
"}\n"
"QMenuBar {\n"
"	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(207, 209, 207, 255), stop:1 rgba(230, 229, 230, 255));\n"
"}\n"
"QMenuBar::item {\n"
"	color: #000000;\n"
"  	spacing: 3px;\n"
"  	padding: 1px 4px;\n"
"	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(207, 209, 207, 255), stop:1 rgba(230, 229, 230, 255));\n"
"}\n"
"\n"
"QMenuBar::item:selected {\n"
"  	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"	color: #FFFFFF;\n"
"}\n"
"QMenu::item:selected {\n"
"	border-style: solid;\n"
"	border-top-color: transparent;\n"
"	border-right-color: transparent;\n"
"	border-left-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
""
                        "	border-bottom-color: transparent;\n"
"	border-left-width: 2px;\n"
"	color: #000000;\n"
"	padding-left:15px;\n"
"	padding-top:4px;\n"
"	padding-bottom:4px;\n"
"	padding-right:7px;\n"
"}\n"
"QMenu::item {\n"
"	border-style: solid;\n"
"	border-top-color: transparent;\n"
"	border-right-color: transparent;\n"
"	border-left-color: transparent;\n"
"	border-bottom-color: transparent;\n"
"	border-bottom-width: 1px;\n"
"	color: #000000;\n"
"	padding-left:17px;\n"
"	padding-top:4px;\n"
"	padding-bottom:4px;\n"
"	padding-right:7px;\n"
"}\n"
"QTabWidget {\n"
"	color:rgb(0,0,0);\n"
"	background-color:#000000;\n"
"}\n"
"QTabWidget::pane {\n"
"		border-color: rgb(223,223,223);\n"
"		background-color:rgb(226,226,226);\n"
"		border-style: solid;\n"
"		border-width: 2px;\n"
"    	border-radius: 6px;\n"
"}\n"
"QTabBar::tab:first {\n"
"	border-style: solid;\n"
"	border-left-width:1px;\n"
"	border-right-width:0px;\n"
"	border-top-width:1px;\n"
"	border-bottom-width:1px;\n"
"	border-top-color: rgb(209,209,209);\n"
"	border-left-col"
                        "or: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(209, 209, 209, 209), stop:1 rgba(229, 229, 229, 229));\n"
"	border-bottom-color: rgb(229,229,229);\n"
"	border-top-left-radius: 4px;\n"
"	border-bottom-left-radius: 4px;\n"
"	color: #000000;\n"
"	padding: 3px;\n"
"	margin-left:0px;\n"
"	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(247, 247, 247, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QTabBar::tab:last {\n"
"	border-style: solid;\n"
"	border-width:1px;\n"
"	border-top-color: rgb(209,209,209);\n"
"	border-left-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(209, 209, 209, 209), stop:1 rgba(229, 229, 229, 229));\n"
"	border-right-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(209, 209, 209, 209), stop:1 rgba(229, 229, 229, 229));\n"
"	border-bottom-color: rgb(229,229,229);\n"
"	border-top-right-radius: 4px;\n"
"	border-bottom-right-radius: 4px;\n"
"	color: #000000;\n"
"	padding: 3px;\n"
""
                        "	margin-left:0px;\n"
"	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(247, 247, 247, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QTabBar::tab {\n"
"	border-style: solid;\n"
"	border-top-width:1px;\n"
"	border-bottom-width:1px;\n"
"	border-left-width:1px;\n"
"	border-top-color: rgb(209,209,209);\n"
"	border-left-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(209, 209, 209, 209), stop:1 rgba(229, 229, 229, 229));\n"
"	border-bottom-color: rgb(229,229,229);\n"
"	color: #000000;\n"
"	padding: 3px;\n"
"	margin-left:0px;\n"
"	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(247, 247, 247, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QTabBar::tab:selected, QTabBar::tab:last:selected, QTabBar::tab:hover {\n"
"  	border-style: solid;\n"
"  	border-left-width:1px;\n"
"	border-right-color: transparent;\n"
"	border-top-color: rgb(209,209,209);\n"
"	border-left-color: qlineargradient(spread:pad, x1:0.5, y1:1, "
                        "x2:0.5, y2:0, stop:0 rgba(209, 209, 209, 209), stop:1 rgba(229, 229, 229, 229));\n"
"	border-bottom-color: rgb(229,229,229);\n"
"	color: #FFFFFF;\n"
"	padding: 3px;\n"
"	margin-left:0px;\n"
"	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"\n"
"QTabBar::tab:selected, QTabBar::tab:first:selected, QTabBar::tab:hover {\n"
"  	border-style: solid;\n"
"  	border-left-width:1px;\n"
"  	border-bottom-width:1px;\n"
"  	border-top-width:1px;\n"
"	border-right-color: transparent;\n"
"	border-top-color: rgb(209,209,209);\n"
"	border-left-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(209, 209, 209, 209), stop:1 rgba(229, 229, 229, 229));\n"
"	border-bottom-color: rgb(229,229,229);\n"
"	color: #FFFFFF;\n"
"	padding: 3px;\n"
"	margin-left:0px;\n"
"	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"\n"
""
                        "QCheckBox {\n"
"	color: #000000;\n"
"	padding: 2px;\n"
"}\n"
"QCheckBox:disabled {\n"
"	color: #808086;\n"
"	padding: 2px;\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"	border-radius:4px;\n"
"	border-style:solid;\n"
"	padding-left: 1px;\n"
"	padding-right: 1px;\n"
"	padding-bottom: 1px;\n"
"	padding-top: 1px;\n"
"	border-width:1px;\n"
"	border-color: transparent;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"\n"
"	height: 10px;\n"
"	width: 10px;\n"
"	border-style:solid;\n"
"	border-width: 1px;\n"
"	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"	color: #000000;\n"
"	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"\n"
"	height: 10px;\n"
"	width: 10px;\n"
"	border-style:solid;\n"
"	border-width: 1px;\n"
"	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255"
                        ", 255), stop:1 rgba(91, 171, 252, 255));\n"
"	color: #000000;\n"
"}\n"
"QRadioButton {\n"
"	color: 000000;\n"
"	padding: 1px;\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"	height: 10px;\n"
"	width: 10px;\n"
"	border-style:solid;\n"
"	border-radius:5px;\n"
"	border-width: 1px;\n"
"	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"	color: #a9b7c6;\n"
"	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"QRadioButton::indicator:!checked {\n"
"	height: 10px;\n"
"	width: 10px;\n"
"	border-style:solid;\n"
"	border-radius:5px;\n"
"	border-width: 1px;\n"
"	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"	color: #a9b7c6;\n"
"	background-color: transparent;\n"
"}\n"
"QStatusBar {\n"
"	color:#027f7f;\n"
"}\n"
"QSpinBox {\n"
"	border-style: solid;\n"
""
                        "	border-width: 1px;\n"
"	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"QDoubleSpinBox {\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"QTimeEdit {\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"QDateTimeEdit {\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"QDateEdit {\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"\n"
""
                        "QToolBox {\n"
"	color: #a9b7c6;\n"
"	background-color:#000000;\n"
"}\n"
"QToolBox::tab {\n"
"	color: #a9b7c6;\n"
"	background-color:#000000;\n"
"}\n"
"QToolBox::tab:selected {\n"
"	color: #FFFFFF;\n"
"	background-color:#000000;\n"
"}\n"
"QScrollArea {\n"
"	color: #FFFFFF;\n"
"	background-color:#000000;\n"
"}\n"
"QSlider::groove:horizontal {\n"
"	height: 5px;\n"
"	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(49, 147, 250, 255), stop:1 rgba(34, 142, 255, 255));\n"
"}\n"
"QSlider::groove:vertical {\n"
"	width: 5px;\n"
"	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(49, 147, 250, 255), stop:1 rgba(34, 142, 255, 255));\n"
"}\n"
"QSlider::handle:horizontal {\n"
"	background: rgb(253,253,253);\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: rgb(207,207,207);\n"
"	width: 12px;\n"
"	margin: -5px 0;\n"
"	border-radius: 7px;\n"
"}\n"
"QSlider::handle:vertical {\n"
"	background: rgb(253,253,253);\n"
"	border-style: solid;"
                        "\n"
"	border-width: 1px;\n"
"	border-color: rgb(207,207,207);\n"
"	height: 12px;\n"
"	margin: 0 -5px;\n"
"	border-radius: 7px;\n"
"}\n"
"QSlider::add-page:horizontal {\n"
"    background: rgb(181,181,181);\n"
"}\n"
"QSlider::add-page:vertical {\n"
"    background: rgb(181,181,181);\n"
"}\n"
"QSlider::sub-page:horizontal {\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(49, 147, 250, 255), stop:1 rgba(34, 142, 255, 255));\n"
"}\n"
"QSlider::sub-page:vertical {\n"
"    background-color: qlineargradient(spread:pad, y1:0.5, x1:1, y2:0.5, x2:0, stop:0 rgba(49, 147, 250, 255), stop:1 rgba(34, 142, 255, 255));\n"
"}\n"
"QScrollBar:horizontal {\n"
"	max-height: 20px;\n"
"	border: 1px transparent grey;\n"
"	margin: 0px 20px 0px 20px;\n"
"}\n"
"QScrollBar:vertical {\n"
"	max-width: 20px;\n"
"	border: 1px transparent grey;\n"
"	margin: 20px 0px 20px 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"	background: rgb(253,253,253);\n"
"	border-style: solid;\n"
"	border-width: 1"
                        "px;\n"
"	border-color: rgb(207,207,207);\n"
"	border-radius: 7px;\n"
"	min-width: 25px;\n"
"}\n"
"QScrollBar::handle:horizontal:hover {\n"
"	background: rgb(253,253,253);\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: rgb(147, 200, 200);\n"
"	border-radius: 7px;\n"
"	min-width: 25px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"	background: rgb(253,253,253);\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: rgb(207,207,207);\n"
"	border-radius: 7px;\n"
"	min-height: 25px;\n"
"}\n"
"QScrollBar::handle:vertical:hover {\n"
"	background: rgb(253,253,253);\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: rgb(147, 200, 200);\n"
"	border-radius: 7px;\n"
"	min-height: 25px;\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"   border: 2px transparent grey;\n"
"   border-top-right-radius: 7px;\n"
"   border-bottom-right-radius: 7px;\n"
"   background: rgba(34, 142, 255, 255);\n"
"   width: 20px;\n"
"   subcontrol-position: right;\n"
"   subcontrol-origin: margin;"
                        "\n"
"}\n"
"QScrollBar::add-line:horizontal:pressed {\n"
"   border: 2px transparent grey;\n"
"   border-top-right-radius: 7px;\n"
"   border-bottom-right-radius: 7px;\n"
"   background: rgb(181,181,181);\n"
"   width: 20px;\n"
"   subcontrol-position: right;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"   border: 2px transparent grey;\n"
"   border-bottom-left-radius: 7px;\n"
"   border-bottom-right-radius: 7px;\n"
"   background: rgba(34, 142, 255, 255);\n"
"   height: 20px;\n"
"   subcontrol-position: bottom;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical:pressed {\n"
"   border: 2px transparent grey;\n"
"   border-bottom-left-radius: 7px;\n"
"   border-bottom-right-radius: 7px;\n"
"   background: rgb(181,181,181);\n"
"   height: 20px;\n"
"   subcontrol-position: bottom;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"   border: 2px transparent grey;\n"
"   border-top-left-radius: 7px;\n"
"   border-bottom-left-ra"
                        "dius: 7px;\n"
"   background: rgba(34, 142, 255, 255);\n"
"   width: 20px;\n"
"   subcontrol-position: left;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal:pressed {\n"
"   border: 2px transparent grey;\n"
"   border-top-left-radius: 7px;\n"
"   border-bottom-left-radius: 7px;\n"
"   background: rgb(181,181,181);\n"
"   width: 20px;\n"
"   subcontrol-position: left;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"   border: 2px transparent grey;\n"
"   border-top-left-radius: 7px;\n"
"   border-top-right-radius: 7px;\n"
"   background: rgba(34, 142, 255, 255);\n"
"   height: 20px;\n"
"   subcontrol-position: top;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed {\n"
"   border: 2px transparent grey;\n"
"   border-top-left-radius: 7px;\n"
"   border-top-right-radius: 7px;\n"
"   background: rgb(181,181,181);\n"
"   height: 20px;\n"
"   subcontrol-position: top;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::le"
                        "ft-arrow:horizontal {\n"
"   border: 1px transparent grey;\n"
"   border-top-left-radius: 3px;\n"
"   border-bottom-left-radius: 3px;\n"
"   width: 6px;\n"
"   height: 6px;\n"
"   background: white;\n"
"}\n"
"QScrollBar::right-arrow:horizontal {\n"
"   border: 1px transparent grey;\n"
"   border-top-right-radius: 3px;\n"
"   border-bottom-right-radius: 3px;\n"
"   width: 6px;\n"
"   height: 6px;\n"
"   background: white;\n"
"}\n"
"QScrollBar::up-arrow:vertical {\n"
"   border: 1px transparent grey;\n"
"   border-top-left-radius: 3px;\n"
"   border-top-right-radius: 3px;\n"
"   width: 6px;\n"
"   height: 6px;\n"
"   background: white;\n"
"}\n"
"QScrollBar::down-arrow:vertical {\n"
"   border: 1px transparent grey;\n"
"   border-bottom-left-radius: 3px;\n"
"   border-bottom-right-radius: 3px;\n"
"   width: 6px;\n"
"   height: 6px;\n"
"   background: white;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"   background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub"
                        "-page:vertical {\n"
"   background: none;\n"
"}\n"
"")
        self.RM_TvDB = QTableView(self.page_uno)
        self.RM_TvDB.setObjectName(u"RM_TvDB")
        self.RM_TvDB.setGeometry(QRect(20, 710, 1221, 192))
        self.stackedWidget.addWidget(self.page_uno)
        self.page_dos = QWidget()
        self.page_dos.setObjectName(u"page_dos")
        self.gridLayoutWidget_3 = QWidget(self.page_dos)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(10, 10, 491, 151))
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.density = QDoubleSpinBox(self.gridLayoutWidget_3)
        self.density.setObjectName(u"density")

        self.gridLayout_3.addWidget(self.density, 0, 1, 1, 1)

        self.label_9 = QLabel(self.gridLayoutWidget_3)
        self.label_9.setObjectName(u"label_9")
        font = QFont()
        self.label_9.setFont(font)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_9, 4, 0, 1, 1)

        self.label_10 = QLabel(self.gridLayoutWidget_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_10, 0, 0, 1, 1)

        self.qFluid = QSpinBox(self.gridLayoutWidget_3)
        self.qFluid.setObjectName(u"qFluid")
        self.qFluid.setMaximum(2000)
        self.qFluid.setSingleStep(5)
        self.qFluid.setValue(500)

        self.gridLayout_3.addWidget(self.qFluid, 4, 1, 1, 1)

        self.label_11 = QLabel(self.gridLayoutWidget_3)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_11, 2, 0, 1, 1)

        self.Ty = QDoubleSpinBox(self.gridLayoutWidget_3)
        self.Ty.setObjectName(u"Ty")

        self.gridLayout_3.addWidget(self.Ty, 2, 1, 1, 1)

        self.label_12 = QLabel(self.gridLayoutWidget_3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_12, 3, 0, 1, 1)

        self.mp = QDoubleSpinBox(self.gridLayoutWidget_3)
        self.mp.setObjectName(u"mp")

        self.gridLayout_3.addWidget(self.mp, 3, 1, 1, 1)

        self.verticalLayoutWidget_3 = QWidget(self.page_dos)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(10, 230, 691, 361))
        self.verticalLayout_6 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.Density_Table = QTableWidget(self.verticalLayoutWidget_3)
        if (self.Density_Table.columnCount() < 4):
            self.Density_Table.setColumnCount(4)
        __qtablewidgetitem34 = QTableWidgetItem()
        __qtablewidgetitem34.setTextAlignment(Qt.AlignCenter);
        self.Density_Table.setHorizontalHeaderItem(0, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        __qtablewidgetitem35.setTextAlignment(Qt.AlignCenter);
        self.Density_Table.setHorizontalHeaderItem(1, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        __qtablewidgetitem36.setTextAlignment(Qt.AlignCenter);
        self.Density_Table.setHorizontalHeaderItem(2, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        __qtablewidgetitem37.setTextAlignment(Qt.AlignCenter);
        self.Density_Table.setHorizontalHeaderItem(3, __qtablewidgetitem37)
        if (self.Density_Table.rowCount() < 7):
            self.Density_Table.setRowCount(7)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.Density_Table.setVerticalHeaderItem(0, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.Density_Table.setVerticalHeaderItem(1, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.Density_Table.setVerticalHeaderItem(2, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.Density_Table.setVerticalHeaderItem(3, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.Density_Table.setVerticalHeaderItem(4, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.Density_Table.setVerticalHeaderItem(5, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.Density_Table.setVerticalHeaderItem(6, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        __qtablewidgetitem45.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem45.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.Density_Table.setItem(0, 0, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        __qtablewidgetitem46.setTextAlignment(Qt.AlignCenter);
        self.Density_Table.setItem(0, 1, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        __qtablewidgetitem47.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem47.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.Density_Table.setItem(0, 2, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        __qtablewidgetitem48.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem48.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.Density_Table.setItem(0, 3, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        __qtablewidgetitem49.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem49.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.Density_Table.setItem(1, 0, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        __qtablewidgetitem50.setTextAlignment(Qt.AlignCenter);
        self.Density_Table.setItem(1, 1, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        __qtablewidgetitem51.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem51.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.Density_Table.setItem(1, 2, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        __qtablewidgetitem52.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem52.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.Density_Table.setItem(1, 3, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        __qtablewidgetitem53.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem53.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.Density_Table.setItem(2, 0, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        __qtablewidgetitem54.setTextAlignment(Qt.AlignCenter);
        self.Density_Table.setItem(2, 1, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        __qtablewidgetitem55.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem55.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.Density_Table.setItem(2, 2, __qtablewidgetitem55)
        __qtablewidgetitem56 = QTableWidgetItem()
        __qtablewidgetitem56.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem56.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.Density_Table.setItem(2, 3, __qtablewidgetitem56)
        __qtablewidgetitem57 = QTableWidgetItem()
        __qtablewidgetitem57.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem57.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.Density_Table.setItem(3, 0, __qtablewidgetitem57)
        __qtablewidgetitem58 = QTableWidgetItem()
        __qtablewidgetitem58.setTextAlignment(Qt.AlignCenter);
        self.Density_Table.setItem(3, 1, __qtablewidgetitem58)
        __qtablewidgetitem59 = QTableWidgetItem()
        __qtablewidgetitem59.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem59.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.Density_Table.setItem(3, 2, __qtablewidgetitem59)
        __qtablewidgetitem60 = QTableWidgetItem()
        __qtablewidgetitem60.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem60.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.Density_Table.setItem(3, 3, __qtablewidgetitem60)
        __qtablewidgetitem61 = QTableWidgetItem()
        __qtablewidgetitem61.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem61.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.Density_Table.setItem(4, 0, __qtablewidgetitem61)
        __qtablewidgetitem62 = QTableWidgetItem()
        __qtablewidgetitem62.setTextAlignment(Qt.AlignCenter);
        self.Density_Table.setItem(4, 1, __qtablewidgetitem62)
        __qtablewidgetitem63 = QTableWidgetItem()
        __qtablewidgetitem63.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem63.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.Density_Table.setItem(4, 2, __qtablewidgetitem63)
        __qtablewidgetitem64 = QTableWidgetItem()
        __qtablewidgetitem64.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem64.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.Density_Table.setItem(4, 3, __qtablewidgetitem64)
        __qtablewidgetitem65 = QTableWidgetItem()
        __qtablewidgetitem65.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem65.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.Density_Table.setItem(5, 0, __qtablewidgetitem65)
        __qtablewidgetitem66 = QTableWidgetItem()
        __qtablewidgetitem66.setTextAlignment(Qt.AlignCenter);
        self.Density_Table.setItem(5, 1, __qtablewidgetitem66)
        __qtablewidgetitem67 = QTableWidgetItem()
        __qtablewidgetitem67.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem67.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.Density_Table.setItem(5, 2, __qtablewidgetitem67)
        __qtablewidgetitem68 = QTableWidgetItem()
        __qtablewidgetitem68.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem68.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.Density_Table.setItem(5, 3, __qtablewidgetitem68)
        __qtablewidgetitem69 = QTableWidgetItem()
        __qtablewidgetitem69.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem69.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.Density_Table.setItem(6, 0, __qtablewidgetitem69)
        __qtablewidgetitem70 = QTableWidgetItem()
        __qtablewidgetitem70.setTextAlignment(Qt.AlignCenter);
        self.Density_Table.setItem(6, 1, __qtablewidgetitem70)
        __qtablewidgetitem71 = QTableWidgetItem()
        __qtablewidgetitem71.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem71.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.Density_Table.setItem(6, 2, __qtablewidgetitem71)
        __qtablewidgetitem72 = QTableWidgetItem()
        __qtablewidgetitem72.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem72.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.Density_Table.setItem(6, 3, __qtablewidgetitem72)
        self.Density_Table.setObjectName(u"Density_Table")

        self.verticalLayout_6.addWidget(self.Density_Table)

        self.Nhe = QPushButton(self.page_dos)
        self.Nhe.setObjectName(u"Nhe")
        self.Nhe.setGeometry(QRect(10, 610, 112, 35))
        self.NCRe = QPushButton(self.page_dos)
        self.NCRe.setObjectName(u"NCRe")
        self.NCRe.setGeometry(QRect(140, 610, 112, 35))
        self.DP = QPushButton(self.page_dos)
        self.DP.setObjectName(u"DP")
        self.DP.setGeometry(QRect(260, 610, 112, 35))
        self.Dp_Clean = QPushButton(self.page_dos)
        self.Dp_Clean.setObjectName(u"Dp_Clean")
        self.Dp_Clean.setGeometry(QRect(390, 610, 112, 35))
        self.gridLayoutWidget_4 = QWidget(self.page_dos)
        self.gridLayoutWidget_4.setObjectName(u"gridLayoutWidget_4")
        self.gridLayoutWidget_4.setGeometry(QRect(10, 660, 691, 211))
        self.gridLayout_4 = QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.Dp_Superficial = QDoubleSpinBox(self.gridLayoutWidget_4)
        self.Dp_Superficial.setObjectName(u"Dp_Superficial")
        self.Dp_Superficial.setEnabled(False)
        self.Dp_Superficial.setMaximum(100000000000000.000000000000000)

        self.gridLayout_4.addWidget(self.Dp_Superficial, 0, 1, 1, 1)

        self.label_13 = QLabel(self.gridLayoutWidget_4)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_13, 2, 0, 1, 1)

        self.Dp_Total = QDoubleSpinBox(self.gridLayoutWidget_4)
        self.Dp_Total.setObjectName(u"Dp_Total")
        self.Dp_Total.setEnabled(False)
        self.Dp_Total.setMaximum(100000000000000.000000000000000)

        self.gridLayout_4.addWidget(self.Dp_Total, 2, 1, 1, 1)

        self.DEC = QDoubleSpinBox(self.gridLayoutWidget_4)
        self.DEC.setObjectName(u"DEC")
        self.DEC.setEnabled(False)
        self.DEC.setMaximum(100000000000000.000000000000000)

        self.gridLayout_4.addWidget(self.DEC, 3, 1, 1, 1)

        self.label_14 = QLabel(self.gridLayoutWidget_4)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_14, 0, 0, 1, 1)

        self.label_15 = QLabel(self.gridLayoutWidget_4)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_15, 3, 0, 1, 1)

        self.label_16 = QLabel(self.gridLayoutWidget_4)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_16, 1, 0, 1, 1)

        self.Dp_Barrena = QDoubleSpinBox(self.gridLayoutWidget_4)
        self.Dp_Barrena.setObjectName(u"Dp_Barrena")
        self.Dp_Barrena.setEnabled(False)
        self.Dp_Barrena.setMaximum(100000000000000.000000000000000)

        self.gridLayout_4.addWidget(self.Dp_Barrena, 1, 1, 1, 1)

        self.label_17 = QLabel(self.page_dos)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(930, 20, 211, 24))
        self.label_17.setFont(font)
        self.label_17.setAlignment(Qt.AlignCenter)
        self.label_18 = QLabel(self.page_dos)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(820, 40, 371, 441))
        self.label_18.setPixmap(QPixmap(u"../../../../../../Pictures/Saved Pictures/WhatsApp Image 2022-01-01 at 2.52.27 PM (2).jpeg"))
        self.label_19 = QLabel(self.page_dos)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(750, 510, 471, 301))
        self.label_19.setPixmap(QPixmap(u"../../../../../../Pictures/Saved Pictures/WhatsApp Image 2022-01-01 at 2.52.27 PM (3).jpeg"))
        self.label_20 = QLabel(self.page_dos)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(20, 170, 621, 51))
        font1 = QFont()
        font1.setPointSize(8)
        self.label_20.setFont(font1)
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
        self.RM_Rep.setText(QCoreApplication.translate("MainWindow", u"Reporte", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Temperatura", None))
        ___qtablewidgetitem14 = self.RM_TableWidgetDB.horizontalHeaderItem(0)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"RPM", None));
        ___qtablewidgetitem15 = self.RM_TableWidgetDB.horizontalHeaderItem(1)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"\u03a6", None));
        ___qtablewidgetitem16 = self.RM_TableWidgetDB.verticalHeaderItem(0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem17 = self.RM_TableWidgetDB.verticalHeaderItem(1)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem18 = self.RM_TableWidgetDB.verticalHeaderItem(2)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem19 = self.RM_TableWidgetDB.verticalHeaderItem(3)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem20 = self.RM_TableWidgetDB.verticalHeaderItem(4)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem21 = self.RM_TableWidgetDB.verticalHeaderItem(5)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"6", None));

        __sortingEnabled1 = self.RM_TableWidgetDB.isSortingEnabled()
        self.RM_TableWidgetDB.setSortingEnabled(False)
        ___qtablewidgetitem22 = self.RM_TableWidgetDB.item(0, 0)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem23 = self.RM_TableWidgetDB.item(0, 1)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem24 = self.RM_TableWidgetDB.item(1, 0)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem25 = self.RM_TableWidgetDB.item(1, 1)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem26 = self.RM_TableWidgetDB.item(2, 0)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"100", None));
        ___qtablewidgetitem27 = self.RM_TableWidgetDB.item(2, 1)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem28 = self.RM_TableWidgetDB.item(3, 0)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"200", None));
        ___qtablewidgetitem29 = self.RM_TableWidgetDB.item(3, 1)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem30 = self.RM_TableWidgetDB.item(4, 0)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"300", None));
        ___qtablewidgetitem31 = self.RM_TableWidgetDB.item(4, 1)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem32 = self.RM_TableWidgetDB.item(5, 0)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"600", None));
        ___qtablewidgetitem33 = self.RM_TableWidgetDB.item(5, 1)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"0", None));
        self.RM_TableWidgetDB.setSortingEnabled(__sortingEnabled1)

        self.RM_GraphDB.setText(QCoreApplication.translate("MainWindow", u"Gr\u00e0fico", None))
        self.RM_DeleteDB.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
        self.RM_UpdateDB.setText(QCoreApplication.translate("MainWindow", u"Actualizar BD", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Viscosidad Aparente", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Punto de Cedencia", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Viscosidad Pl\u00e0stica", None))
        self.RM_VaDB.setSuffix(QCoreApplication.translate("MainWindow", u" cp", None))
        self.RM_VaDB.setPrefix("")
        self.RM_VpDB.setSuffix(QCoreApplication.translate("MainWindow", u" cp", None))
        self.density.setSuffix(QCoreApplication.translate("MainWindow", u" [gr/cm3]", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Q", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"pf", None))
        self.qFluid.setSuffix(QCoreApplication.translate("MainWindow", u" [rpm]", None))
        self.qFluid.setPrefix("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Ty", None))
        self.Ty.setSuffix(QCoreApplication.translate("MainWindow", u" [lb/100ft2]", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"mp", None))
        self.mp.setSuffix(QCoreApplication.translate("MainWindow", u" [cp]", None))
        ___qtablewidgetitem34 = self.Density_Table.horizontalHeaderItem(0)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"NHe", None));
        ___qtablewidgetitem35 = self.Density_Table.horizontalHeaderItem(1)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"NCRe", None));
        ___qtablewidgetitem36 = self.Density_Table.horizontalHeaderItem(2)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"Flujo", None));
        ___qtablewidgetitem37 = self.Density_Table.horizontalHeaderItem(3)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"\u2206P", None));
        ___qtablewidgetitem38 = self.Density_Table.verticalHeaderItem(0)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"Tp", None));
        ___qtablewidgetitem39 = self.Density_Table.verticalHeaderItem(1)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"Hw", None));
        ___qtablewidgetitem40 = self.Density_Table.verticalHeaderItem(2)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"Dc", None));
        ___qtablewidgetitem41 = self.Density_Table.verticalHeaderItem(3)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"AG_DC", None));
        ___qtablewidgetitem42 = self.Density_Table.verticalHeaderItem(4)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"AG_HW", None));
        ___qtablewidgetitem43 = self.Density_Table.verticalHeaderItem(5)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"AG_TP", None));
        ___qtablewidgetitem44 = self.Density_Table.verticalHeaderItem(6)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"TR_TP", None));

        __sortingEnabled2 = self.Density_Table.isSortingEnabled()
        self.Density_Table.setSortingEnabled(False)
        ___qtablewidgetitem45 = self.Density_Table.item(0, 0)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem46 = self.Density_Table.item(0, 1)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem47 = self.Density_Table.item(0, 2)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainWindow", u"-", None));
        ___qtablewidgetitem48 = self.Density_Table.item(0, 3)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem49 = self.Density_Table.item(1, 0)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem50 = self.Density_Table.item(1, 1)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem51 = self.Density_Table.item(1, 2)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("MainWindow", u"-", None));
        ___qtablewidgetitem52 = self.Density_Table.item(1, 3)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem53 = self.Density_Table.item(2, 0)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem54 = self.Density_Table.item(2, 1)
        ___qtablewidgetitem54.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem55 = self.Density_Table.item(2, 2)
        ___qtablewidgetitem55.setText(QCoreApplication.translate("MainWindow", u"-", None));
        ___qtablewidgetitem56 = self.Density_Table.item(2, 3)
        ___qtablewidgetitem56.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem57 = self.Density_Table.item(3, 0)
        ___qtablewidgetitem57.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem58 = self.Density_Table.item(3, 1)
        ___qtablewidgetitem58.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem59 = self.Density_Table.item(3, 2)
        ___qtablewidgetitem59.setText(QCoreApplication.translate("MainWindow", u"-", None));
        ___qtablewidgetitem60 = self.Density_Table.item(3, 3)
        ___qtablewidgetitem60.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem61 = self.Density_Table.item(4, 0)
        ___qtablewidgetitem61.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem62 = self.Density_Table.item(4, 1)
        ___qtablewidgetitem62.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem63 = self.Density_Table.item(4, 2)
        ___qtablewidgetitem63.setText(QCoreApplication.translate("MainWindow", u"-", None));
        ___qtablewidgetitem64 = self.Density_Table.item(4, 3)
        ___qtablewidgetitem64.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem65 = self.Density_Table.item(5, 0)
        ___qtablewidgetitem65.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem66 = self.Density_Table.item(5, 1)
        ___qtablewidgetitem66.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem67 = self.Density_Table.item(5, 2)
        ___qtablewidgetitem67.setText(QCoreApplication.translate("MainWindow", u"-", None));
        ___qtablewidgetitem68 = self.Density_Table.item(5, 3)
        ___qtablewidgetitem68.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem69 = self.Density_Table.item(6, 0)
        ___qtablewidgetitem69.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem70 = self.Density_Table.item(6, 1)
        ___qtablewidgetitem70.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem71 = self.Density_Table.item(6, 2)
        ___qtablewidgetitem71.setText(QCoreApplication.translate("MainWindow", u"-", None));
        ___qtablewidgetitem72 = self.Density_Table.item(6, 3)
        ___qtablewidgetitem72.setText(QCoreApplication.translate("MainWindow", u"0", None));
        self.Density_Table.setSortingEnabled(__sortingEnabled2)

        self.Nhe.setText(QCoreApplication.translate("MainWindow", u"Nhe", None))
        self.NCRe.setText(QCoreApplication.translate("MainWindow", u"NCRe", None))
        self.DP.setText(QCoreApplication.translate("MainWindow", u"\u2206P", None))
        self.Dp_Clean.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.Dp_Superficial.setSuffix(QCoreApplication.translate("MainWindow", u" [psi]", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u2206Ptotal", None))
        self.Dp_Total.setPrefix("")
        self.Dp_Total.setSuffix(QCoreApplication.translate("MainWindow", u" [psi]", None))
        self.DEC.setSuffix(QCoreApplication.translate("MainWindow", u" [gr/cm3]", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u2206Psuperficial ", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Desntidad Equivalente de Circulaci\u00f3n", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u2206Pbarrena", None))
        self.Dp_Barrena.setSuffix(QCoreApplication.translate("MainWindow", u" [psi]", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Estado Mec\u00e1nico", None))
        self.label_18.setText("")
        self.label_19.setText("")
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Se considera un valor de E constante = 0.000053 [ADIM] de acuerdo al equipo superficial", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"5", None))
    # retranslateUi

