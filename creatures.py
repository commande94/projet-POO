import random

# --- CLASSE MÈRE ---
class Creature:
    def __init__(self, nom, description, pv, defense, type_degats):
        self.nom = nom
        self.description = description
        self.pv_max = pv
        self.pv_actuels = pv
        self.defense = defense  # CA (Classe d'Armure)
        self.type_degats = type_degats
        self.initiative = 0
        self.actions = []  # Liste d'objets Action
        self.etats = []

    def lancer_initiative(self):
        """Détermine l'ordre de jeu avec un 1d20"""
        self.initiative = random.randint(1, 20)
        return self.initiative

    def est_en_vie(self):
        return self.pv_actuels > 0

# --- CLASSES FILLES ---
class Personnage(Creature):
    def __init__(self, nom, description, pv, defense, type_degats, arme):
        # Appel du constructeur parent
        super().__init__(nom, description, pv, defense, type_degats)
        self.arme = arme  # Instance d'une classe Arme
        self.inventaire = []

class Monstre(Creature):
    def __init__(self, nom, description, pv, defense, type_degats, resistances):
        super().__init__(nom, description, pv, defense, type_degats)
        self.resistances = resistances # Liste de types de dégâts

class Action:
    def __init__(self, nom):
        self.nom = nom

    def executer(self, lanceur, cible):
        # Cette méthode sera redéfinie dans les classes filles
        pass

class Attaque(Action):
    def executer(self, lanceur, cible):
        print(f"⚔️ {lanceur.nom} attaque {cible.nom} !")
        # 1. Jet de touche (1d20)
        jet_touche = random.randint(1, 20)
        
        # 2. Gestion des critiques
        if jet_touche == 20:
            print("✨ RÉUSSITE CRITIQUE !")
            # Logique de dégâts doublés
        elif jet_touche == 1:
            print("💀 ÉCHEC CRITIQUE !")
            # Logique de dégâts sur soi-même
        # ... suite de la logique de CA et dégâts