class Personnage(Creature):
    def __init__(self, nom, description, pv, defense, type_degats, arme):
        super().__init__(nom, description, pv, defense, type_degats)
        self.arme = arme
        self.inventaire = []
        self.actions.append(Attaque())
        self.actions.append(Soin())
        self.actions.append(Buff())