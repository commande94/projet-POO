import random
from data import *

class Action:
    def __init__(self, nom):
        if not isinstance(nom, str):
            raise ValueError(f"Nom d'action invalide : {nom}")
        self.nom = nom

    def executer(self, lanceur, cible, arene=None):
        pass

class Attaque(Action):
    def __init__(self):
        super().__init__("Attaque")

    def executer(self, lanceur, cible, arene=None):
        if not cible or not cible.est_en_vie():
            print(f"❌ {lanceur.nom} ne peut pas attaquer une cible invalide !\n")
            return
        print(f"\n⚔️ {lanceur.nom} attaque {cible.nom} ! 💥")
        jet = random.randint(1, 20)
        bonus = 0
        if arene and lanceur.type_degats == arene.bonus: bonus = 2
        if arene and lanceur.type_degats == arene.malus: bonus = -2
        jet += bonus
        if bonus > 0: print(f"✨ Bonus de l'arène +{bonus}")
        elif bonus < 0: print(f"❌ Malus de l'arène {bonus}")
        print(f"🎯 Jet: {jet} vs Défense {cible.defense}")
        if jet > cible.defense:
            try:
                nb, f = map(int, lanceur.arme["degats"].split("d"))
                degats = sum(random.randint(1, f) for _ in range(nb))
            except Exception:
                degats = 1
                print("⚠️ Dégâts par défaut = 1")
            if hasattr(cible,"resistances") and lanceur.type_degats in cible.resistances:
                degats //= 2
                print("🛡️ Résistance détectée, dégâts divisés par 2")
            cible.pv_actuels = max(0, cible.pv_actuels - degats)
            print(f"💥 {cible.nom} subit {degats} dégâts ! ({cible.pv_actuels}/{cible.pv_max} PV)\n")
        else:
            print("❌ Manqué ! 🙈\n")

class Soin(Action):
    def __init__(self):
        super().__init__("Soin")

    def executer(self, lanceur, cible, arene=None):
        if not cible or not cible.est_en_vie():
            print(f"❌ {lanceur.nom} ne peut pas soigner une cible invalide ! 💊\n")
            return
        soin = random.randint(1,8) + random.randint(1,8)
        cible.pv_actuels = min(cible.pv_max, cible.pv_actuels + soin)
        print(f"💊 {lanceur.nom} soigne {cible.nom} de {soin} PV ! ({cible.pv_actuels}/{cible.pv_max})\n")

class AttaqueSpeciale(Action):
    def __init__(self, nom="Attaque Spéciale"):
        super().__init__(nom)
        self.cooldown = 3
        self.dernier_tour_utilisation = -self.cooldown

    def executer(self, lanceur, cible, arene=None, tour_actuel=0):
        if tour_actuel - self.dernier_tour_utilisation < self.cooldown:
            tours_restants = self.cooldown - (tour_actuel - self.dernier_tour_utilisation)
            print(f"❌ {self.nom} indisponible ! ({tours_restants} tour(s) restant(s))\n")
            return False
        if not cible or not cible.est_en_vie():
            print(f"❌ Cible invalide pour l'attaque spéciale de {lanceur.nom} 💥\n")
            return False
        try:
            nb, f = map(int, lanceur.arme["degats"].split("d"))
            degats = sum(random.randint(1, f) for _ in range(nb)) + 5
        except Exception:
            degats = 5
            print("⚠️ Dégâts spéciaux par défaut = 5")
        bonus = 0
        if arene and lanceur.type_degats == arene.bonus: bonus = 2
        if arene and lanceur.type_degats == arene.malus: bonus = -2
        degats += bonus
        if bonus > 0: print(f"✨ Bonus arène +{bonus}")
        elif bonus < 0: print(f"❌ Malus arène {bonus}")
        if hasattr(cible, "resistances") and lanceur.type_degats in cible.resistances:
            degats //= 2
            print("🛡️ Résistance détectée, dégâts divisés par 2")
        cible.pv_actuels = max(0, cible.pv_actuels - degats)
        print(f"💥 {lanceur.nom} utilise {self.nom} sur {cible.nom} et inflige {degats} dégâts ! ({cible.pv_actuels}/{cible.pv_max} PV)\n")
        self.dernier_tour_utilisation = tour_actuel
        return True

class Buff(Action):
    def __init__(self):
        super().__init__("Buff")
    
    def executer(self, lanceur, cible):
        if not cible or not cible.est_en_vie():
            print(f"❌ Cible invalide pour le Buff de {lanceur.nom} 💪\n")
            return
        bonus = 2
        cible.defense += bonus
        cible.etats.append(f"def+{bonus}")
        print(f"💪 {lanceur.nom} augmente la défense de {cible.nom} de {bonus} (défense = {cible.defense})\n")

