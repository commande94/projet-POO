import random

class Creature:
    def __init__(self, nom, description, pv, defense, type_degats):
        self.nom = nom
        self.description = description
        self.pv_max = pv
        self.pv_actuels = pv
        self.defense = defense
        self.type_degats = type_degats
        self.initiative = 0
        self.actions = []
        self.etats = []

    def lancer_initiative(self):
        self.initiative = random.randint(1, 20)
        print(f"{self.nom} lance l'initiative : {self.initiative}")
        return self.initiative

    def est_en_vie(self):
        return self.pv_actuels > 0

class Personnage(Creature):
    def __init__(self, nom, description, pv, defense, type_degats, arme=None):
        super().__init__(nom, description, pv, defense, type_degats)
        self.arme = arme
        self.inventaire = []

class Monstre(Creature):
    def __init__(self, nom, description, pv, defense, type_degats, resistances=None):
        super().__init__(nom, description, pv, defense, type_degats)
        self.resistances = resistances if resistances else []