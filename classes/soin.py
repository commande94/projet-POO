class Soin(Action):
    def __init__(self):
        super().__init__("Soin")
    def executer(self, lanceur, cible):
        so = roll_dice(2, 8)
        cible.pv_actuels = min(cible.pv_actuels + so, cible.pv_max)
        print(f"💊 {lanceur.nom} soigne {cible.nom} de {so} points ({cible.pv_actuels}/{cible.pv_max})")