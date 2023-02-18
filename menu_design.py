# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menuRQXwjw.ui'
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
        MainWindow.resize(1303, 947)
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

        self.bt_3 = QPushButton(self.frame_lateral)
        self.bt_3.setObjectName(u"bt_3")
        self.bt_3.setMinimumSize(QSize(0, 40))

        self.verticalLayout_3.addWidget(self.bt_3)

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
        self.scrollArea = QScrollArea(self.page_tres)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(0, 0, 1331, 911))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1329, 909))
        self.label_21 = QLabel(self.scrollAreaWidgetContents)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(40, 0, 601, 31))
        font2 = QFont()
        font2.setPointSize(15)
        self.label_21.setFont(font2)
        self.gridLayoutWidget_5 = QWidget(self.scrollAreaWidgetContents)
        self.gridLayoutWidget_5.setObjectName(u"gridLayoutWidget_5")
        self.gridLayoutWidget_5.setGeometry(QRect(30, 40, 401, 807))
        self.gridLayout_5 = QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.casing_length = QDoubleSpinBox(self.gridLayoutWidget_5)
        self.casing_length.setObjectName(u"casing_length")
        self.casing_length.setMaximum(100000.000000000000000)
        self.casing_length.setValue(11500.000000000000000)

        self.gridLayout_5.addWidget(self.casing_length, 8, 2, 1, 1)

        self.label_33 = QLabel(self.gridLayoutWidget_5)
        self.label_33.setObjectName(u"label_33")

        self.gridLayout_5.addWidget(self.label_33, 11, 0, 1, 1)

        self.label_29 = QLabel(self.gridLayoutWidget_5)
        self.label_29.setObjectName(u"label_29")

        self.gridLayout_5.addWidget(self.label_29, 7, 0, 1, 1)

        self.drill_pipe_size = QDoubleSpinBox(self.gridLayoutWidget_5)
        self.drill_pipe_size.setObjectName(u"drill_pipe_size")
        self.drill_pipe_size.setValue(4.280000000000000)

        self.gridLayout_5.addWidget(self.drill_pipe_size, 9, 2, 1, 1)

        self.label_23 = QLabel(self.gridLayoutWidget_5)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout_5.addWidget(self.label_23, 1, 0, 1, 1)

        self.label_42 = QLabel(self.gridLayoutWidget_5)
        self.label_42.setObjectName(u"label_42")

        self.gridLayout_5.addWidget(self.label_42, 20, 0, 1, 1)

        self.density_of_particle = QDoubleSpinBox(self.gridLayoutWidget_5)
        self.density_of_particle.setObjectName(u"density_of_particle")
        self.density_of_particle.setValue(22.000000000000000)

        self.gridLayout_5.addWidget(self.density_of_particle, 16, 2, 1, 1)

        self.yield_point = QDoubleSpinBox(self.gridLayoutWidget_5)
        self.yield_point.setObjectName(u"yield_point")
        self.yield_point.setValue(14.000000000000000)

        self.gridLayout_5.addWidget(self.yield_point, 3, 2, 1, 1)

        self.label_27 = QLabel(self.gridLayoutWidget_5)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout_5.addWidget(self.label_27, 5, 0, 1, 1)

        self.plastic_viscosity = QDoubleSpinBox(self.gridLayoutWidget_5)
        self.plastic_viscosity.setObjectName(u"plastic_viscosity")
        self.plastic_viscosity.setValue(26.000000000000000)

        self.gridLayout_5.addWidget(self.plastic_viscosity, 2, 2, 1, 1)

        self.label_31 = QLabel(self.gridLayoutWidget_5)
        self.label_31.setObjectName(u"label_31")

        self.gridLayout_5.addWidget(self.label_31, 9, 0, 1, 1)

        self.label_34 = QLabel(self.gridLayoutWidget_5)
        self.label_34.setObjectName(u"label_34")

        self.gridLayout_5.addWidget(self.label_34, 12, 0, 1, 1)

        self.label_35 = QLabel(self.gridLayoutWidget_5)
        self.label_35.setObjectName(u"label_35")

        self.gridLayout_5.addWidget(self.label_35, 13, 0, 1, 1)

        self.pump_pressure = QDoubleSpinBox(self.gridLayoutWidget_5)
        self.pump_pressure.setObjectName(u"pump_pressure")
        self.pump_pressure.setMaximum(10000.000000000000000)
        self.pump_pressure.setValue(2950.000000000000000)

        self.gridLayout_5.addWidget(self.pump_pressure, 13, 2, 1, 1)

        self.label_41 = QLabel(self.gridLayoutWidget_5)
        self.label_41.setObjectName(u"label_41")

        self.gridLayout_5.addWidget(self.label_41, 19, 0, 1, 1)

        self.l_600 = QDoubleSpinBox(self.gridLayoutWidget_5)
        self.l_600.setObjectName(u"l_600")
        self.l_600.setValue(66.000000000000000)

        self.gridLayout_5.addWidget(self.l_600, 21, 2, 1, 1)

        self.label_28 = QLabel(self.gridLayoutWidget_5)
        self.label_28.setObjectName(u"label_28")

        self.gridLayout_5.addWidget(self.label_28, 6, 0, 1, 1)

        self.drill_collar_size = QDoubleSpinBox(self.gridLayoutWidget_5)
        self.drill_collar_size.setObjectName(u"drill_collar_size")
        self.drill_collar_size.setValue(3.000000000000000)

        self.gridLayout_5.addWidget(self.drill_collar_size, 10, 2, 1, 1)

        self.rate_of_penetration = QDoubleSpinBox(self.gridLayoutWidget_5)
        self.rate_of_penetration.setObjectName(u"rate_of_penetration")
        self.rate_of_penetration.setValue(50.000000000000000)

        self.gridLayout_5.addWidget(self.rate_of_penetration, 15, 2, 1, 1)

        self.diameter_of_particle = QDoubleSpinBox(self.gridLayoutWidget_5)
        self.diameter_of_particle.setObjectName(u"diameter_of_particle")
        self.diameter_of_particle.setValue(0.250000000000000)

        self.gridLayout_5.addWidget(self.diameter_of_particle, 17, 2, 1, 1)

        self.label_37 = QLabel(self.gridLayoutWidget_5)
        self.label_37.setObjectName(u"label_37")

        self.gridLayout_5.addWidget(self.label_37, 15, 0, 1, 1)

        self.open_hole_length = QDoubleSpinBox(self.gridLayoutWidget_5)
        self.open_hole_length.setObjectName(u"open_hole_length")
        self.open_hole_length.setMaximum(10000.000000000000000)
        self.open_hole_length.setValue(3000.000000000000000)

        self.gridLayout_5.addWidget(self.open_hole_length, 6, 2, 1, 1)

        self.L_300 = QDoubleSpinBox(self.gridLayoutWidget_5)
        self.L_300.setObjectName(u"L_300")
        self.L_300.setValue(40.000000000000000)

        self.gridLayout_5.addWidget(self.L_300, 20, 2, 1, 1)

        self.label_26 = QLabel(self.gridLayoutWidget_5)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout_5.addWidget(self.label_26, 4, 0, 1, 1)

        self.pump_output = QDoubleSpinBox(self.gridLayoutWidget_5)
        self.pump_output.setObjectName(u"pump_output")
        self.pump_output.setMaximum(10000.000000000000000)
        self.pump_output.setValue(400.000000000000000)

        self.gridLayout_5.addWidget(self.pump_output, 12, 2, 1, 1)

        self.bit_size = QDoubleSpinBox(self.gridLayoutWidget_5)
        self.bit_size.setObjectName(u"bit_size")
        self.bit_size.setValue(9.880000000000001)

        self.gridLayout_5.addWidget(self.bit_size, 5, 2, 1, 1)

        self.label_32 = QLabel(self.gridLayoutWidget_5)
        self.label_32.setObjectName(u"label_32")

        self.gridLayout_5.addWidget(self.label_32, 10, 0, 1, 1)

        self.label_22 = QLabel(self.gridLayoutWidget_5)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_5.addWidget(self.label_22, 0, 0, 1, 1)

        self.label_40 = QLabel(self.gridLayoutWidget_5)
        self.label_40.setObjectName(u"label_40")

        self.gridLayout_5.addWidget(self.label_40, 18, 0, 1, 1)

        self.label_30 = QLabel(self.gridLayoutWidget_5)
        self.label_30.setObjectName(u"label_30")

        self.gridLayout_5.addWidget(self.label_30, 8, 0, 1, 1)

        self.label_43 = QLabel(self.gridLayoutWidget_5)
        self.label_43.setObjectName(u"label_43")

        self.gridLayout_5.addWidget(self.label_43, 21, 0, 1, 1)

        self.label_38 = QLabel(self.gridLayoutWidget_5)
        self.label_38.setObjectName(u"label_38")

        self.gridLayout_5.addWidget(self.label_38, 16, 0, 1, 1)

        self.label_39 = QLabel(self.gridLayoutWidget_5)
        self.label_39.setObjectName(u"label_39")

        self.gridLayout_5.addWidget(self.label_39, 17, 0, 1, 1)

        self.surface_case = QDoubleSpinBox(self.gridLayoutWidget_5)
        self.surface_case.setObjectName(u"surface_case")
        self.surface_case.setValue(0.150000000000000)

        self.gridLayout_5.addWidget(self.surface_case, 14, 2, 1, 1)

        self.gel_strength = QDoubleSpinBox(self.gridLayoutWidget_5)
        self.gel_strength.setObjectName(u"gel_strength")
        self.gel_strength.setValue(8.000000000000000)

        self.gridLayout_5.addWidget(self.gel_strength, 4, 2, 1, 1)

        self.label_36 = QLabel(self.gridLayoutWidget_5)
        self.label_36.setObjectName(u"label_36")

        self.gridLayout_5.addWidget(self.label_36, 14, 0, 1, 1)

        self.mud_weight = QDoubleSpinBox(self.gridLayoutWidget_5)
        self.mud_weight.setObjectName(u"mud_weight")
        self.mud_weight.setValue(12.000000000000000)

        self.gridLayout_5.addWidget(self.mud_weight, 0, 2, 1, 1)

        self.label_24 = QLabel(self.gridLayoutWidget_5)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout_5.addWidget(self.label_24, 2, 0, 1, 1)

        self.prof_total = QDoubleSpinBox(self.gridLayoutWidget_5)
        self.prof_total.setObjectName(u"prof_total")
        self.prof_total.setMaximum(100000.000000000000000)
        self.prof_total.setValue(15000.000000000000000)

        self.gridLayout_5.addWidget(self.prof_total, 19, 2, 1, 1)

        self.label_25 = QLabel(self.gridLayoutWidget_5)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout_5.addWidget(self.label_25, 3, 0, 1, 1)

        self.casing_size = QDoubleSpinBox(self.gridLayoutWidget_5)
        self.casing_size.setObjectName(u"casing_size")
        self.casing_size.setValue(9.949999999999999)

        self.gridLayout_5.addWidget(self.casing_size, 7, 2, 1, 1)

        self.drill_collar_length = QDoubleSpinBox(self.gridLayoutWidget_5)
        self.drill_collar_length.setObjectName(u"drill_collar_length")
        self.drill_collar_length.setMaximum(10000.000000000000000)
        self.drill_collar_length.setValue(650.000000000000000)

        self.gridLayout_5.addWidget(self.drill_collar_length, 11, 2, 1, 1)

        self.solid_sg = QDoubleSpinBox(self.gridLayoutWidget_5)
        self.solid_sg.setObjectName(u"solid_sg")
        self.solid_sg.setValue(3.820000000000000)

        self.gridLayout_5.addWidget(self.solid_sg, 1, 2, 1, 1)

        self.fracture_gradient = QDoubleSpinBox(self.gridLayoutWidget_5)
        self.fracture_gradient.setObjectName(u"fracture_gradient")
        self.fracture_gradient.setValue(14.000000000000000)

        self.gridLayout_5.addWidget(self.fracture_gradient, 18, 2, 1, 1)

        self.bit_size_alt = QDoubleSpinBox(self.gridLayoutWidget_5)
        self.bit_size_alt.setObjectName(u"bit_size_alt")
        self.bit_size_alt.setValue(12.000000000000000)

        self.gridLayout_5.addWidget(self.bit_size_alt, 5, 1, 1, 1)

        self.casing_size_alt = QDoubleSpinBox(self.gridLayoutWidget_5)
        self.casing_size_alt.setObjectName(u"casing_size_alt")
        self.casing_size_alt.setValue(10.750000000000000)

        self.gridLayout_5.addWidget(self.casing_size_alt, 7, 1, 1, 1)

        self.casing_length_alt = QDoubleSpinBox(self.gridLayoutWidget_5)
        self.casing_length_alt.setObjectName(u"casing_length_alt")
        self.casing_length_alt.setMaximum(50000.000000000000000)
        self.casing_length_alt.setValue(12000.000000000000000)

        self.gridLayout_5.addWidget(self.casing_length_alt, 8, 1, 1, 1)

        self.drill_pipe_size_alt = QDoubleSpinBox(self.gridLayoutWidget_5)
        self.drill_pipe_size_alt.setObjectName(u"drill_pipe_size_alt")
        self.drill_pipe_size_alt.setValue(5.000000000000000)

        self.gridLayout_5.addWidget(self.drill_pipe_size_alt, 9, 1, 1, 1)

        self.drill_collar_size_alt = QDoubleSpinBox(self.gridLayoutWidget_5)
        self.drill_collar_size_alt.setObjectName(u"drill_collar_size_alt")
        self.drill_collar_size_alt.setValue(8.000000000000000)

        self.gridLayout_5.addWidget(self.drill_collar_size_alt, 10, 1, 1, 1)

        self.gridLayoutWidget_6 = QWidget(self.scrollAreaWidgetContents)
        self.gridLayoutWidget_6.setObjectName(u"gridLayoutWidget_6")
        self.gridLayoutWidget_6.setGeometry(QRect(1090, 130, 160, 67))
        self.gridLayout_6 = QGridLayout(self.gridLayoutWidget_6)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_44 = QLabel(self.gridLayoutWidget_6)
        self.label_44.setObjectName(u"label_44")

        self.gridLayout_6.addWidget(self.label_44, 0, 0, 1, 1)

        self.p_sup = QDoubleSpinBox(self.gridLayoutWidget_6)
        self.p_sup.setObjectName(u"p_sup")

        self.gridLayout_6.addWidget(self.p_sup, 0, 1, 1, 1)

        self.label_45 = QLabel(self.gridLayoutWidget_6)
        self.label_45.setObjectName(u"label_45")

        self.gridLayout_6.addWidget(self.label_45, 1, 0, 1, 1)

        self.sarta = QDoubleSpinBox(self.gridLayoutWidget_6)
        self.sarta.setObjectName(u"sarta")
        self.sarta.setMaximum(99999.990000000005239)

        self.gridLayout_6.addWidget(self.sarta, 1, 1, 1, 1)

        self.drill_pipe_table = QTableWidget(self.scrollAreaWidgetContents)
        if (self.drill_pipe_table.columnCount() < 1):
            self.drill_pipe_table.setColumnCount(1)
        __qtablewidgetitem73 = QTableWidgetItem()
        self.drill_pipe_table.setHorizontalHeaderItem(0, __qtablewidgetitem73)
        if (self.drill_pipe_table.rowCount() < 10):
            self.drill_pipe_table.setRowCount(10)
        __qtablewidgetitem74 = QTableWidgetItem()
        self.drill_pipe_table.setVerticalHeaderItem(0, __qtablewidgetitem74)
        __qtablewidgetitem75 = QTableWidgetItem()
        self.drill_pipe_table.setVerticalHeaderItem(1, __qtablewidgetitem75)
        __qtablewidgetitem76 = QTableWidgetItem()
        self.drill_pipe_table.setVerticalHeaderItem(2, __qtablewidgetitem76)
        __qtablewidgetitem77 = QTableWidgetItem()
        self.drill_pipe_table.setVerticalHeaderItem(3, __qtablewidgetitem77)
        __qtablewidgetitem78 = QTableWidgetItem()
        self.drill_pipe_table.setVerticalHeaderItem(4, __qtablewidgetitem78)
        __qtablewidgetitem79 = QTableWidgetItem()
        self.drill_pipe_table.setVerticalHeaderItem(5, __qtablewidgetitem79)
        __qtablewidgetitem80 = QTableWidgetItem()
        self.drill_pipe_table.setVerticalHeaderItem(6, __qtablewidgetitem80)
        __qtablewidgetitem81 = QTableWidgetItem()
        self.drill_pipe_table.setVerticalHeaderItem(7, __qtablewidgetitem81)
        __qtablewidgetitem82 = QTableWidgetItem()
        self.drill_pipe_table.setVerticalHeaderItem(8, __qtablewidgetitem82)
        __qtablewidgetitem83 = QTableWidgetItem()
        self.drill_pipe_table.setVerticalHeaderItem(9, __qtablewidgetitem83)
        __qtablewidgetitem84 = QTableWidgetItem()
        self.drill_pipe_table.setItem(0, 0, __qtablewidgetitem84)
        __qtablewidgetitem85 = QTableWidgetItem()
        self.drill_pipe_table.setItem(1, 0, __qtablewidgetitem85)
        __qtablewidgetitem86 = QTableWidgetItem()
        self.drill_pipe_table.setItem(2, 0, __qtablewidgetitem86)
        __qtablewidgetitem87 = QTableWidgetItem()
        self.drill_pipe_table.setItem(3, 0, __qtablewidgetitem87)
        __qtablewidgetitem88 = QTableWidgetItem()
        self.drill_pipe_table.setItem(4, 0, __qtablewidgetitem88)
        __qtablewidgetitem89 = QTableWidgetItem()
        self.drill_pipe_table.setItem(5, 0, __qtablewidgetitem89)
        __qtablewidgetitem90 = QTableWidgetItem()
        self.drill_pipe_table.setItem(6, 0, __qtablewidgetitem90)
        __qtablewidgetitem91 = QTableWidgetItem()
        self.drill_pipe_table.setItem(7, 0, __qtablewidgetitem91)
        __qtablewidgetitem92 = QTableWidgetItem()
        self.drill_pipe_table.setItem(8, 0, __qtablewidgetitem92)
        __qtablewidgetitem93 = QTableWidgetItem()
        self.drill_pipe_table.setItem(9, 0, __qtablewidgetitem93)
        self.drill_pipe_table.setObjectName(u"drill_pipe_table")
        self.drill_pipe_table.setGeometry(QRect(470, 70, 151, 401))
        self.label_46 = QLabel(self.scrollAreaWidgetContents)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setGeometry(QRect(500, 50, 81, 16))
        self.gridLayoutWidget_7 = QWidget(self.scrollAreaWidgetContents)
        self.gridLayoutWidget_7.setObjectName(u"gridLayoutWidget_7")
        self.gridLayoutWidget_7.setGeometry(QRect(1090, 200, 169, 104))
        self.gridLayout_7 = QGridLayout(self.gridLayoutWidget_7)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_48 = QLabel(self.gridLayoutWidget_7)
        self.label_48.setObjectName(u"label_48")

        self.gridLayout_7.addWidget(self.label_48, 1, 0, 1, 1)

        self.dj = QDoubleSpinBox(self.gridLayoutWidget_7)
        self.dj.setObjectName(u"dj")
        self.dj.setMaximum(9999.989999999999782)

        self.gridLayout_7.addWidget(self.dj, 1, 1, 1, 1)

        self.label_47 = QLabel(self.gridLayoutWidget_7)
        self.label_47.setObjectName(u"label_47")

        self.gridLayout_7.addWidget(self.label_47, 0, 0, 1, 1)

        self.barrena = QDoubleSpinBox(self.gridLayoutWidget_7)
        self.barrena.setObjectName(u"barrena")
        self.barrena.setMaximum(99999.990000000005239)

        self.gridLayout_7.addWidget(self.barrena, 0, 1, 1, 1)

        self.label_49 = QLabel(self.gridLayoutWidget_7)
        self.label_49.setObjectName(u"label_49")

        self.gridLayout_7.addWidget(self.label_49, 2, 0, 1, 1)

        self.anular = QDoubleSpinBox(self.gridLayoutWidget_7)
        self.anular.setObjectName(u"anular")
        self.anular.setMaximum(99999.990000000005239)

        self.gridLayout_7.addWidget(self.anular, 2, 1, 1, 1)

        self.pipe_casing_table = QTableWidget(self.scrollAreaWidgetContents)
        if (self.pipe_casing_table.columnCount() < 1):
            self.pipe_casing_table.setColumnCount(1)
        __qtablewidgetitem94 = QTableWidgetItem()
        self.pipe_casing_table.setHorizontalHeaderItem(0, __qtablewidgetitem94)
        if (self.pipe_casing_table.rowCount() < 10):
            self.pipe_casing_table.setRowCount(10)
        __qtablewidgetitem95 = QTableWidgetItem()
        self.pipe_casing_table.setVerticalHeaderItem(0, __qtablewidgetitem95)
        __qtablewidgetitem96 = QTableWidgetItem()
        self.pipe_casing_table.setVerticalHeaderItem(1, __qtablewidgetitem96)
        __qtablewidgetitem97 = QTableWidgetItem()
        self.pipe_casing_table.setVerticalHeaderItem(2, __qtablewidgetitem97)
        __qtablewidgetitem98 = QTableWidgetItem()
        self.pipe_casing_table.setVerticalHeaderItem(3, __qtablewidgetitem98)
        __qtablewidgetitem99 = QTableWidgetItem()
        self.pipe_casing_table.setVerticalHeaderItem(4, __qtablewidgetitem99)
        __qtablewidgetitem100 = QTableWidgetItem()
        self.pipe_casing_table.setVerticalHeaderItem(5, __qtablewidgetitem100)
        __qtablewidgetitem101 = QTableWidgetItem()
        self.pipe_casing_table.setVerticalHeaderItem(6, __qtablewidgetitem101)
        __qtablewidgetitem102 = QTableWidgetItem()
        self.pipe_casing_table.setVerticalHeaderItem(7, __qtablewidgetitem102)
        __qtablewidgetitem103 = QTableWidgetItem()
        self.pipe_casing_table.setVerticalHeaderItem(8, __qtablewidgetitem103)
        __qtablewidgetitem104 = QTableWidgetItem()
        self.pipe_casing_table.setVerticalHeaderItem(9, __qtablewidgetitem104)
        __qtablewidgetitem105 = QTableWidgetItem()
        self.pipe_casing_table.setItem(0, 0, __qtablewidgetitem105)
        __qtablewidgetitem106 = QTableWidgetItem()
        self.pipe_casing_table.setItem(1, 0, __qtablewidgetitem106)
        __qtablewidgetitem107 = QTableWidgetItem()
        self.pipe_casing_table.setItem(2, 0, __qtablewidgetitem107)
        __qtablewidgetitem108 = QTableWidgetItem()
        self.pipe_casing_table.setItem(3, 0, __qtablewidgetitem108)
        __qtablewidgetitem109 = QTableWidgetItem()
        self.pipe_casing_table.setItem(4, 0, __qtablewidgetitem109)
        __qtablewidgetitem110 = QTableWidgetItem()
        self.pipe_casing_table.setItem(5, 0, __qtablewidgetitem110)
        __qtablewidgetitem111 = QTableWidgetItem()
        self.pipe_casing_table.setItem(6, 0, __qtablewidgetitem111)
        __qtablewidgetitem112 = QTableWidgetItem()
        self.pipe_casing_table.setItem(7, 0, __qtablewidgetitem112)
        __qtablewidgetitem113 = QTableWidgetItem()
        self.pipe_casing_table.setItem(8, 0, __qtablewidgetitem113)
        __qtablewidgetitem114 = QTableWidgetItem()
        self.pipe_casing_table.setItem(9, 0, __qtablewidgetitem114)
        self.pipe_casing_table.setObjectName(u"pipe_casing_table")
        self.pipe_casing_table.setGeometry(QRect(460, 530, 201, 331))
        self.label_50 = QLabel(self.scrollAreaWidgetContents)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setGeometry(QRect(500, 500, 101, 16))
        self.label_51 = QLabel(self.scrollAreaWidgetContents)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setGeometry(QRect(670, 40, 91, 16))
        self.label_51.setAlignment(Qt.AlignCenter)
        self.drill_collar_table = QTableWidget(self.scrollAreaWidgetContents)
        if (self.drill_collar_table.columnCount() < 1):
            self.drill_collar_table.setColumnCount(1)
        __qtablewidgetitem115 = QTableWidgetItem()
        self.drill_collar_table.setHorizontalHeaderItem(0, __qtablewidgetitem115)
        if (self.drill_collar_table.rowCount() < 10):
            self.drill_collar_table.setRowCount(10)
        __qtablewidgetitem116 = QTableWidgetItem()
        self.drill_collar_table.setVerticalHeaderItem(0, __qtablewidgetitem116)
        __qtablewidgetitem117 = QTableWidgetItem()
        self.drill_collar_table.setVerticalHeaderItem(1, __qtablewidgetitem117)
        __qtablewidgetitem118 = QTableWidgetItem()
        self.drill_collar_table.setVerticalHeaderItem(2, __qtablewidgetitem118)
        __qtablewidgetitem119 = QTableWidgetItem()
        self.drill_collar_table.setVerticalHeaderItem(3, __qtablewidgetitem119)
        __qtablewidgetitem120 = QTableWidgetItem()
        self.drill_collar_table.setVerticalHeaderItem(4, __qtablewidgetitem120)
        __qtablewidgetitem121 = QTableWidgetItem()
        self.drill_collar_table.setVerticalHeaderItem(5, __qtablewidgetitem121)
        __qtablewidgetitem122 = QTableWidgetItem()
        self.drill_collar_table.setVerticalHeaderItem(6, __qtablewidgetitem122)
        __qtablewidgetitem123 = QTableWidgetItem()
        self.drill_collar_table.setVerticalHeaderItem(7, __qtablewidgetitem123)
        __qtablewidgetitem124 = QTableWidgetItem()
        self.drill_collar_table.setVerticalHeaderItem(8, __qtablewidgetitem124)
        __qtablewidgetitem125 = QTableWidgetItem()
        self.drill_collar_table.setVerticalHeaderItem(9, __qtablewidgetitem125)
        __qtablewidgetitem126 = QTableWidgetItem()
        self.drill_collar_table.setItem(0, 0, __qtablewidgetitem126)
        __qtablewidgetitem127 = QTableWidgetItem()
        self.drill_collar_table.setItem(1, 0, __qtablewidgetitem127)
        __qtablewidgetitem128 = QTableWidgetItem()
        self.drill_collar_table.setItem(2, 0, __qtablewidgetitem128)
        __qtablewidgetitem129 = QTableWidgetItem()
        self.drill_collar_table.setItem(3, 0, __qtablewidgetitem129)
        __qtablewidgetitem130 = QTableWidgetItem()
        self.drill_collar_table.setItem(4, 0, __qtablewidgetitem130)
        __qtablewidgetitem131 = QTableWidgetItem()
        self.drill_collar_table.setItem(5, 0, __qtablewidgetitem131)
        __qtablewidgetitem132 = QTableWidgetItem()
        self.drill_collar_table.setItem(6, 0, __qtablewidgetitem132)
        __qtablewidgetitem133 = QTableWidgetItem()
        self.drill_collar_table.setItem(7, 0, __qtablewidgetitem133)
        __qtablewidgetitem134 = QTableWidgetItem()
        self.drill_collar_table.setItem(8, 0, __qtablewidgetitem134)
        __qtablewidgetitem135 = QTableWidgetItem()
        self.drill_collar_table.setItem(9, 0, __qtablewidgetitem135)
        self.drill_collar_table.setObjectName(u"drill_collar_table")
        self.drill_collar_table.setGeometry(QRect(650, 70, 151, 401))
        self.label_52 = QLabel(self.scrollAreaWidgetContents)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setGeometry(QRect(670, 500, 141, 20))
        self.label_52.setAlignment(Qt.AlignCenter)
        self.pipe_open_table = QTableWidget(self.scrollAreaWidgetContents)
        if (self.pipe_open_table.columnCount() < 1):
            self.pipe_open_table.setColumnCount(1)
        __qtablewidgetitem136 = QTableWidgetItem()
        self.pipe_open_table.setHorizontalHeaderItem(0, __qtablewidgetitem136)
        if (self.pipe_open_table.rowCount() < 10):
            self.pipe_open_table.setRowCount(10)
        __qtablewidgetitem137 = QTableWidgetItem()
        self.pipe_open_table.setVerticalHeaderItem(0, __qtablewidgetitem137)
        __qtablewidgetitem138 = QTableWidgetItem()
        self.pipe_open_table.setVerticalHeaderItem(1, __qtablewidgetitem138)
        __qtablewidgetitem139 = QTableWidgetItem()
        self.pipe_open_table.setVerticalHeaderItem(2, __qtablewidgetitem139)
        __qtablewidgetitem140 = QTableWidgetItem()
        self.pipe_open_table.setVerticalHeaderItem(3, __qtablewidgetitem140)
        __qtablewidgetitem141 = QTableWidgetItem()
        self.pipe_open_table.setVerticalHeaderItem(4, __qtablewidgetitem141)
        __qtablewidgetitem142 = QTableWidgetItem()
        self.pipe_open_table.setVerticalHeaderItem(5, __qtablewidgetitem142)
        __qtablewidgetitem143 = QTableWidgetItem()
        self.pipe_open_table.setVerticalHeaderItem(6, __qtablewidgetitem143)
        __qtablewidgetitem144 = QTableWidgetItem()
        self.pipe_open_table.setVerticalHeaderItem(7, __qtablewidgetitem144)
        __qtablewidgetitem145 = QTableWidgetItem()
        self.pipe_open_table.setVerticalHeaderItem(8, __qtablewidgetitem145)
        __qtablewidgetitem146 = QTableWidgetItem()
        self.pipe_open_table.setVerticalHeaderItem(9, __qtablewidgetitem146)
        __qtablewidgetitem147 = QTableWidgetItem()
        self.pipe_open_table.setItem(0, 0, __qtablewidgetitem147)
        __qtablewidgetitem148 = QTableWidgetItem()
        self.pipe_open_table.setItem(1, 0, __qtablewidgetitem148)
        __qtablewidgetitem149 = QTableWidgetItem()
        self.pipe_open_table.setItem(2, 0, __qtablewidgetitem149)
        __qtablewidgetitem150 = QTableWidgetItem()
        self.pipe_open_table.setItem(3, 0, __qtablewidgetitem150)
        __qtablewidgetitem151 = QTableWidgetItem()
        self.pipe_open_table.setItem(4, 0, __qtablewidgetitem151)
        __qtablewidgetitem152 = QTableWidgetItem()
        self.pipe_open_table.setItem(5, 0, __qtablewidgetitem152)
        __qtablewidgetitem153 = QTableWidgetItem()
        self.pipe_open_table.setItem(6, 0, __qtablewidgetitem153)
        __qtablewidgetitem154 = QTableWidgetItem()
        self.pipe_open_table.setItem(7, 0, __qtablewidgetitem154)
        __qtablewidgetitem155 = QTableWidgetItem()
        self.pipe_open_table.setItem(8, 0, __qtablewidgetitem155)
        __qtablewidgetitem156 = QTableWidgetItem()
        self.pipe_open_table.setItem(9, 0, __qtablewidgetitem156)
        self.pipe_open_table.setObjectName(u"pipe_open_table")
        self.pipe_open_table.setGeometry(QRect(680, 530, 201, 331))
        self.gridLayoutWidget_8 = QWidget(self.scrollAreaWidgetContents)
        self.gridLayoutWidget_8.setObjectName(u"gridLayoutWidget_8")
        self.gridLayoutWidget_8.setGeometry(QRect(1090, 50, 161, 71))
        self.gridLayout_8 = QGridLayout(self.gridLayoutWidget_8)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.p_total = QDoubleSpinBox(self.gridLayoutWidget_8)
        self.p_total.setObjectName(u"p_total")
        self.p_total.setMaximum(99999.990000000005239)

        self.gridLayout_8.addWidget(self.p_total, 0, 1, 1, 1)

        self.label_53 = QLabel(self.gridLayoutWidget_8)
        self.label_53.setObjectName(u"label_53")

        self.gridLayout_8.addWidget(self.label_53, 0, 0, 1, 1)

        self.gridLayoutWidget_9 = QWidget(self.scrollAreaWidgetContents)
        self.gridLayoutWidget_9.setObjectName(u"gridLayoutWidget_9")
        self.gridLayoutWidget_9.setGeometry(QRect(1090, 10, 160, 31))
        self.gridLayout_9 = QGridLayout(self.gridLayoutWidget_9)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_58 = QLabel(self.gridLayoutWidget_9)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.label_58, 0, 0, 1, 1)

        self.ecd = QDoubleSpinBox(self.gridLayoutWidget_9)
        self.ecd.setObjectName(u"ecd")

        self.gridLayout_9.addWidget(self.ecd, 0, 1, 1, 1)

        self.label_59 = QLabel(self.scrollAreaWidgetContents)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setGeometry(QRect(890, 500, 131, 16))
        self.drill_collar_open_table = QTableWidget(self.scrollAreaWidgetContents)
        if (self.drill_collar_open_table.columnCount() < 1):
            self.drill_collar_open_table.setColumnCount(1)
        __qtablewidgetitem157 = QTableWidgetItem()
        self.drill_collar_open_table.setHorizontalHeaderItem(0, __qtablewidgetitem157)
        if (self.drill_collar_open_table.rowCount() < 10):
            self.drill_collar_open_table.setRowCount(10)
        __qtablewidgetitem158 = QTableWidgetItem()
        self.drill_collar_open_table.setVerticalHeaderItem(0, __qtablewidgetitem158)
        __qtablewidgetitem159 = QTableWidgetItem()
        self.drill_collar_open_table.setVerticalHeaderItem(1, __qtablewidgetitem159)
        __qtablewidgetitem160 = QTableWidgetItem()
        self.drill_collar_open_table.setVerticalHeaderItem(2, __qtablewidgetitem160)
        __qtablewidgetitem161 = QTableWidgetItem()
        self.drill_collar_open_table.setVerticalHeaderItem(3, __qtablewidgetitem161)
        __qtablewidgetitem162 = QTableWidgetItem()
        self.drill_collar_open_table.setVerticalHeaderItem(4, __qtablewidgetitem162)
        __qtablewidgetitem163 = QTableWidgetItem()
        self.drill_collar_open_table.setVerticalHeaderItem(5, __qtablewidgetitem163)
        __qtablewidgetitem164 = QTableWidgetItem()
        self.drill_collar_open_table.setVerticalHeaderItem(6, __qtablewidgetitem164)
        __qtablewidgetitem165 = QTableWidgetItem()
        self.drill_collar_open_table.setVerticalHeaderItem(7, __qtablewidgetitem165)
        __qtablewidgetitem166 = QTableWidgetItem()
        self.drill_collar_open_table.setVerticalHeaderItem(8, __qtablewidgetitem166)
        __qtablewidgetitem167 = QTableWidgetItem()
        self.drill_collar_open_table.setVerticalHeaderItem(9, __qtablewidgetitem167)
        __qtablewidgetitem168 = QTableWidgetItem()
        self.drill_collar_open_table.setItem(0, 0, __qtablewidgetitem168)
        __qtablewidgetitem169 = QTableWidgetItem()
        self.drill_collar_open_table.setItem(1, 0, __qtablewidgetitem169)
        __qtablewidgetitem170 = QTableWidgetItem()
        self.drill_collar_open_table.setItem(2, 0, __qtablewidgetitem170)
        __qtablewidgetitem171 = QTableWidgetItem()
        self.drill_collar_open_table.setItem(3, 0, __qtablewidgetitem171)
        __qtablewidgetitem172 = QTableWidgetItem()
        self.drill_collar_open_table.setItem(4, 0, __qtablewidgetitem172)
        __qtablewidgetitem173 = QTableWidgetItem()
        self.drill_collar_open_table.setItem(5, 0, __qtablewidgetitem173)
        __qtablewidgetitem174 = QTableWidgetItem()
        self.drill_collar_open_table.setItem(6, 0, __qtablewidgetitem174)
        __qtablewidgetitem175 = QTableWidgetItem()
        self.drill_collar_open_table.setItem(7, 0, __qtablewidgetitem175)
        __qtablewidgetitem176 = QTableWidgetItem()
        self.drill_collar_open_table.setItem(8, 0, __qtablewidgetitem176)
        __qtablewidgetitem177 = QTableWidgetItem()
        self.drill_collar_open_table.setItem(9, 0, __qtablewidgetitem177)
        self.drill_collar_open_table.setObjectName(u"drill_collar_open_table")
        self.drill_collar_open_table.setGeometry(QRect(890, 530, 201, 331))
        self.label_60 = QLabel(self.scrollAreaWidgetContents)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setGeometry(QRect(830, 40, 191, 16))
        self.hidraulic_drill_table = QTableWidget(self.scrollAreaWidgetContents)
        if (self.hidraulic_drill_table.columnCount() < 1):
            self.hidraulic_drill_table.setColumnCount(1)
        __qtablewidgetitem178 = QTableWidgetItem()
        self.hidraulic_drill_table.setHorizontalHeaderItem(0, __qtablewidgetitem178)
        if (self.hidraulic_drill_table.rowCount() < 8):
            self.hidraulic_drill_table.setRowCount(8)
        __qtablewidgetitem179 = QTableWidgetItem()
        self.hidraulic_drill_table.setVerticalHeaderItem(0, __qtablewidgetitem179)
        __qtablewidgetitem180 = QTableWidgetItem()
        self.hidraulic_drill_table.setVerticalHeaderItem(1, __qtablewidgetitem180)
        __qtablewidgetitem181 = QTableWidgetItem()
        self.hidraulic_drill_table.setVerticalHeaderItem(2, __qtablewidgetitem181)
        __qtablewidgetitem182 = QTableWidgetItem()
        self.hidraulic_drill_table.setVerticalHeaderItem(3, __qtablewidgetitem182)
        __qtablewidgetitem183 = QTableWidgetItem()
        self.hidraulic_drill_table.setVerticalHeaderItem(4, __qtablewidgetitem183)
        __qtablewidgetitem184 = QTableWidgetItem()
        self.hidraulic_drill_table.setVerticalHeaderItem(5, __qtablewidgetitem184)
        __qtablewidgetitem185 = QTableWidgetItem()
        self.hidraulic_drill_table.setVerticalHeaderItem(6, __qtablewidgetitem185)
        __qtablewidgetitem186 = QTableWidgetItem()
        self.hidraulic_drill_table.setVerticalHeaderItem(7, __qtablewidgetitem186)
        __qtablewidgetitem187 = QTableWidgetItem()
        self.hidraulic_drill_table.setItem(0, 0, __qtablewidgetitem187)
        __qtablewidgetitem188 = QTableWidgetItem()
        self.hidraulic_drill_table.setItem(1, 0, __qtablewidgetitem188)
        __qtablewidgetitem189 = QTableWidgetItem()
        self.hidraulic_drill_table.setItem(2, 0, __qtablewidgetitem189)
        __qtablewidgetitem190 = QTableWidgetItem()
        self.hidraulic_drill_table.setItem(3, 0, __qtablewidgetitem190)
        __qtablewidgetitem191 = QTableWidgetItem()
        self.hidraulic_drill_table.setItem(4, 0, __qtablewidgetitem191)
        __qtablewidgetitem192 = QTableWidgetItem()
        self.hidraulic_drill_table.setItem(5, 0, __qtablewidgetitem192)
        __qtablewidgetitem193 = QTableWidgetItem()
        self.hidraulic_drill_table.setItem(6, 0, __qtablewidgetitem193)
        __qtablewidgetitem194 = QTableWidgetItem()
        self.hidraulic_drill_table.setItem(7, 0, __qtablewidgetitem194)
        self.hidraulic_drill_table.setObjectName(u"hidraulic_drill_table")
        self.hidraulic_drill_table.setGeometry(QRect(830, 70, 181, 391))
        self.label_61 = QLabel(self.scrollAreaWidgetContents)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setGeometry(QRect(1120, 430, 151, 16))
        self.clean_table = QTableWidget(self.scrollAreaWidgetContents)
        if (self.clean_table.columnCount() < 1):
            self.clean_table.setColumnCount(1)
        __qtablewidgetitem195 = QTableWidgetItem()
        self.clean_table.setHorizontalHeaderItem(0, __qtablewidgetitem195)
        if (self.clean_table.rowCount() < 12):
            self.clean_table.setRowCount(12)
        __qtablewidgetitem196 = QTableWidgetItem()
        self.clean_table.setVerticalHeaderItem(0, __qtablewidgetitem196)
        __qtablewidgetitem197 = QTableWidgetItem()
        self.clean_table.setVerticalHeaderItem(1, __qtablewidgetitem197)
        __qtablewidgetitem198 = QTableWidgetItem()
        self.clean_table.setVerticalHeaderItem(2, __qtablewidgetitem198)
        __qtablewidgetitem199 = QTableWidgetItem()
        self.clean_table.setVerticalHeaderItem(3, __qtablewidgetitem199)
        __qtablewidgetitem200 = QTableWidgetItem()
        self.clean_table.setVerticalHeaderItem(4, __qtablewidgetitem200)
        __qtablewidgetitem201 = QTableWidgetItem()
        self.clean_table.setVerticalHeaderItem(5, __qtablewidgetitem201)
        __qtablewidgetitem202 = QTableWidgetItem()
        self.clean_table.setVerticalHeaderItem(6, __qtablewidgetitem202)
        __qtablewidgetitem203 = QTableWidgetItem()
        self.clean_table.setVerticalHeaderItem(7, __qtablewidgetitem203)
        __qtablewidgetitem204 = QTableWidgetItem()
        self.clean_table.setVerticalHeaderItem(8, __qtablewidgetitem204)
        __qtablewidgetitem205 = QTableWidgetItem()
        self.clean_table.setVerticalHeaderItem(9, __qtablewidgetitem205)
        __qtablewidgetitem206 = QTableWidgetItem()
        self.clean_table.setVerticalHeaderItem(10, __qtablewidgetitem206)
        __qtablewidgetitem207 = QTableWidgetItem()
        self.clean_table.setVerticalHeaderItem(11, __qtablewidgetitem207)
        __qtablewidgetitem208 = QTableWidgetItem()
        self.clean_table.setItem(0, 0, __qtablewidgetitem208)
        __qtablewidgetitem209 = QTableWidgetItem()
        self.clean_table.setItem(1, 0, __qtablewidgetitem209)
        __qtablewidgetitem210 = QTableWidgetItem()
        self.clean_table.setItem(2, 0, __qtablewidgetitem210)
        __qtablewidgetitem211 = QTableWidgetItem()
        self.clean_table.setItem(3, 0, __qtablewidgetitem211)
        __qtablewidgetitem212 = QTableWidgetItem()
        self.clean_table.setItem(4, 0, __qtablewidgetitem212)
        __qtablewidgetitem213 = QTableWidgetItem()
        self.clean_table.setItem(5, 0, __qtablewidgetitem213)
        __qtablewidgetitem214 = QTableWidgetItem()
        self.clean_table.setItem(6, 0, __qtablewidgetitem214)
        __qtablewidgetitem215 = QTableWidgetItem()
        self.clean_table.setItem(7, 0, __qtablewidgetitem215)
        __qtablewidgetitem216 = QTableWidgetItem()
        self.clean_table.setItem(8, 0, __qtablewidgetitem216)
        __qtablewidgetitem217 = QTableWidgetItem()
        self.clean_table.setItem(9, 0, __qtablewidgetitem217)
        __qtablewidgetitem218 = QTableWidgetItem()
        self.clean_table.setItem(10, 0, __qtablewidgetitem218)
        __qtablewidgetitem219 = QTableWidgetItem()
        self.clean_table.setItem(11, 0, __qtablewidgetitem219)
        self.clean_table.setObjectName(u"clean_table")
        self.clean_table.setGeometry(QRect(1110, 460, 171, 411))
        self.btn_calcular = QPushButton(self.scrollAreaWidgetContents)
        self.btn_calcular.setObjectName(u"btn_calcular")
        self.btn_calcular.setGeometry(QRect(40, 850, 111, 41))
        self.btn_limpiar = QPushButton(self.scrollAreaWidgetContents)
        self.btn_limpiar.setObjectName(u"btn_limpiar")
        self.btn_limpiar.setGeometry(QRect(200, 850, 111, 41))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
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
        self.bt_3.setText(QCoreApplication.translate("MainWindow", u"Hidar\u00falica", None))
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
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Caida de Presi\u00f3n Total en el Sistema y ECD", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Drill Collar Length", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Casing Size", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Solid SG", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"L300", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Bit Size", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Drill Pipe Size", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Pump Output", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Pump Pressure", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Prof Total", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Open Hole Length", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Rate of Penetration", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Gel strength", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Drill Collar Size", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Mud Weight", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Fracture Gradient", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Casing length", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"L600", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Density of Particle", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Diameter of Particle", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Surface Case", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Plastic Viscosity", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Yield Point", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Psup", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Sarta", None))
        ___qtablewidgetitem73 = self.drill_pipe_table.horizontalHeaderItem(0)
        ___qtablewidgetitem73.setText(QCoreApplication.translate("MainWindow", u"Values", None));
        ___qtablewidgetitem74 = self.drill_pipe_table.verticalHeaderItem(0)
        ___qtablewidgetitem74.setText(QCoreApplication.translate("MainWindow", u"Vp1", None));
        ___qtablewidgetitem75 = self.drill_pipe_table.verticalHeaderItem(1)
        ___qtablewidgetitem75.setText(QCoreApplication.translate("MainWindow", u"np", None));
        ___qtablewidgetitem76 = self.drill_pipe_table.verticalHeaderItem(2)
        ___qtablewidgetitem76.setText(QCoreApplication.translate("MainWindow", u"kp", None));
        ___qtablewidgetitem77 = self.drill_pipe_table.verticalHeaderItem(3)
        ___qtablewidgetitem77.setText(QCoreApplication.translate("MainWindow", u"ViscE1", None));
        ___qtablewidgetitem78 = self.drill_pipe_table.verticalHeaderItem(4)
        ___qtablewidgetitem78.setText(QCoreApplication.translate("MainWindow", u"alfa", None));
        ___qtablewidgetitem79 = self.drill_pipe_table.verticalHeaderItem(5)
        ___qtablewidgetitem79.setText(QCoreApplication.translate("MainWindow", u"Rep1", None));
        ___qtablewidgetitem80 = self.drill_pipe_table.verticalHeaderItem(6)
        ___qtablewidgetitem80.setText(QCoreApplication.translate("MainWindow", u"ReL", None));
        ___qtablewidgetitem81 = self.drill_pipe_table.verticalHeaderItem(7)
        ___qtablewidgetitem81.setText(QCoreApplication.translate("MainWindow", u"ReT", None));
        ___qtablewidgetitem82 = self.drill_pipe_table.verticalHeaderItem(8)
        ___qtablewidgetitem82.setText(QCoreApplication.translate("MainWindow", u"fp1", None));
        ___qtablewidgetitem83 = self.drill_pipe_table.verticalHeaderItem(9)
        ___qtablewidgetitem83.setText(QCoreApplication.translate("MainWindow", u"Ppipe", None));

        __sortingEnabled3 = self.drill_pipe_table.isSortingEnabled()
        self.drill_pipe_table.setSortingEnabled(False)
        ___qtablewidgetitem84 = self.drill_pipe_table.item(0, 0)
        ___qtablewidgetitem84.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem85 = self.drill_pipe_table.item(1, 0)
        ___qtablewidgetitem85.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem86 = self.drill_pipe_table.item(2, 0)
        ___qtablewidgetitem86.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem87 = self.drill_pipe_table.item(3, 0)
        ___qtablewidgetitem87.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem88 = self.drill_pipe_table.item(4, 0)
        ___qtablewidgetitem88.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem89 = self.drill_pipe_table.item(5, 0)
        ___qtablewidgetitem89.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem90 = self.drill_pipe_table.item(6, 0)
        ___qtablewidgetitem90.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem91 = self.drill_pipe_table.item(7, 0)
        ___qtablewidgetitem91.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem92 = self.drill_pipe_table.item(8, 0)
        ___qtablewidgetitem92.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem93 = self.drill_pipe_table.item(9, 0)
        ___qtablewidgetitem93.setText(QCoreApplication.translate("MainWindow", u"0", None));
        self.drill_pipe_table.setSortingEnabled(__sortingEnabled3)

        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Drill Pipe", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"DJ's", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Barrena", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Anular", None))
        ___qtablewidgetitem94 = self.pipe_casing_table.horizontalHeaderItem(0)
        ___qtablewidgetitem94.setText(QCoreApplication.translate("MainWindow", u"Values", None));
        ___qtablewidgetitem95 = self.pipe_casing_table.verticalHeaderItem(0)
        ___qtablewidgetitem95.setText(QCoreApplication.translate("MainWindow", u"Va1", None));
        ___qtablewidgetitem96 = self.pipe_casing_table.verticalHeaderItem(1)
        ___qtablewidgetitem96.setText(QCoreApplication.translate("MainWindow", u"na", None));
        ___qtablewidgetitem97 = self.pipe_casing_table.verticalHeaderItem(2)
        ___qtablewidgetitem97.setText(QCoreApplication.translate("MainWindow", u"ka", None));
        ___qtablewidgetitem98 = self.pipe_casing_table.verticalHeaderItem(3)
        ___qtablewidgetitem98.setText(QCoreApplication.translate("MainWindow", u"VisEa1", None));
        ___qtablewidgetitem99 = self.pipe_casing_table.verticalHeaderItem(4)
        ___qtablewidgetitem99.setText(QCoreApplication.translate("MainWindow", u"beta", None));
        ___qtablewidgetitem100 = self.pipe_casing_table.verticalHeaderItem(5)
        ___qtablewidgetitem100.setText(QCoreApplication.translate("MainWindow", u"Rea1", None));
        ___qtablewidgetitem101 = self.pipe_casing_table.verticalHeaderItem(6)
        ___qtablewidgetitem101.setText(QCoreApplication.translate("MainWindow", u"ReLa", None));
        ___qtablewidgetitem102 = self.pipe_casing_table.verticalHeaderItem(7)
        ___qtablewidgetitem102.setText(QCoreApplication.translate("MainWindow", u"ReTa", None));
        ___qtablewidgetitem103 = self.pipe_casing_table.verticalHeaderItem(8)
        ___qtablewidgetitem103.setText(QCoreApplication.translate("MainWindow", u"fa1", None));
        ___qtablewidgetitem104 = self.pipe_casing_table.verticalHeaderItem(9)
        ___qtablewidgetitem104.setText(QCoreApplication.translate("MainWindow", u"Pa1", None));

        __sortingEnabled4 = self.pipe_casing_table.isSortingEnabled()
        self.pipe_casing_table.setSortingEnabled(False)
        ___qtablewidgetitem105 = self.pipe_casing_table.item(0, 0)
        ___qtablewidgetitem105.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem106 = self.pipe_casing_table.item(1, 0)
        ___qtablewidgetitem106.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem107 = self.pipe_casing_table.item(2, 0)
        ___qtablewidgetitem107.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem108 = self.pipe_casing_table.item(3, 0)
        ___qtablewidgetitem108.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem109 = self.pipe_casing_table.item(4, 0)
        ___qtablewidgetitem109.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem110 = self.pipe_casing_table.item(5, 0)
        ___qtablewidgetitem110.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem111 = self.pipe_casing_table.item(6, 0)
        ___qtablewidgetitem111.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem112 = self.pipe_casing_table.item(7, 0)
        ___qtablewidgetitem112.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem113 = self.pipe_casing_table.item(8, 0)
        ___qtablewidgetitem113.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem114 = self.pipe_casing_table.item(9, 0)
        ___qtablewidgetitem114.setText(QCoreApplication.translate("MainWindow", u"0", None));
        self.pipe_casing_table.setSortingEnabled(__sortingEnabled4)

        self.label_50.setText(QCoreApplication.translate("MainWindow", u"Pipe/Casing", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Drill Collar", None))
        ___qtablewidgetitem115 = self.drill_collar_table.horizontalHeaderItem(0)
        ___qtablewidgetitem115.setText(QCoreApplication.translate("MainWindow", u"Values", None));
        ___qtablewidgetitem116 = self.drill_collar_table.verticalHeaderItem(0)
        ___qtablewidgetitem116.setText(QCoreApplication.translate("MainWindow", u"Vp2", None));
        ___qtablewidgetitem117 = self.drill_collar_table.verticalHeaderItem(1)
        ___qtablewidgetitem117.setText(QCoreApplication.translate("MainWindow", u"np", None));
        ___qtablewidgetitem118 = self.drill_collar_table.verticalHeaderItem(2)
        ___qtablewidgetitem118.setText(QCoreApplication.translate("MainWindow", u"kp", None));
        ___qtablewidgetitem119 = self.drill_collar_table.verticalHeaderItem(3)
        ___qtablewidgetitem119.setText(QCoreApplication.translate("MainWindow", u"ViscE2", None));
        ___qtablewidgetitem120 = self.drill_collar_table.verticalHeaderItem(4)
        ___qtablewidgetitem120.setText(QCoreApplication.translate("MainWindow", u"alfa", None));
        ___qtablewidgetitem121 = self.drill_collar_table.verticalHeaderItem(5)
        ___qtablewidgetitem121.setText(QCoreApplication.translate("MainWindow", u"Rep2", None));
        ___qtablewidgetitem122 = self.drill_collar_table.verticalHeaderItem(6)
        ___qtablewidgetitem122.setText(QCoreApplication.translate("MainWindow", u"ReL", None));
        ___qtablewidgetitem123 = self.drill_collar_table.verticalHeaderItem(7)
        ___qtablewidgetitem123.setText(QCoreApplication.translate("MainWindow", u"ReT", None));
        ___qtablewidgetitem124 = self.drill_collar_table.verticalHeaderItem(8)
        ___qtablewidgetitem124.setText(QCoreApplication.translate("MainWindow", u"fp2", None));
        ___qtablewidgetitem125 = self.drill_collar_table.verticalHeaderItem(9)
        ___qtablewidgetitem125.setText(QCoreApplication.translate("MainWindow", u"Pd.c.", None));

        __sortingEnabled5 = self.drill_collar_table.isSortingEnabled()
        self.drill_collar_table.setSortingEnabled(False)
        ___qtablewidgetitem126 = self.drill_collar_table.item(0, 0)
        ___qtablewidgetitem126.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem127 = self.drill_collar_table.item(1, 0)
        ___qtablewidgetitem127.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem128 = self.drill_collar_table.item(2, 0)
        ___qtablewidgetitem128.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem129 = self.drill_collar_table.item(3, 0)
        ___qtablewidgetitem129.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem130 = self.drill_collar_table.item(4, 0)
        ___qtablewidgetitem130.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem131 = self.drill_collar_table.item(5, 0)
        ___qtablewidgetitem131.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem132 = self.drill_collar_table.item(6, 0)
        ___qtablewidgetitem132.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem133 = self.drill_collar_table.item(7, 0)
        ___qtablewidgetitem133.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem134 = self.drill_collar_table.item(8, 0)
        ___qtablewidgetitem134.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem135 = self.drill_collar_table.item(9, 0)
        ___qtablewidgetitem135.setText(QCoreApplication.translate("MainWindow", u"0", None));
        self.drill_collar_table.setSortingEnabled(__sortingEnabled5)

        self.label_52.setText(QCoreApplication.translate("MainWindow", u"Pipe/Open Hole", None))
        ___qtablewidgetitem136 = self.pipe_open_table.horizontalHeaderItem(0)
        ___qtablewidgetitem136.setText(QCoreApplication.translate("MainWindow", u"Values", None));
        ___qtablewidgetitem137 = self.pipe_open_table.verticalHeaderItem(0)
        ___qtablewidgetitem137.setText(QCoreApplication.translate("MainWindow", u"Va2", None));
        ___qtablewidgetitem138 = self.pipe_open_table.verticalHeaderItem(1)
        ___qtablewidgetitem138.setText(QCoreApplication.translate("MainWindow", u"na", None));
        ___qtablewidgetitem139 = self.pipe_open_table.verticalHeaderItem(2)
        ___qtablewidgetitem139.setText(QCoreApplication.translate("MainWindow", u"ka", None));
        ___qtablewidgetitem140 = self.pipe_open_table.verticalHeaderItem(3)
        ___qtablewidgetitem140.setText(QCoreApplication.translate("MainWindow", u"VisEa2", None));
        ___qtablewidgetitem141 = self.pipe_open_table.verticalHeaderItem(4)
        ___qtablewidgetitem141.setText(QCoreApplication.translate("MainWindow", u"beta", None));
        ___qtablewidgetitem142 = self.pipe_open_table.verticalHeaderItem(5)
        ___qtablewidgetitem142.setText(QCoreApplication.translate("MainWindow", u"Rea2", None));
        ___qtablewidgetitem143 = self.pipe_open_table.verticalHeaderItem(6)
        ___qtablewidgetitem143.setText(QCoreApplication.translate("MainWindow", u"ReLa", None));
        ___qtablewidgetitem144 = self.pipe_open_table.verticalHeaderItem(7)
        ___qtablewidgetitem144.setText(QCoreApplication.translate("MainWindow", u"ReTa", None));
        ___qtablewidgetitem145 = self.pipe_open_table.verticalHeaderItem(8)
        ___qtablewidgetitem145.setText(QCoreApplication.translate("MainWindow", u"fa2", None));
        ___qtablewidgetitem146 = self.pipe_open_table.verticalHeaderItem(9)
        ___qtablewidgetitem146.setText(QCoreApplication.translate("MainWindow", u"Pa2", None));

        __sortingEnabled6 = self.pipe_open_table.isSortingEnabled()
        self.pipe_open_table.setSortingEnabled(False)
        ___qtablewidgetitem147 = self.pipe_open_table.item(0, 0)
        ___qtablewidgetitem147.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem148 = self.pipe_open_table.item(1, 0)
        ___qtablewidgetitem148.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem149 = self.pipe_open_table.item(2, 0)
        ___qtablewidgetitem149.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem150 = self.pipe_open_table.item(3, 0)
        ___qtablewidgetitem150.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem151 = self.pipe_open_table.item(4, 0)
        ___qtablewidgetitem151.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem152 = self.pipe_open_table.item(5, 0)
        ___qtablewidgetitem152.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem153 = self.pipe_open_table.item(6, 0)
        ___qtablewidgetitem153.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem154 = self.pipe_open_table.item(7, 0)
        ___qtablewidgetitem154.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem155 = self.pipe_open_table.item(8, 0)
        ___qtablewidgetitem155.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem156 = self.pipe_open_table.item(9, 0)
        ___qtablewidgetitem156.setText(QCoreApplication.translate("MainWindow", u"0", None));
        self.pipe_open_table.setSortingEnabled(__sortingEnabled6)

        self.label_53.setText(QCoreApplication.translate("MainWindow", u"PTotal", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"ECD", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"Drill Collar/Open Hole", None))
        ___qtablewidgetitem157 = self.drill_collar_open_table.horizontalHeaderItem(0)
        ___qtablewidgetitem157.setText(QCoreApplication.translate("MainWindow", u"Values", None));
        ___qtablewidgetitem158 = self.drill_collar_open_table.verticalHeaderItem(0)
        ___qtablewidgetitem158.setText(QCoreApplication.translate("MainWindow", u"Va3", None));
        ___qtablewidgetitem159 = self.drill_collar_open_table.verticalHeaderItem(1)
        ___qtablewidgetitem159.setText(QCoreApplication.translate("MainWindow", u"na", None));
        ___qtablewidgetitem160 = self.drill_collar_open_table.verticalHeaderItem(2)
        ___qtablewidgetitem160.setText(QCoreApplication.translate("MainWindow", u"ka", None));
        ___qtablewidgetitem161 = self.drill_collar_open_table.verticalHeaderItem(3)
        ___qtablewidgetitem161.setText(QCoreApplication.translate("MainWindow", u"VisEa3", None));
        ___qtablewidgetitem162 = self.drill_collar_open_table.verticalHeaderItem(4)
        ___qtablewidgetitem162.setText(QCoreApplication.translate("MainWindow", u"beta", None));
        ___qtablewidgetitem163 = self.drill_collar_open_table.verticalHeaderItem(5)
        ___qtablewidgetitem163.setText(QCoreApplication.translate("MainWindow", u"Rea4", None));
        ___qtablewidgetitem164 = self.drill_collar_open_table.verticalHeaderItem(6)
        ___qtablewidgetitem164.setText(QCoreApplication.translate("MainWindow", u"ReLa", None));
        ___qtablewidgetitem165 = self.drill_collar_open_table.verticalHeaderItem(7)
        ___qtablewidgetitem165.setText(QCoreApplication.translate("MainWindow", u"ReTa", None));
        ___qtablewidgetitem166 = self.drill_collar_open_table.verticalHeaderItem(8)
        ___qtablewidgetitem166.setText(QCoreApplication.translate("MainWindow", u"fa3", None));
        ___qtablewidgetitem167 = self.drill_collar_open_table.verticalHeaderItem(9)
        ___qtablewidgetitem167.setText(QCoreApplication.translate("MainWindow", u"Pa3", None));

        __sortingEnabled7 = self.drill_collar_open_table.isSortingEnabled()
        self.drill_collar_open_table.setSortingEnabled(False)
        ___qtablewidgetitem168 = self.drill_collar_open_table.item(0, 0)
        ___qtablewidgetitem168.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem169 = self.drill_collar_open_table.item(1, 0)
        ___qtablewidgetitem169.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem170 = self.drill_collar_open_table.item(2, 0)
        ___qtablewidgetitem170.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem171 = self.drill_collar_open_table.item(3, 0)
        ___qtablewidgetitem171.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem172 = self.drill_collar_open_table.item(4, 0)
        ___qtablewidgetitem172.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem173 = self.drill_collar_open_table.item(5, 0)
        ___qtablewidgetitem173.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem174 = self.drill_collar_open_table.item(6, 0)
        ___qtablewidgetitem174.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem175 = self.drill_collar_open_table.item(7, 0)
        ___qtablewidgetitem175.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem176 = self.drill_collar_open_table.item(8, 0)
        ___qtablewidgetitem176.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem177 = self.drill_collar_open_table.item(9, 0)
        ___qtablewidgetitem177.setText(QCoreApplication.translate("MainWindow", u"0", None));
        self.drill_collar_open_table.setSortingEnabled(__sortingEnabled7)

        self.label_60.setText(QCoreApplication.translate("MainWindow", u"Hidr\u00e1ulica de la Barrena", None))
        ___qtablewidgetitem178 = self.hidraulic_drill_table.horizontalHeaderItem(0)
        ___qtablewidgetitem178.setText(QCoreApplication.translate("MainWindow", u"Values", None));
        ___qtablewidgetitem179 = self.hidraulic_drill_table.verticalHeaderItem(0)
        ___qtablewidgetitem179.setText(QCoreApplication.translate("MainWindow", u"Vab", None));
        ___qtablewidgetitem180 = self.hidraulic_drill_table.verticalHeaderItem(1)
        ___qtablewidgetitem180.setText(QCoreApplication.translate("MainWindow", u"HHPb", None));
        ___qtablewidgetitem181 = self.hidraulic_drill_table.verticalHeaderItem(2)
        ___qtablewidgetitem181.setText(QCoreApplication.translate("MainWindow", u"HHPb/pg2", None));
        ___qtablewidgetitem182 = self.hidraulic_drill_table.verticalHeaderItem(3)
        ___qtablewidgetitem182.setText(QCoreApplication.translate("MainWindow", u"%psib", None));
        ___qtablewidgetitem183 = self.hidraulic_drill_table.verticalHeaderItem(4)
        ___qtablewidgetitem183.setText(QCoreApplication.translate("MainWindow", u"SysHHP", None));
        ___qtablewidgetitem184 = self.hidraulic_drill_table.verticalHeaderItem(5)
        ___qtablewidgetitem184.setText(QCoreApplication.translate("MainWindow", u"Vn", None));
        ___qtablewidgetitem185 = self.hidraulic_drill_table.verticalHeaderItem(6)
        ___qtablewidgetitem185.setText(QCoreApplication.translate("MainWindow", u"IF", None));
        ___qtablewidgetitem186 = self.hidraulic_drill_table.verticalHeaderItem(7)
        ___qtablewidgetitem186.setText(QCoreApplication.translate("MainWindow", u"IF/pg2", None));

        __sortingEnabled8 = self.hidraulic_drill_table.isSortingEnabled()
        self.hidraulic_drill_table.setSortingEnabled(False)
        ___qtablewidgetitem187 = self.hidraulic_drill_table.item(0, 0)
        ___qtablewidgetitem187.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem188 = self.hidraulic_drill_table.item(1, 0)
        ___qtablewidgetitem188.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem189 = self.hidraulic_drill_table.item(2, 0)
        ___qtablewidgetitem189.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem190 = self.hidraulic_drill_table.item(3, 0)
        ___qtablewidgetitem190.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem191 = self.hidraulic_drill_table.item(4, 0)
        ___qtablewidgetitem191.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem192 = self.hidraulic_drill_table.item(5, 0)
        ___qtablewidgetitem192.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem193 = self.hidraulic_drill_table.item(6, 0)
        ___qtablewidgetitem193.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem194 = self.hidraulic_drill_table.item(7, 0)
        ___qtablewidgetitem194.setText(QCoreApplication.translate("MainWindow", u"0", None));
        self.hidraulic_drill_table.setSortingEnabled(__sortingEnabled8)

        self.label_61.setText(QCoreApplication.translate("MainWindow", u"Limpieza de Pozo", None))
        ___qtablewidgetitem195 = self.clean_table.horizontalHeaderItem(0)
        ___qtablewidgetitem195.setText(QCoreApplication.translate("MainWindow", u"Values", None));
        ___qtablewidgetitem196 = self.clean_table.verticalHeaderItem(0)
        ___qtablewidgetitem196.setText(QCoreApplication.translate("MainWindow", u"Vab", None));
        ___qtablewidgetitem197 = self.clean_table.verticalHeaderItem(1)
        ___qtablewidgetitem197.setText(QCoreApplication.translate("MainWindow", u"beta", None));
        ___qtablewidgetitem198 = self.clean_table.verticalHeaderItem(2)
        ___qtablewidgetitem198.setText(QCoreApplication.translate("MainWindow", u"gama", None));
        ___qtablewidgetitem199 = self.clean_table.verticalHeaderItem(3)
        ___qtablewidgetitem199.setText(QCoreApplication.translate("MainWindow", u"Vs", None));
        ___qtablewidgetitem200 = self.clean_table.verticalHeaderItem(4)
        ___qtablewidgetitem200.setText(QCoreApplication.translate("MainWindow", u"NTP", None));
        ___qtablewidgetitem201 = self.clean_table.verticalHeaderItem(5)
        ___qtablewidgetitem201.setText(QCoreApplication.translate("MainWindow", u"ITT", None));
        ___qtablewidgetitem202 = self.clean_table.verticalHeaderItem(6)
        ___qtablewidgetitem202.setText(QCoreApplication.translate("MainWindow", u"NTE", None));
        ___qtablewidgetitem203 = self.clean_table.verticalHeaderItem(7)
        ___qtablewidgetitem203.setText(QCoreApplication.translate("MainWindow", u"Ca", None));
        ___qtablewidgetitem204 = self.clean_table.verticalHeaderItem(8)
        ___qtablewidgetitem204.setText(QCoreApplication.translate("MainWindow", u"Den Ca", None));
        ___qtablewidgetitem205 = self.clean_table.verticalHeaderItem(9)
        ___qtablewidgetitem205.setText(QCoreApplication.translate("MainWindow", u"nhb", None));
        ___qtablewidgetitem206 = self.clean_table.verticalHeaderItem(10)
        ___qtablewidgetitem206.setText(QCoreApplication.translate("MainWindow", u"khb", None));
        ___qtablewidgetitem207 = self.clean_table.verticalHeaderItem(11)
        ___qtablewidgetitem207.setText(QCoreApplication.translate("MainWindow", u"CCI", None));

        __sortingEnabled9 = self.clean_table.isSortingEnabled()
        self.clean_table.setSortingEnabled(False)
        ___qtablewidgetitem208 = self.clean_table.item(0, 0)
        ___qtablewidgetitem208.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem209 = self.clean_table.item(1, 0)
        ___qtablewidgetitem209.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem210 = self.clean_table.item(2, 0)
        ___qtablewidgetitem210.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem211 = self.clean_table.item(3, 0)
        ___qtablewidgetitem211.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem212 = self.clean_table.item(4, 0)
        ___qtablewidgetitem212.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem213 = self.clean_table.item(5, 0)
        ___qtablewidgetitem213.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem214 = self.clean_table.item(6, 0)
        ___qtablewidgetitem214.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem215 = self.clean_table.item(7, 0)
        ___qtablewidgetitem215.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem216 = self.clean_table.item(8, 0)
        ___qtablewidgetitem216.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem217 = self.clean_table.item(9, 0)
        ___qtablewidgetitem217.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem218 = self.clean_table.item(10, 0)
        ___qtablewidgetitem218.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem219 = self.clean_table.item(11, 0)
        ___qtablewidgetitem219.setText(QCoreApplication.translate("MainWindow", u"0", None));
        self.clean_table.setSortingEnabled(__sortingEnabled9)

        self.btn_calcular.setText(QCoreApplication.translate("MainWindow", u"Calcular", None))
        self.btn_limpiar.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"5", None))
    # retranslateUi

