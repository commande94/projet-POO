class Monstre(Creature):
    def __init__(self, nom, description, pv, defense, type_degats, resistances, degats):
        super().__init__(nom, description, pv, defense, type_degats)
        self.resistances = resistances
        self.degats = degats
        self.actions.append(Attaque())
        self.actions.append(Soin())
        self.actions.append(Buff())