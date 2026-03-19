class Buff(Action):
    def __init__(self):
        super().__init__("Buff")
    def executer(self, lanceur, cible):
        bonus = 2
        cible.defense += bonus
        cible.etats.append(f"def+{bonus}")
        print(f"💪 {lanceur.nom} augmente la défense de {cible.nom} de {bonus} (défense = {cible.defense})")