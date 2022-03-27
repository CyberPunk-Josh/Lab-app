from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox, QAbstractItemView
from PySide6.QtSql import QSqlDatabase, QSqlTableModel
from PySide6.QtCore import Qt
import pyqtgraph as pg
import sys

# Local files
from menu_design import *


class RModelDB(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        # Connection to Database:
        server = 'LAPTOP-2OCJA2M7\SQLEXPRESS'
        database = 'LabFluidos'
        driver = 'ODBC Driver 17 for SQL Server'

        dbDB = QSqlDatabase.addDatabase('QODBC')
        dbDB.setDatabaseName(f"Driver={driver};Server={server};Database={database};Trusted_Connection=yes;")
        if not dbDB.open():
            print("Cannot connect to the database")
            sys.exit(True)

        # Structure of objects for records
        self.recordsDB = [
            {"name": "Modelo 1", "valuesX": [], "valuesY": [], "color": "green", "symbol": "o", "VA": 0, "VP": 0,
             "PC": 0, "Temperatura": "23 [ºC]", "tethaValues": []},
            {"name": "Modelo 2", "valuesX": [], "valuesY": [], "color": "blue", "symbol": "o", "VA": 0, "VP": 0,
             "PC": 0, "Temperatura": "60 [ºC]", "tethaValues": []},
            {"name": "Modelo 3", "valuesX": [], "valuesY": [], "color": "pink", "symbol": "o", "VA": 0, "VP": 0,
             "PC": 0, "Temperatura": "65 [ºC]", "tethaValues": []},
            {"name": "Modelo 4", "valuesX": [], "valuesY": [], "color": "red", "symbol": "o", "VA": 0, "VP": 0,
             "PC": 0, "Temperatura": "70 [ºC]", "tethaValues": []},
            {"name": "Modelo 5", "valuesX": [], "valuesY": [], "color": "brown", "symbol": "o", "VA": 0, "VP": 0,
             "PC": 0, "Temperatura": "82 [ºC]", "tethaValues": []}
        ]

        # Adding object's name to comboBox
        for record in self.recordsDB:
            self.RM_ComboBoxBD.addItem(record["name"] + " " + record["Temperatura"])

        # Build Grafics in UI:
        self.build_graphics()

        # Creating the model
        self.modelDB = QSqlTableModel()
        self.modelDB.setTable("RegistroViscosimetro")
        self.modelDB.select()
        self.modelDB.setHeaderData(0, Qt.Horizontal, "Id")

        # Configuring table
        self.RM_TvDB.setModel(self.modelDB)
        # hidding first column
        self.RM_TvDB.setColumnHidden(0, True)

        # not editing table
        self.RM_TvDB.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # select row
        self.RM_TvDB.setSelectionMode(QAbstractItemView.SingleSelection)
        self.RM_TvDB.setSelectionBehavior(QAbstractItemView.SelectRows)

        # signals
        self.RM_TvDB.selectionModel().selectionChanged.connect(self.selectRow)
        self.RM_GraphDB.clicked.connect(self.getReologicalValuesDB)
        self.RM_ComboBoxBD.currentTextChanged.connect(self.comboChangedDB)
        self.RM_DeleteDB.clicked.connect(self.deleteRecordDB)
        self.RM_UpdateDB.clicked.connect(self.updateRecordDB)

        self.rowDB = -1

    def build_graphics(self):
        self.RM_WidgetDB.addLegend()
        self.RM_WidgetDB.setBackground("w")
        self.graphicsDB = []
        for record in self.recordsDB:
            plotDB = self.RM_WidgetDB.plot(record["valuesX"], record["valuesY"], name=record["Temperatura"],
                                           pen=pg.mkPen(record["color"], width=3), symbol=record["symbol"])
            self.graphicsDB.append(plotDB)
        self.RM_WidgetDB.showGrid(x=True, y=True)
        self.RM_WidgetDB.setTitle("Modelo Reològico", sizer="24px")
        styles = {"color": "#000", "font-size": "20px"}
        self.RM_WidgetDB.setLabel("left", "t [Dinas/cm2]", **styles)
        self.RM_WidgetDB.setLabel("bottom", "y [seg-1]", **styles)

    def selectRow(self, selection):
        if selection.indexes():
            self.rowDB = selection.indexes()[0].row()
            # getting values of records in sqlSERVER
            rpm3 = str(self.modelDB.index(self.rowDB, 1).data())
            rpm6 = str(self.modelDB.index(self.rowDB, 2).data())
            rpm100 = str(self.modelDB.index(self.rowDB, 3).data())
            rpm200 = str(self.modelDB.index(self.rowDB, 4).data())
            rpm300 = str(self.modelDB.index(self.rowDB, 5).data())
            rpm600 = str(self.modelDB.index(self.rowDB, 6).data())

            # setting values into table in UI
            self.RM_TableWidgetDB.item(0, 1).setText(rpm3)
            self.RM_TableWidgetDB.item(1, 1).setText(rpm6)
            self.RM_TableWidgetDB.item(2, 1).setText(rpm100)
            self.RM_TableWidgetDB.item(3, 1).setText(rpm200)
            self.RM_TableWidgetDB.item(4, 1).setText(rpm300)
            self.RM_TableWidgetDB.item(5, 1).setText(rpm600)

    def getReologicalValuesDB(self):
        try:
            # getting values from tBLE IN ui
            valuesInXDB = [
                int(self.RM_TableWidgetDB.item(0, 0).text()),
                int(self.RM_TableWidgetDB.item(1, 0).text()),
                int(self.RM_TableWidgetDB.item(2, 0).text()),
                int(self.RM_TableWidgetDB.item(3, 0).text()),
                int(self.RM_TableWidgetDB.item(4, 0).text()),
                int(self.RM_TableWidgetDB.item(5, 0).text())
            ]

            valuesInYDB = [
                float(self.RM_TableWidgetDB.item(0, 1).text()),
                float(self.RM_TableWidgetDB.item(1, 1).text()),
                float(self.RM_TableWidgetDB.item(2, 1).text()),
                float(self.RM_TableWidgetDB.item(3, 1).text()),
                float(self.RM_TableWidgetDB.item(4, 1).text()),
                float(self.RM_TableWidgetDB.item(5, 1).text())
            ]

            indexDB = self.RM_ComboBoxBD.currentIndex()

            for value in valuesInXDB:
                self.recordsDB[indexDB]["valuesX"].append(round(value * 1.703, 3))
            for value in valuesInYDB:
                self.recordsDB[indexDB]["tethaValues"].append(value)
                self.recordsDB[indexDB]["valuesY"].append(round(value * 5.1109, 3))

            # CALCULATING REOLOGICAL VALUES
            VADB = round(float(self.RM_TableWidgetDB.item(5, 1).text()) / 2, 2)
            VPDB = round(
                float(self.RM_TableWidgetDB.item(5, 1).text()) - float(self.RM_TableWidgetDB.item(4, 1).text()), 2)
            PCDB = round(float(self.RM_TableWidgetDB.item(4, 1).text()) - VPDB, 2)

            # ADDING REOLOGICAL DATA TO OBJECT
            self.recordsDB[indexDB]["VA"] = VADB
            self.recordsDB[indexDB]["VP"] = VPDB
            self.recordsDB[indexDB]["PC"] = PCDB

            # ADDING REOLOGICAL DATA TO INPUTS IN UI
            self.RM_VaDB.setValue(self.recordsDB[indexDB]["VA"])
            self.RM_VpDB.setValue(self.recordsDB[indexDB]["VP"])
            self.RM_PcDB.setValue(self.recordsDB[indexDB]["PC"])

            # adding values into graph and updating graphics
            self.graphicsDB[indexDB].setData(self.recordsDB[indexDB]["valuesX"], self.recordsDB[indexDB]["valuesY"])
        except:
            QMessageBox.information(self, "Error", "Todos los campos son obligatorios, revisa tu informarción")

    def comboChangedDB(self):
        indexDB = self.RM_ComboBoxBD.currentIndex()
        if len(self.recordsDB[indexDB]["tethaValues"]) > 0:
            self.RM_TableWidgetDB.item(0, 1).setText(str(self.recordsDB[indexDB]["tethaValues"][0]))
            self.RM_TableWidgetDB.item(1, 1).setText(str(self.recordsDB[indexDB]["tethaValues"][1]))
            self.RM_TableWidgetDB.item(2, 1).setText(str(self.recordsDB[indexDB]["tethaValues"][2]))
            self.RM_TableWidgetDB.item(3, 1).setText(str(self.recordsDB[indexDB]["tethaValues"][3]))
            self.RM_TableWidgetDB.item(4, 1).setText(str(self.recordsDB[indexDB]["tethaValues"][4]))
            self.RM_TableWidgetDB.item(5, 1).setText(str(self.recordsDB[indexDB]["tethaValues"][5]))
            self.RM_VaDB.setValue(self.recordsDB[indexDB]["VA"])
            self.RM_VpDB.setValue(self.recordsDB[indexDB]["VP"])
            self.RM_PcDB.setValue(self.recordsDB[indexDB]["PC"])
        else:
            self.RM_TableWidgetDB.item(0, 1).setText("")
            self.RM_TableWidgetDB.item(1, 1).setText("")
            self.RM_TableWidgetDB.item(2, 1).setText("")
            self.RM_TableWidgetDB.item(3, 1).setText("")
            self.RM_TableWidgetDB.item(4, 1).setText("")
            self.RM_TableWidgetDB.item(5, 1).setText("")
            self.RM_VaDB.setValue(0)
            self.RM_VpDB.setValue(0)
            self.RM_PcDB.setValue(0)

    def deleteRecordDB(self):
        try:
            if self.rowDB >= 0:
                self.modelDB.removeRow(self.rowDB)
                self.modelDB.select()
                self.rowDB = -1
                self.RM_TableWidgetDB.item(0, 1).setText("")
                self.RM_TableWidgetDB.item(1, 1).setText("")
                self.RM_TableWidgetDB.item(2, 1).setText("")
                self.RM_TableWidgetDB.item(3, 1).setText("")
                self.RM_TableWidgetDB.item(4, 1).setText("")
                self.RM_TableWidgetDB.item(5, 1).setText("")
                self.RM_VaDB.setValue(0)
                self.RM_VpDB.setValue(0)
                self.RM_PcDB.setValue(0)
        except:
            QMessageBox.information(self, "Error", "No se ha podido eliminar el registro")

    def updateRecordDB(self):
        self.modelDB.select()
