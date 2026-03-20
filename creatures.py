import random
from data import *

class Action:
    def __init__(self, nom): self.nom = nom
    def executer(self, lanceur, cible, arene=None): pass

class Attaque(Action):
    def __init__(self): super().__init__("Attaque")
    def executer(self, lanceur, cible, arene=None):
        print(f"\n⚔️ {lanceur.nom} attaque {cible.nom}")
        jet = random.randint(1,20)
        bonus = 0
        if arene and lanceur.type_degats == arene.bonus: bonus = 2
        if arene and lanceur.type_degats == arene.malus: bonus = -2
        jet += bonus
        if bonus>0: print(f"✨ Bonus de l'arène +{bonus}")
        elif bonus<0: print(f"❌ Malus de l'arène {bonus}")
        print(f"Jet: {jet} vs Défense {cible.defense}")
        if jet > cible.defense:
            nb,f = map(int, lanceur.arme["degats"].split("d"))
            degats = sum(random.randint(1,f) for _ in range(nb))
            if hasattr(cible,"resistances") and lanceur.type_degats in cible.resistances:
                degats//=2
                print("Résistance détectée, dégâts divisés par 2")
            cible.pv_actuels -= degats
            print(f"💥 {cible.nom} subit {degats} dégâts ({cible.pv_actuels}/{cible.pv_max} PV)")
        else:
            print("❌ Manqué !")

class Soin(Action):
    def __init__(self): super().__init__("Soin")
    def executer(self, lanceur, cible, arene=None):
        soin = random.randint(1,8)+random.randint(1,8)
        cible.pv_actuels = min(cible.pv_max, cible.pv_actuels+soin)
        print(f"💊 {lanceur.nom} soigne {cible.nom} de {soin} ({cible.pv_actuels}/{cible.pv_max})")

class Buff(Action):
    def __init__(self):
        super().__init__("Buff")
    
    def executer(self, lanceur, cible):
        bonus = 2
        cible.defense += bonus
        cible.etats.append(f"def+{bonus}")
        print(f"💪 {lanceur.nom} augmente la défense de {cible.nom} de {bonus} (défense = {cible.defense})")


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
    def est_en_vie(self): return self.pv_actuels>0
    def lancer_initiative(self):
        self.initiative = random.randint(1, 20)
        print(f"{self.nom} lance l'initiative : {self.initiative}")
        return self.initiative

    def est_en_vie(self):
        return self.pv_actuels > 0
            
class Personnage(Creature):
    def __init__(self, nom, description, pv, defense, type_degats, arme):
        super().__init__(nom, description, pv, defense, type_degats)
        self.arme = arme
        self.inventaire = []
        self.actions = [Attaque(), Soin(), Buff()]


class Monstre(Creature):
    def __init__(self, nom, description, pv, defense, type_degats, degats, resistances=None):
        super().__init__(nom, description, pv, defense, type_degats)
        self.degats = degats
        self.resistances = resistances if resistances else []  
        self.actions = [Attaque(), Soin(), Buff()]

class Boss(Creature):
    def __init__(self, nom, description, pv, defense, type_degats, resistances, degats, peut_voler=False, chance_esquive=0.2):
        super().__init__(nom, description, pv, defense, type_degats)
        self.resistances = resistances if resistances else []
        self.degats = degats
        self.peut_voler = peut_voler
        self.actions = [Attaque(), Soin(), Buff()]
        self.chance_esquive = chance_esquive if peut_voler else 0

    def peut_esquiver(self):
        return self.peut_voler and random.random() < self.chance_esquive