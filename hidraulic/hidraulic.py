from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox, QFileDialog

from menu_design import *
from utils import HidraulicFunctions


class Hidraulic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        # Signals
        self.btn_calcular.clicked.connect(self.getHidraulicValues)

    def getHidraulicValues(self):
        # Get values from UI
        mud_weight = self.mud_weight.value()
        solid_sg = self.solid_sg.value()
        plastic_viscosity = self.plastic_viscosity.value()
        yield_point = self.yield_point.value()
        gel_strength = self.gel_strength.value()
        bit_size = self.bit_size.value()
        open_hole_length = self.open_hole_length.value()
        casing_size = self.casing_size.value()
        casing_length = self.casing_length.value()
        drill_pipe_size = self.drill_pipe_size.value()
        drill_collar_size = self.drill_collar_size.value()
        drill_collar_length = self.drill_collar_length.value()
        pump_output = self.pump_output.value()
        pump_pressure = self.pump_pressure.value()
        surface_case = self.surface_case.value()
        rate_of_penetration = self.rate_of_penetration.value()
        density_of_particle = self.density_of_particle.value()
        diameter_of_particle = self.diameter_of_particle.value()
        fracture_gradient = self.fracture_gradient.value()
        prof_total = self.prof_total.value()
        l_300 = self.L_300.value()
        l_600 = self.l_600.value()

        # Psup
        p_sup = HidraulicFunctions.p_sup(surface_case, mud_weight, pump_output)
        self.p_sup.setValue(p_sup)

        # Drill Pipe Table
        vp1 = HidraulicFunctions.v_p1(pump_output, drill_pipe_size)
        np = HidraulicFunctions.np(l_600, l_300)
        kp = HidraulicFunctions.kp(l_600, np)
        visc_e1 = HidraulicFunctions.vis_e1(kp, vp1, drill_pipe_size, np)
        alfa = HidraulicFunctions.alfa(np)
        rep1 = HidraulicFunctions.rep1(vp1, drill_pipe_size, mud_weight, visc_e1, alfa)

        # Setting values into table
        self.drill_pipe_table.item(0, 0).setText(str(vp1))
        self.drill_pipe_table.item(1, 0).setText(str(np))
        self.drill_pipe_table.item(2, 0).setText(str(kp))
        self.drill_pipe_table.item(3, 0).setText(str(visc_e1))
        self.drill_pipe_table.item(4, 0).setText(str(alfa))
        self.drill_pipe_table.item(5, 0).setText(str(rep1))
