from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QMessageBox

# Local files
from menu_design import *
from ui_Graph import Ui_Form
from utils import FluidFunctions


class DP_SubWindow(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class Density(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.dpSubwindow = DP_SubWindow()

        # Technical data:
        self.operationData = [
            ["DeDc", 8, "[pg]"],
            ["Dbna", 12.25, "[pg]"]
        ]

        self.drillData = [
            ["Tobera", 14, "[pg]"],
            ["Tobera", 12.415, "[pg]"]
        ]

        self.drillPipeline = [
            ["DiDc", 3, "98[m]"],
            ["DiHw", 3, "108[m]"],
            ["Tp", 5, "Ditp=4,276[pg]"],
            ["DiTp", 4.276, "[pg]"]
        ]

        # Signals
        self.NCRe.clicked.connect(self.showGraphWindow)
        self.Nhe.clicked.connect(self.getNheValue)
        self.DP.clicked.connect(self.getDeltaP)
        self.Dp_Clean.clicked.connect(self.cleanValues)


    def showGraphWindow(self):
        self.dpSubwindow.show()

    def getNheValue(self):
        pf = self.density.value()
        mp = self.mp.value()
        ty = self.Ty.value()
        try:
            if pf == 0 or mp == 0 or ty == 0:
                QMessageBox.information(self, "Error",
                                        "Todos los campos deben ser mayores a cero, revisa tu información")
            else:
                # NHe in Perforation Pipeline
                Ditp = self.drillPipeline[3][1]
                NheTp = FluidFunctions.hedstrom_number(pf, ty, Ditp, mp)

                # NHe in Heavy Weight
                Dihw = self.drillPipeline[1][1]
                NheHw = FluidFunctions.hedstrom_number(pf, ty, Dihw, mp)

                # NHe in Drill Collar
                Didc = self.drillPipeline[0][1]
                NheDc = FluidFunctions.hedstrom_number(pf, ty, Didc, mp)

                # Between Hole and Drill Collar
                DiAG = self.operationData[1][1]
                DeDc = self.operationData[0][1]
                NheHD = FluidFunctions.hedstrom_number_pipelines(pf, ty, DiAG, DeDc, mp)

                # Between Hole and Heavy Weight
                DeHw = self.drillPipeline[2][1]
                NheHHW = FluidFunctions.hedstrom_number_pipelines(pf, ty, DiAG, DeHw, mp)

                # Between Hole and Perforation Pipeline
                DeHw = self.drillPipeline[2][1]
                NheHP = FluidFunctions.hedstrom_number_pipelines(pf, ty, DiAG, DeHw, mp)

                # Between Drill Collar and Perforation Pipeline
                DiDD = self.drillData[1][1]
                DePP = self.drillPipeline[2][1]
                NheDP = FluidFunctions.hedstrom_number_pipelines(pf, ty, DiDD, DePP, mp)

                # set Nhe values into table
                self.Density_Table.item(0, 0).setText(str(NheTp))
                self.Density_Table.item(1, 0).setText(str(NheHw))
                self.Density_Table.item(2, 0).setText(str(NheDc))
                self.Density_Table.item(3, 0).setText(str(NheHD))
                self.Density_Table.item(4, 0).setText(str(NheHHW))
                self.Density_Table.item(5, 0).setText(str(NheHP))
                self.Density_Table.item(6, 0).setText(str(NheDP))
        except:
            QMessageBox.information(self, "Error", "Se ha presentado un error, revisa tu información")

    def getDeltaP(self):
        # get variable values
        pf = self.density.value()
        mp = self.mp.value()
        ty = self.Ty.value()
        Q = self.qFluid.value()
        e = 0.000053
        a = 0.9276

        try:
            if pf == 0 or mp == 0 or ty == 0:
                QMessageBox.information(self, "Error",
                                        "Todos los campos deben ser mayores a cero, revisa tu información")
            else:
                # Perforation Pipeline
                Ditp = self.drillPipeline[3][1]
                Vtp = FluidFunctions.vel(Q, Ditp)
                NreCTp = float(self.Density_Table.item(0, 1).text())
                NreTp = FluidFunctions.reynolds_number(pf, Vtp, Ditp, mp)
                FlowTypeTp = FluidFunctions.flow_type(NreTp, NreCTp)
                DeltaPTp = FluidFunctions.delta_p_pipeline(Vtp, mp, ty, Ditp, pf, NreTp, FlowTypeTp)
                DeltaPTpT = DeltaPTp * 5094

                # Heavy Weight
                Dihw = self.drillPipeline[1][1]
                Vhw = FluidFunctions.vel(Q, Dihw)
                NreCHw = float(self.Density_Table.item(1, 1).text())
                NreHw = FluidFunctions.reynolds_number(pf, Vhw, Dihw, mp)
                FlowTypeHw = FluidFunctions.flow_type(NreHw, NreCHw)
                DeltaPHw = FluidFunctions.delta_p_pipeline(Vhw, mp, ty, Dihw, pf, NreHw, FlowTypeHw)
                DeltaPHwT = DeltaPHw * 108

                # Drill Collar
                Didc = self.drillPipeline[0][1]
                Vdc = FluidFunctions.vel(Q, Didc)
                NreCDc = float(self.Density_Table.item(2, 1).text())
                NreDc = FluidFunctions.reynolds_number(pf, Vhw, Didc, mp)
                FlowTypeDc = FluidFunctions.flow_type(NreDc, NreCDc)
                DeltaPDc = FluidFunctions.delta_p_pipeline(Vdc, mp, ty, Didc, pf, NreDc, FlowTypeDc)
                DeltaPDcT = DeltaPDc * 98

                # Between Hole and Drill Collar
                DiAG = self.operationData[1][1]
                DeDc = self.operationData[0][1]
                VHD = FluidFunctions.vel_anular_space(Q, DiAG, DeDc)
                NreCHD = float(self.Density_Table.item(3, 1).text())
                NreHD = FluidFunctions.reynolds_number_pipelines(pf, VHD, DiAG, DeDc, mp)
                FlowTypeHD = FluidFunctions.flow_type(NreHD, NreCHD)
                DeltaPHD = FluidFunctions.delta_p_two_pipelines(VHD, mp, DiAG, DeDc, ty, pf, FlowTypeHD, NreHD)
                DeltaPHDT = round(98 * DeltaPHD, 4)

                # Between Hole and Heavy Weight
                DeHw = self.drillPipeline[2][1]
                VHW = FluidFunctions.vel_anular_space(Q, DiAG, DeHw)
                NreCHHW = float(self.Density_Table.item(4, 1).text())
                NreHHW = FluidFunctions.reynolds_number_pipelines(pf, VHW, DiAG, DeHw, mp)
                FlowTypeHHW = FluidFunctions.flow_type(NreHHW, NreCHHW)
                DeltaPHHW = FluidFunctions.delta_p_two_pipelines(VHW, mp, DiAG, DeHw, ty, pf, FlowTypeHHW, NreHHW)
                DeltaPHHWT = round(108 * DeltaPHHW, 4)

                # Between Hole and Perforation Pipeline
                DeHw = self.drillPipeline[2][1]
                VHP = FluidFunctions.vel_anular_space(Q, DiAG, DeHw)
                NreCHP = float(self.Density_Table.item(5, 1).text())
                NreHP = FluidFunctions.reynolds_number_pipelines(pf, VHP, DiAG, DeHw, mp)
                FlowTypeHP = FluidFunctions.flow_type(NreHP, NreCHP)
                DeltaPHP = FluidFunctions.delta_p_two_pipelines(VHP, mp, DiAG, DeHw, ty, pf, FlowTypeHP, NreHP)
                DeltaPHPT = round(1794 * DeltaPHP, 4)

                # Between Drill Collar and Perforation Pipeline
                DiDD = self.drillData[1][1]
                DePP = self.drillPipeline[2][1]
                VDP = FluidFunctions.vel_anular_space(Q, DiDD, DePP)
                NreCDP = float(self.Density_Table.item(6, 1).text())
                NreDP = FluidFunctions.reynolds_number_pipelines(pf, VDP, DiDD, DePP, mp)
                FlowTypeDP = FluidFunctions.flow_type(NreDP, NreCDP)
                DeltaPDP = FluidFunctions.delta_p_two_pipelines(VDP, mp, DiDD, DePP, ty, pf, FlowTypeDP, NreDP)
                DeltaPDPT = round(3300 * DeltaPDP, 4)

                # Superficial Equipment
                deltaPs = round(5.4595 * e * pow(pf, 0.8) * pow(Q, 1.8) * pow(mp, 0.2), 4)

                # Drill
                DeltaPD = FluidFunctions.delta_p_drill(a, Q, pf)

                # Delta P Total
                deltaPT = round(DeltaPHDT + DeltaPHHWT + DeltaPHPT + DeltaPDPT, 4)

                # Equivalent Density
                dec = FluidFunctions.equivalent_density(pf, deltaPT, 5300)

                # printing values in UI
                self.Density_Table.item(0, 2).setText(str(FlowTypeTp))
                self.Density_Table.item(0, 3).setText(str(DeltaPTpT))
                self.Density_Table.item(1, 2).setText(str(FlowTypeHw))
                self.Density_Table.item(1, 3).setText(str(DeltaPHwT))
                self.Density_Table.item(2, 2).setText(str(FlowTypeDc))
                self.Density_Table.item(2, 3).setText(str(DeltaPDcT))
                self.Density_Table.item(3, 2).setText(str(FlowTypeHD))
                self.Density_Table.item(3, 3).setText(str(DeltaPHDT))
                self.Density_Table.item(4, 2).setText(str(FlowTypeHHW))
                self.Density_Table.item(4, 3).setText(str(DeltaPHHWT))
                self.Density_Table.item(5, 2).setText(str(FlowTypeHP))
                self.Density_Table.item(5, 3).setText(str(DeltaPHPT))
                self.Density_Table.item(6, 2).setText(str(FlowTypeDP))
                self.Density_Table.item(6, 3).setText(str(DeltaPDPT))
                self.Dp_Superficial.setValue(deltaPs)
                self.Dp_Barrena.setValue(DeltaPD)
                self.Dp_Total.setValue(deltaPT)
                self.DEC.setValue(dec)
        except:
            QMessageBox.information(self, "Error", "Se ha presentado un error, revisa tu información")

    def cleanValues(self):
        # set null values for NHe
        self.Density_Table.item(0, 0).setText('')
        self.Density_Table.item(1, 0).setText('')
        self.Density_Table.item(2, 0).setText('')
        self.Density_Table.item(3, 0).setText('')
        self.Density_Table.item(4, 0).setText('')
        self.Density_Table.item(5, 0).setText('')
        self.Density_Table.item(6, 0).setText('')

        # set null values for DeltaP and Flujo
        self.Density_Table.item(0, 2).setText('')
        self.Density_Table.item(0, 3).setText('')
        self.Density_Table.item(1, 2).setText('')
        self.Density_Table.item(1, 3).setText('')
        self.Density_Table.item(2, 2).setText('')
        self.Density_Table.item(2, 3).setText('')
        self.Density_Table.item(3, 2).setText('')
        self.Density_Table.item(3, 3).setText('')
        self.Density_Table.item(4, 2).setText('')
        self.Density_Table.item(4, 3).setText('')
        self.Density_Table.item(5, 2).setText('')
        self.Density_Table.item(5, 3).setText('')
        self.Density_Table.item(6, 2).setText('')
        self.Density_Table.item(6, 3).setText('')

        # set null values for NCRe
        self.Density_Table.item(0, 1).setText('')
        self.Density_Table.item(1, 1).setText('')
        self.Density_Table.item(2, 1).setText('')
        self.Density_Table.item(3, 1).setText('')
        self.Density_Table.item(4, 1).setText('')
        self.Density_Table.item(5, 1).setText('')
        self.Density_Table.item(6, 1).setText('')

        self.Dp_Superficial.setValue(0)
        self.Dp_Barrena.setValue(0)
        self.Dp_Total.setValue(0)
        self.DEC.setValue(0)