class Vol(Action):
    def __init__(self):
        super().__init__("Vol")
    
    def executer(self, lanceur, cible, arene=None):
        if not hasattr(lanceur, "en_vol"):
            lanceur.en_vol = False
        if not lanceur.en_vol:
            lanceur.en_vol = True
            print(f"🦅 {lanceur.nom} s'envole dans les airs ! Certaines attaques au corps à corps ne peuvent plus l'atteindre.\n")
        else:
            if not cible or not cible.est_en_vie():
                print(f"❌ Cible invalide pour l'attaque aérienne de {lanceur.nom} 💥\n")
                return
            try:
                nb, f = map(int, lanceur.degats)
                degats = sum(random.randint(1, f) for _ in range(nb))
            except Exception:
                degats = 1
            bonus = 0
            if arene and lanceur.type_degats == arene.bonus: bonus = 2
            if arene and lanceur.type_degats == arene.malus: bonus = -2
            degats += bonus
            if bonus > 0: print(f"✨ Bonus arène +{bonus}")
            elif bonus < 0: print(f"❌ Malus arène {bonus}")
            if hasattr(cible, "resistances") and lanceur.type_degats in cible.resistances:
                degats //= 2
            cible.pv_actuels = max(0, cible.pv_actuels - degats)
            print(f"💥 {lanceur.nom} attaque {cible.nom} depuis les airs et inflige {degats} dégâts ! ({cible.pv_actuels}/{cible.pv_max} PV)\n")

class LaPierre(Action):
    def __init__(self):
        super().__init__("Se transformer en pierre")
    
    def executer(self, lanceur, cible=None, arene=None):
        lanceur.en_pierre = not getattr(lanceur, "en_pierre", False)
        if lanceur.en_pierre:
            print(f"🪨 {lanceur.nom} se transforme en pierre et devient presque invincible !\n")
        else:
            print(f"🪨 {lanceur.nom} reprend sa forme normale et peut être attaqué à nouveau.\n")

    @staticmethod
    def peut_etre_touche(lanceur, attaquant):
        if getattr(lanceur, "en_pierre", False):
            print(f"🪨 {lanceur.nom} est en pierre ! {attaquant.nom} ne peut pas l'atteindre !\n")
            return False
        return True

class Chaos(Action):
    def __init__(self):
        super().__init__("Pouvoir du Chaos")
    
    def executer(self, lanceur, allies, arene=None):
        print(f"\n💀 {lanceur.nom} invoque le chaos ! 🔥")
        for cible in allies:
            if not cible.est_en_vie(): continue
            try:
                dmg = random.randint(*lanceur.degats)
            except Exception:
                dmg = 1
            effet = random.choice(["degats", "malus_defense", "malus_initiative"])
            if effet == "degats":
                cible.pv_actuels = max(0, cible.pv_actuels - dmg)
                print(f"{cible.nom} subit {dmg} dégâts du chaos ! ({cible.pv_actuels}/{cible.pv_max} PV)")
            elif effet == "malus_defense":
                cible.defense = max(0, cible.defense - 2)
                print(f"{cible.nom} voit sa défense réduite de 2 ! (défense = {cible.defense})")
            elif effet == "malus_initiative":
                cible.initiative = max(0, cible.initiative - 2)
                print(f"{cible.nom} voit son initiative réduite de 2 ! (initiative = {cible.initiative})\n")

class Creature:
    def __init__(self, nom, description, pv, defense, type_degats):
        if not isinstance(nom, str): nom = "Créature inconnue"
        if not isinstance(description, str): description = ""
        if not isinstance(pv, int) or pv <= 0: pv = 1
        if not isinstance(defense, int) or defense < 0: defense = 0
        if not isinstance(type_degats, str): type_degats = "physique"

        self.nom = nom
        self.description = description
        self.pv_max = pv
        self.pv_actuels = pv
        self.defense = defense
        self.type_degats = type_degats
        self.initiative = 0
        self.actions = []
        self.etats = []
        self.en_vol = False
        self.en_pierre = False

    def est_en_vie(self): return self.pv_actuels > 0

    def subir_degats(self, montant):
        if not isinstance(montant, int): return
        self.pv_actuels = max(0, self.pv_actuels - montant)

    def soigner(self, montant):
        if not isinstance(montant, int): return
        self.pv_actuels = min(self.pv_max, self.pv_actuels + montant)

    def lancer_initiative(self):
        self.initiative = random.randint(1, 20)
        print(f"🎲 {self.nom} lance l'initiative : {self.initiative}")
        return self.initiative

class Personnage(Creature):
    def __init__(self, nom, description, pv, defense, type_degats, arme):
        super().__init__(nom, description, pv, defense, type_degats)
        self.arme = arme if isinstance(arme, dict) else {"degats":"1d4"}
        self.inventaire = []
        self.actions = [Attaque(), Soin(), Buff(), AttaqueSpeciale()]

class Monstre(Creature):
    def __init__(self, nom, description, pv, defense, type_degats, degats, resistances=None):
        super().__init__(nom, description, pv, defense, type_degats)
        self.degats = degats if isinstance(degats, tuple) else (1,1)
        self.resistances = resistances if isinstance(resistances, list) else []
        self.actions = [Attaque(), Soin(), Buff()]

class Boss(Creature):
    def __init__(self, nom, description, pv, defense, type_degats, resistances, degats, peut_voler=False, chance_esquive=0.2):
        super().__init__(nom, description, pv, defense, type_degats)
        self.resistances = resistances if isinstance(resistances, list) else []
        self.degats = degats if isinstance(degats, tuple) else (1,1)
        self.peut_voler = bool(peut_voler)
        self.en_vol = False
        self.en_pierre = False
        self.actions = [Attaque(), Soin(), Buff(), Vol(), LaPierre(), Chaos()]
        self.chance_esquive = chance_esquive if peut_voler else 0

    def peut_esquiver(self):
        return self.peut_voler and random.random() < self.chance_esquive