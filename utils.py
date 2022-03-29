class FluidFunctions:
    # Function to calculate velocity inside a pipeline
    def vel(Q, Di):
        """Returns velocity inside a pipeline with pipe flow and diameter as params"""
        V = round(24.5098 * Q / (pow(Di, 2)), 4)
        return V

    # Function to calculate Reynolds number
    def reynolds_number(pf, V, Di, mp):
        """Returns Reynolds Number"""
        Nre = round(129.0755 * (pf * V * Di / mp))
        return Nre

    # Function to calculate Hedstrom number
    def hedstrom_number(pf, ty, Di, mp):
        """Returns Hedstrom Number"""
        Nhe = round(309614.34 * (pf * ty * pow(Di, 2)) / pow(mp, 2), 4)
        return Nhe

    # Function to determine flow type
    def flow_type(Nre, NreC):
        return "Laminar" if Nre < NreC else "Turbulento"

    # Function to calculate Loss of pressure in drill pipeline, heavy weight and drill collar
    def delta_p_pipeline(V, mp, ty, Di, pf, Nre, flow):
        """Returns loss of pressure in drill pipeline, heavy weight and drill collar by its flow type"""
        if flow == "Laminar":
            deltaP = (V * mp / 27432 * pow(Di, 2)) + (ty / 68.58 * Di)
            return deltaP
        else:
            f = 0.079 / pow(Nre, 0.25)
            deltaP = round((f * pf * pow(V, 2)) / (3392.2668 * Di), 4)
            return deltaP

    # Function to calculate Presion Loss in Drill
    def delta_p_drill(a, Q, pf):
        """Returns loss of pressure in drill"""
        deltaPba = round((pow(Q, 2) * pf) / (1303 * pow(a, 2)), 4)
        return deltaPba

    # Function to calculate velocity in anular space
    def vel_anular_space(Q, d1, d2):
        """Returns velocity in anular space"""
        Vae = round(24.5098 * Q / (pow(d1, 2) - pow(d2, 2)), 4)
        return Vae

    # Function to calculate Reynolds number between pipelines
    def reynolds_number_pipelines(pf, vel, d1, d2, mp):
        """Returns reynolds number between two pipelnes"""
        Nre = round(105.2911 * ((pf * vel * (d1 - d2)) / mp), 4)
        return Nre

    # Function to calculate Hedstrom number between two pipelnes
    def hedstrom_number_pipelines(pf, ty, d1, d2, mp):
        """Returns hedstrom number between two pipelnes"""
        Nhe = round(206131.38 * ((pf * ty * pow(d1 - d2, 2)) / pow(mp, 2)), 4)
        return Nhe

    # Function to calculate loss of pressure between two pipelines
    def delta_p_two_pipelines(v, mp, d1, d2, ty, pf, flow, Nre):
        """Returns loss of pressure between two pipelines"""
        if flow == "Laminar":
            deltaP = round((v * mp / (18288 * pow(d1 - d2, 2))) + (ty / (60.96 * (d1 - d2))), 4)
            return deltaP
        else:
            f = 0.079 / pow(Nre, 0.25)
            deltaP = round((f * pf * pow(v, 2)) / (2774.2975 * (d1 - d2)), 4)
            return deltaP

    # Function to calculate equivalent density
    def equivalent_density(pf, pa, h):
        DEC = round(pf + ((0.704 * pa) / h), 4)
        return DEC
