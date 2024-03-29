from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox, QFileDialog

from menu_design import *
from utils import HidraulicFunctions, AugerHydraulics, WellCleaning


class Hidraulic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        # Signals
        self.btn_calcular.clicked.connect(self.getHidraulicValues)
        self.btn_limpiar.clicked.connect(self.clearAllValues)

    def getHidraulicValues(self):
        # Get values from UI
        mud_weight = self.mud_weight.value()
        solid_sg = self.solid_sg.value()
        plastic_viscosity = self.plastic_viscosity.value()
        yield_point = self.yield_point.value()
        gel_strength = self.gel_strength.value()
        bit_size = self.bit_size.value()
        bit_size_alt = self.bit_size_alt.value()
        open_hole_length = self.open_hole_length.value()
        casing_size = self.casing_size.value()
        casing_size_alt = self.casing_size_alt.value()
        casing_length = self.casing_length.value()
        casing_length_alt = self.casing_length_alt.value()
        drill_pipe_size = self.drill_pipe_size.value()
        drill_pipe_size_alt = self.drill_pipe_size_alt.value()
        drill_collar_size = self.drill_collar_size.value()
        drill_collar_size_alt = self.drill_collar_size_alt.value()
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
        rel = HidraulicFunctions.re_l(np)
        ret = HidraulicFunctions.re_t(np)
        fp1 = HidraulicFunctions.fp_1(np, rep1)
        p_pipe = HidraulicFunctions.p_pipe(fp1, vp1, mud_weight, drill_pipe_size, prof_total, drill_collar_length)

        # Setting values into  drill pipe table
        self.drill_pipe_table.item(0, 0).setText(str(vp1))
        self.drill_pipe_table.item(1, 0).setText(str(np))
        self.drill_pipe_table.item(2, 0).setText(str(kp))
        self.drill_pipe_table.item(3, 0).setText(str(visc_e1))
        self.drill_pipe_table.item(4, 0).setText(str(alfa))
        self.drill_pipe_table.item(5, 0).setText(str(rep1))
        self.drill_pipe_table.item(6, 0).setText(str(rel))
        self.drill_pipe_table.item(7, 0).setText(str(ret))
        self.drill_pipe_table.item(8, 0).setText(str(fp1))
        self.drill_pipe_table.item(9, 0).setText(str(p_pipe))

        # Drill Collar Table
        vp2 = HidraulicFunctions.v_p1(pump_output, drill_collar_size)
        np2 = HidraulicFunctions.np(l_600, l_300)
        kp2 = HidraulicFunctions.kp(l_600, np2)
        visc_e2 = HidraulicFunctions.vis_e1(kp2, vp2, drill_collar_size, np2)
        alfa2 = HidraulicFunctions.alfa(np2)
        rep2 = HidraulicFunctions.rep1(vp2, drill_collar_size, mud_weight, visc_e2, alfa2)
        rel2 = HidraulicFunctions.re_l(np2)
        ret2 = HidraulicFunctions.re_t(np2)
        fp2 = HidraulicFunctions.fp_1(np2, rep2)
        p_pipe2 = HidraulicFunctions.p_pipe_collar(fp2, vp2, mud_weight, drill_collar_size, drill_collar_length)

        # Setting values into  drill collar table
        self.drill_collar_table.item(0, 0).setText(str(vp2))
        self.drill_collar_table.item(1, 0).setText(str(np2))
        self.drill_collar_table.item(2, 0).setText(str(kp2))
        self.drill_collar_table.item(3, 0).setText(str(visc_e2))
        self.drill_collar_table.item(4, 0).setText(str(alfa2))
        self.drill_collar_table.item(5, 0).setText(str(rep2))
        self.drill_collar_table.item(6, 0).setText(str(rel2))
        self.drill_collar_table.item(7, 0).setText(str(ret2))
        self.drill_collar_table.item(8, 0).setText(str(fp2))
        self.drill_collar_table.item(9, 0).setText(str(p_pipe2))

        # Sarta
        p_sarta = HidraulicFunctions.sarta(p_pipe, p_pipe2)
        self.sarta.setValue(p_sarta)

        # Dj
        dj = HidraulicFunctions.dj(bit_size_alt)
        self.dj.setValue(dj)

        # Barrena
        barrena = HidraulicFunctions.barrena(pump_output, mud_weight, dj)
        self.barrena.setValue(barrena)

        # Pipe / Casing Table
        va1 = HidraulicFunctions.va1(pump_output, casing_size, drill_pipe_size_alt)
        na = HidraulicFunctions.na(l_300, gel_strength)
        ka = HidraulicFunctions.ka(l_300, na)
        visea = HidraulicFunctions.visea(ka, va1, casing_size, drill_pipe_size_alt, na)
        beta = HidraulicFunctions.beta(na)
        rea = HidraulicFunctions.rea(va1, casing_size, drill_pipe_size_alt, mud_weight, visea, beta)
        rela = HidraulicFunctions.rela(na)
        reta = HidraulicFunctions.reta(na)
        fa = HidraulicFunctions.fa(rea)
        pa = HidraulicFunctions.pa(fa, va1, mud_weight, casing_size, drill_pipe_size_alt, casing_length_alt)

        # Setting values into Pipe / Casing table
        self.pipe_casing_table.item(0, 0).setText(str(va1))
        self.pipe_casing_table.item(1, 0).setText(str(na))
        self.pipe_casing_table.item(2, 0).setText(str(ka))
        self.pipe_casing_table.item(3, 0).setText(str(visea))
        self.pipe_casing_table.item(4, 0).setText(str(beta))
        self.pipe_casing_table.item(5, 0).setText(str(rea))
        self.pipe_casing_table.item(6, 0).setText(str(rela))
        self.pipe_casing_table.item(7, 0).setText(str(reta))
        self.pipe_casing_table.item(8, 0).setText(str(fa))
        self.pipe_casing_table.item(9, 0).setText(str(pa))

        # Pipe / Open Hole
        va2 = HidraulicFunctions.va1(pump_output, bit_size, drill_pipe_size_alt)
        na2 = HidraulicFunctions.na(l_300, gel_strength)
        ka2 = HidraulicFunctions.ka(l_300, na2)
        visea2 = HidraulicFunctions.visea(ka2, va2, bit_size, drill_pipe_size_alt, na2)
        beta2 = HidraulicFunctions.beta(na2)
        rea2 = HidraulicFunctions.rea(va2, bit_size, drill_pipe_size_alt, mud_weight, visea2, beta2)
        rela2 = HidraulicFunctions.rela(na2)
        reta2 = HidraulicFunctions.reta(na2)
        fa2 = HidraulicFunctions.fa(rea2)
        pa2 = HidraulicFunctions.pa2(fa2, va2, mud_weight, bit_size, drill_pipe_size_alt,
                                     open_hole_length, drill_collar_length)

        # Setting values into Pipe / Open Hole table
        self.pipe_open_table.item(0, 0).setText(str(va2))
        self.pipe_open_table.item(1, 0).setText(str(na2))
        self.pipe_open_table.item(2, 0).setText(str(ka2))
        self.pipe_open_table.item(3, 0).setText(str(visea2))
        self.pipe_open_table.item(4, 0).setText(str(beta2))
        self.pipe_open_table.item(5, 0).setText(str(rea2))
        self.pipe_open_table.item(6, 0).setText(str(rela2))
        self.pipe_open_table.item(7, 0).setText(str(reta2))
        self.pipe_open_table.item(8, 0).setText(str(fa2))
        self.pipe_open_table.item(9, 0).setText(str(pa2))

        # Drill Collar / Open Hole
        va3 = HidraulicFunctions.va1(pump_output, bit_size, drill_collar_size_alt)
        na3 = HidraulicFunctions.na(l_300, gel_strength)
        ka3 = HidraulicFunctions.ka(l_300, na)
        visea3 = HidraulicFunctions.visea(ka3, va3, bit_size, drill_collar_size_alt, na3)
        beta3 = HidraulicFunctions.beta(na3)
        rea3 = HidraulicFunctions.rea(va3, bit_size, drill_collar_size_alt, mud_weight, visea3, beta3)
        rela3 = HidraulicFunctions.rela(na3)
        reta3 = HidraulicFunctions.reta(na3)
        fa3 = HidraulicFunctions.fa(rea3)
        pa3 = HidraulicFunctions.pa(fa3, va3, mud_weight, bit_size, drill_collar_size_alt, drill_collar_length)

        # Setting values into Drill Collar / Open Hole
        self.drill_collar_open_table.item(0, 0).setText(str(va3))
        self.drill_collar_open_table.item(1, 0).setText(str(na3))
        self.drill_collar_open_table.item(2, 0).setText(str(ka3))
        self.drill_collar_open_table.item(3, 0).setText(str(visea3))
        self.drill_collar_open_table.item(4, 0).setText(str(beta3))
        self.drill_collar_open_table.item(5, 0).setText(str(rea3))
        self.drill_collar_open_table.item(6, 0).setText(str(rela3))
        self.drill_collar_open_table.item(7, 0).setText(str(reta3))
        self.drill_collar_open_table.item(8, 0).setText(str(fa3))
        self.drill_collar_open_table.item(9, 0).setText(str(pa3))

        # Anular
        anular = HidraulicFunctions.anular(pa, pa2, pa3)
        self.anular.setValue(anular)

        # ECD
        ecd = HidraulicFunctions.ecd(anular, casing_length, mud_weight)
        self.ecd.setValue(ecd)

        # PTotal
        ptotal = HidraulicFunctions.pTotal(p_sup, p_sarta, barrena, anular)
        self.p_total.setValue(ptotal)

        # Hidraulica Barrena
        vab = AugerHydraulics.vab(pump_output, bit_size, drill_pipe_size_alt)
        hhpb = AugerHydraulics.hhpb(pump_output, barrena)
        hhpbpg2 = AugerHydraulics.hhpbpg2(hhpb, bit_size)
        psib_value = AugerHydraulics.psib(barrena, pump_pressure)
        syshhp = AugerHydraulics.syshhp(pump_pressure, pump_output)
        vn = AugerHydraulics.vn(pump_output, dj)
        iefe = AugerHydraulics.iefe(mud_weight, vn, pump_output)
        iefepg = AugerHydraulics.iefepg(iefe, bit_size)

        # Setting values into  Auger Hidraulics table
        self.hidraulic_drill_table.item(0, 0).setText(str(vab))
        self.hidraulic_drill_table.item(1, 0).setText(str(hhpb))
        self.hidraulic_drill_table.item(2, 0).setText(str(hhpbpg2))
        self.hidraulic_drill_table.item(3, 0).setText(str(psib_value))
        self.hidraulic_drill_table.item(4, 0).setText(str(syshhp))
        self.hidraulic_drill_table.item(5, 0).setText(str(vn))
        self.hidraulic_drill_table.item(6, 0).setText(str(iefe))
        self.hidraulic_drill_table.item(7, 0).setText(str(iefepg))

        # Well Cleaning
        vab_well = WellCleaning.vab(pump_output, bit_size, drill_pipe_size_alt)
        beta_well = WellCleaning.beta(plastic_viscosity, mud_weight, diameter_of_particle)
        gamma_well = WellCleaning.gamma(beta_well, diameter_of_particle, density_of_particle, mud_weight)
        vs_well = WellCleaning.vs(beta_well, gamma_well)
        npt_well = WellCleaning.npt(vab_well, vs_well)
        itt_well = WellCleaning.itt(casing_length_alt, npt_well)
        nte_well = WellCleaning.nte(npt_well, vab_well)
        ca_well = WellCleaning.ca(bit_size, rate_of_penetration, pump_output, nte_well)
        denca_well = WellCleaning.denca(solid_sg, ca_well, mud_weight)
        nhb_well = WellCleaning.nhb(l_600, l_300)
        khb_well = WellCleaning.khb(l_300, nhb_well)
        cci_well = WellCleaning.cci(mud_weight, khb_well, vab_well)

        # Setting values into Well Cleaning
        self.clean_table.item(0, 0).setText(str(vab_well))
        self.clean_table.item(1, 0).setText(str(beta_well))
        self.clean_table.item(2, 0).setText(str(gamma_well))
        self.clean_table.item(3, 0).setText(str(vs_well))
        self.clean_table.item(4, 0).setText(str(npt_well))
        self.clean_table.item(5, 0).setText(str(itt_well))
        self.clean_table.item(6, 0).setText(str(nte_well))
        self.clean_table.item(7, 0).setText(str(ca_well))
        self.clean_table.item(8, 0).setText(str(denca_well))
        self.clean_table.item(9, 0).setText(str(nhb_well))
        self.clean_table.item(10, 0).setText(str(khb_well))
        self.clean_table.item(11, 0).setText(str(cci_well))


    def clearAllValues(self):
        # Clear values in drill pipe table
        self.drill_pipe_table.item(0, 0).setText('')
        self.drill_pipe_table.item(1, 0).setText('')
        self.drill_pipe_table.item(2, 0).setText('')
        self.drill_pipe_table.item(3, 0).setText('')
        self.drill_pipe_table.item(4, 0).setText('')
        self.drill_pipe_table.item(5, 0).setText('')
        self.drill_pipe_table.item(6, 0).setText('')
        self.drill_pipe_table.item(7, 0).setText('')
        self.drill_pipe_table.item(8, 0).setText('')
        self.drill_pipe_table.item(9, 0).setText('')

        # Setting values into  drill collar table
        self.drill_collar_table.item(0, 0).setText('')
        self.drill_collar_table.item(1, 0).setText('')
        self.drill_collar_table.item(2, 0).setText('')
        self.drill_collar_table.item(3, 0).setText('')
        self.drill_collar_table.item(4, 0).setText('')
        self.drill_collar_table.item(5, 0).setText('')
        self.drill_collar_table.item(6, 0).setText('')
        self.drill_collar_table.item(7, 0).setText('')
        self.drill_collar_table.item(8, 0).setText('')
        self.drill_collar_table.item(9, 0).setText('')

        self.sarta.setValue(0)
        self.dj.setValue(0)
        self.barrena.setValue(0)

        # Clear values in Pipe / Casing table
        self.pipe_casing_table.item(0, 0).setText('')
        self.pipe_casing_table.item(1, 0).setText('')
        self.pipe_casing_table.item(2, 0).setText('')
        self.pipe_casing_table.item(3, 0).setText('')
        self.pipe_casing_table.item(4, 0).setText('')
        self.pipe_casing_table.item(5, 0).setText('')
        self.pipe_casing_table.item(6, 0).setText('')
        self.pipe_casing_table.item(7, 0).setText('')
        self.pipe_casing_table.item(8, 0).setText('')
        self.pipe_casing_table.item(9, 0).setText('')

        # Clear values into Pipe / Open Hole table
        self.pipe_open_table.item(0, 0).setText('')
        self.pipe_open_table.item(1, 0).setText('')
        self.pipe_open_table.item(2, 0).setText('')
        self.pipe_open_table.item(3, 0).setText('')
        self.pipe_open_table.item(4, 0).setText('')
        self.pipe_open_table.item(5, 0).setText('')
        self.pipe_open_table.item(6, 0).setText('')
        self.pipe_open_table.item(7, 0).setText('')
        self.pipe_open_table.item(8, 0).setText('')
        self.pipe_open_table.item(9, 0).setText('')

        # Clear values in Drill Collar / Open Hole
        self.drill_collar_open_table.item(0, 0).setText('')
        self.drill_collar_open_table.item(1, 0).setText('')
        self.drill_collar_open_table.item(2, 0).setText('')
        self.drill_collar_open_table.item(3, 0).setText('')
        self.drill_collar_open_table.item(4, 0).setText('')
        self.drill_collar_open_table.item(5, 0).setText('')
        self.drill_collar_open_table.item(6, 0).setText('')
        self.drill_collar_open_table.item(7, 0).setText('')
        self.drill_collar_open_table.item(8, 0).setText('')
        self.drill_collar_open_table.item(9, 0).setText('')

        self.anular.setValue(0)
        self.ecd.setValue(0)
        self.p_total.setValue(0)
        self.p_sup.setValue(0)

        self.hidraulic_drill_table.item(0, 0).setText('')
        self.hidraulic_drill_table.item(1, 0).setText('')
        self.hidraulic_drill_table.item(2, 0).setText('')
        self.hidraulic_drill_table.item(3, 0).setText('')
        self.hidraulic_drill_table.item(4, 0).setText('')
        self.hidraulic_drill_table.item(5, 0).setText('')
        self.hidraulic_drill_table.item(6, 0).setText('')
        self.hidraulic_drill_table.item(7, 0).setText('')

        # Setting values into Well Cleaning
        self.clean_table.item(0, 0).setText('')
        self.clean_table.item(1, 0).setText('')
        self.clean_table.item(2, 0).setText('')
        self.clean_table.item(3, 0).setText('')
        self.clean_table.item(4, 0).setText('')
        self.clean_table.item(5, 0).setText('')
        self.clean_table.item(6, 0).setText('')
        self.clean_table.item(7, 0).setText('')
        self.clean_table.item(8, 0).setText('')
        self.clean_table.item(9, 0).setText('')
        self.clean_table.item(10, 0).setText('')
        self.clean_table.item(11, 0).setText('')
