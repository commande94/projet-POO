import random
from data import personnages_disponibles, monstres_disponibles, armes_disponibles, boss_disponibles


class Action:
    def __init__(self, nom):
        self.nom = nom
    def executer(self, lanceur, cible):
        pass

class Attaque(Action):
    def __init__(self):
        super().__init__("Attaque")
    def executer(self, lanceur, cible, arene=None):  # Ajout du paramètre arene
        print(f"⚔️ {lanceur.nom} attaque {cible.nom} !")
        
        # Vérifier si le boss esquive
        if isinstance(cible, Boss) and cible.peut_esquiver():
            print(f"🦅 {cible.nom} esquive l'attaque en volant !")
            return
        
        jet = random.randint(1, 20)
        
        # Application des bonus/malus de l'arène
        if arene:
            bonus = arene.appliquer_bonus(lanceur)
            malus = arene.appliquer_malus(lanceur)
            jet += bonus + malus
            if bonus > 0:
                print(f"✨ L'arène donne un bonus de {bonus} à {lanceur.nom} !")
            if malus < 0:
                print(f"🌧️ L'arène donne un malus de {malus} à {lanceur.nom} !")
        
        print(f"Jet de touche : {jet} (défense cible {cible.defense})")
        if jet == 1:
            print("💀 Échec critique !")
            dmg = roll_dice(*get_degat_dice(lanceur))
            print(f"{lanceur.nom} s'inflige {dmg} dégâts.")
            lanceur.pv_actuels -= dmg
        elif jet > cible.defense:
            crit = jet == 20
            if crit:
                print("✨ Réussite critique ! dégâts doublés")
            dmg = roll_dice(*get_degat_dice(lanceur))
            if crit:
                dmg *= 2
            if hasattr(cible, "resistances") and lanceur.type_degats in cible.resistances:
                dmg = dmg // 2
                print("Résistance détectée, dégâts divisés par 2")
            cible.pv_actuels -= dmg
            print(f"{cible.nom} subit {dmg} dégâts ({cible.pv_actuels}/{cible.pv_max} PV restants)")
        else:
            print("Manqué !")


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
    def lancer_initiative(self):
        self.initiative = random.randint(1, 20)
        return self.initiative
    def est_en_vie(self):
        return self.pv_actuels > 0

# === CLASSE BOSS (déplacée APRÈS Creature) ===
class Boss(Creature):
    def __init__(self, nom, description, pv, defense, type_degats, resistances, degats, peut_voler=False, chance_esquive=0.2):
        super().__init__(nom, description, pv, defense, type_degats)
        self.resistances = resistances
        self.degats = degats
        self.peut_voler = peut_voler
        self.chance_esquive = chance_esquive if peut_voler else 0
        self.actions.append(Attaque())
        self.actions.append(Soin())
        self.actions.append(Buff())
    
    def peut_esquiver(self):
        return self.peut_voler and random.random() < self.chance_esquive
    
class Monstre(Creature):
    def __init__(self, nom, description, pv, defense, type_degats, resistances, degats):
        super().__init__(nom, description, pv, defense, type_degats)
        self.resistances = resistances
        self.degats = degats
        self.actions.append(Attaque())
        self.actions.append(Soin())
        self.actions.append(Buff())

class Personnage(Creature):
    def __init__(self, nom, description, pv, defense, type_degats, arme):
        super().__init__(nom, description, pv, defense, type_degats)
        self.arme = arme
        self.inventaire = []
        self.actions.append(Attaque())
        self.actions.append(Soin())
        self.actions.append(Buff())

class Soin(Action):
    def __init__(self):
        super().__init__("Soin")
    def executer(self, lanceur, cible):
        so = roll_dice(2, 8)
        cible.pv_actuels = min(cible.pv_actuels + so, cible.pv_max)
        print(f"💊 {lanceur.nom} soigne {cible.nom} de {so} points ({cible.pv_actuels}/{cible.pv_max})")

# === CLASSE ARÈNE ===
class Arene:
    def __init__(self, nom, description, bonus_type=None, malus_type=None):
        self.nom = nom
        self.description = description
        self.bonus_type = bonus_type  # Type d'attaque bonus
        self.malus_type = malus_type   # Type d'attaque malus
    
    def appliquer_bonus(self, attaquant):
        if self.bonus_type and attaquant.type_degats == self.bonus_type:
            return 2  # Bonus de +2 au jet
        return 0
    
    def appliquer_malus(self, attaquant):
        if self.malus_type and attaquant.type_degats == self.malus_type:
            return -2  # Malus de -2 au jet
        return 0

def afficher_accueil():
    print("🌌" * 25)
    print("        RPG COMBAT SIMULATOR")
    print("🌌" * 25 + "\n")
    
    print("🔥 Bienvenue, Maître du Jeu !\n")
    print("⚔️ Préparez vos héros courageux,")
    print("👹 Sélectionnez des monstres redoutables,")
    print("🏰 Lancez des combats épiques et légendaires !\n")
    print("💥 Chaque créature a ses forces, faiblesses et pouvoirs spéciaux")
    print("🌈 Que le destin guide vos héros vers la victoire !\n")
    print("🌌" * 25 + "\n")

def roll_dice(nb, faces):
    return sum(random.randint(1, faces) for _ in range(nb))

def get_degat_dice(creature):
    if isinstance(creature, Personnage):
        return creature.arme["degats"]
    else:
        return getattr(creature, "degats", (1, 6))

def demander_nombre(msg):
    while True:
        try:
            n = int(input(msg))
            if n >= 0:
                return n
        except:
            pass

def choisir_element(liste, avec_description=True):
    for i, obj in enumerate(liste, 1):
        if avec_description:
            print(f"{i}. {obj['nom']} - {obj.get('description','')}")
        else:
            print(f"{i}. {obj['nom']}")
    while True:
        sel = input("Choix : ")
        if sel.isdigit():
            idx = int(sel) - 1
            if 0 <= idx < len(liste):
                return liste[idx]
        print("Sélection invalide")

def preparer_equipe():
    pers = []
    compt = demander_nombre("Combien de personnages ? ")
    for _ in range(compt):
        base = choisir_element(personnages_disponibles)
        arme = choisir_element(armes_disponibles, avec_description=False)
        p = Personnage(base["nom"], base["description"], base["pv"], base["defense"], base["type_degats"], arme)
        if input("Modifier PV du personnage ? (o/n) ").lower() == "o":
            pv = demander_nombre("Nouveaux PV max : ")
            p.pv_max = pv
            p.pv_actuels = pv
        pers.append(p)
    return pers

def preparer_monstres():
    mons = []
    compt = demander_nombre("Combien de monstres ? ")
    for _ in range(compt):
        base = choisir_element(monstres_disponibles)
        m = Monstre(base["nom"], base["description"], base["pv"], base["defense"], base["type_degats"], base["resistances"], base["degats"])
        mons.append(m)
    return mons

# === NOUVELLE FONCTION POUR PRÉPARER LE BOSS ===
def preparer_boss():
    print("\n=== SÉLECTION DU BOSS ===")
    base = choisir_element(boss_disponibles)
    
    boss = Boss(
        base["nom"],
        base["description"],
        base["pv"],
        base["defense"],
        base["type_degats"],
        base["resistances"],
        base["degats"],
        base.get("peut_voler", False),
        base.get("chance_esquive", 0.2)
    )
    
    print(f"\n👑 BOSS: {boss.nom}")
    if boss.peut_voler:
        print(f"🦅 Peut voler - {boss.chance_esquive*100}% de chance d'esquiver")
    return boss

# === NOUVELLE FONCTION POUR CHOISIR L'ARÈNE ===
def choisir_arene():
    print("\n=== CHOIX DE L'ARÈNE ===")
    arenes = [
        Arene("Forêt Dense", "Une forêt sombre où les arbres gênent les tirs", "perçant", None),
        Arene("Plaine Dégagée", "Une vaste plaine parfaite pour les tirs à distance", None, "perçant"),
        Arene("Grotte Souterraine", "Une grotte étroite où les sorts rebondissent", "magique", None)
    ]
    
    for i, arene in enumerate(arenes, 1):
        print(f"{i}. {arene.nom}")
        print(f"   {arene.description}")
        if arene.bonus_type:
            print(f"   ✅ Bonus: attaques {arene.bonus_type}")
        if arene.malus_type:
            print(f"   ❌ Malus: attaques {arene.malus_type}")
        print()
    
    while True:
        choix = input("Choisissez votre arène (1-3) : ")
        if choix.isdigit():
            idx = int(choix) - 1
            if 0 <= idx < len(arenes):
                return arenes[idx]
        print("Choix invalide")

def choisir_cible(action, lanceur, allies, enemies):
    if isinstance(action, Attaque):
        pool = enemies if isinstance(lanceur, Personnage) else allies
    elif isinstance(action, Soin) or isinstance(action, Buff):
        pool = allies if isinstance(lanceur, Personnage) else enemies
    else:
        pool = allies + enemies
    pool = [c for c in pool if c.est_en_vie()]
    for i, c in enumerate(pool, 1):
        volant = "🦅 " if hasattr(c, "peut_voler") and c.peut_voler else ""
        print(f"{i}. {volant}{c.nom} ({c.pv_actuels}/{c.pv_max} PV)")
    idx = None
    while idx is None:
        sel = input("Cible : ")
        if sel.isdigit():
            i = int(sel) - 1
            if 0 <= i < len(pool):
                idx = i
        if idx is None:
            print("Option invalide")
    return pool[idx]

# === MODIFICATION DE LA FONCTION LANCER_COMBAT ===
def lancer_combat(heros, monstres, arene=None, est_boss=False):
    tous = heros + monstres
    for c in tous:
        c.lancer_initiative()
    ordre = sorted(tous, key=lambda x: x.initiative, reverse=True)
    
    if arene:
        print(f"\n🌍 Combat dans: {arene.nom}")
    
    while any(h.est_en_vie() for h in heros) and any(m.est_en_vie() for m in monstres):
        for c in ordre:
            if not c.est_en_vie():
                continue
            print(f"\n--- Tour de {c.nom} ---")
            for idx, act in enumerate(c.actions, 1):
                print(f"{idx}. {act.nom}")
            choix = None
            while choix is None:
                sel = input("Action : ")
                if sel.isdigit():
                    i = int(sel) - 1
                    if 0 <= i < len(c.actions):
                        choix = c.actions[i]
                if choix is None:
                    print("Option invalide")
            cible = choisir_cible(choix, c, heros, monstres)
            # Passer l'arène à l'attaque
            if isinstance(choix, Attaque):
                choix.executer(c, cible, arene)
            else:
                choix.executer(c, cible)
            if not any(m.est_en_vie() for m in monstres) or not any(h.est_en_vie() for h in heros):
                break
    
    if any(h.est_en_vie() for h in heros):
        if est_boss:
            print("\n🏆 VICTOIRE ÉPIQUE ! Le boss est vaincu !")
        else:
            print("\n🏆 Les héros ont gagné !")
        return True
    else:
        if est_boss:
            print("\n💀 DÉFAITE... Le boss a triomphé...")
        else:
            print("\n💀 Les monstres ont vaincu...")
        return False

# === MAIN ===
if __name__ == "__main__":
    afficher_accueil()
    
    # Demander si on veut un boss
    choix_boss = input("Voulez-vous affronter un BOSS ? (o/n) : ").lower()
    
    if choix_boss == 'o':
        # Mode boss
        heros = preparer_equipe()
        boss = [preparer_boss()]  # Un seul boss dans une liste
        arene = choisir_arene()
        lancer_combat(heros, boss, arene, est_boss=True)
    else:
        # Mode normal
        heros = preparer_equipe()
        monstres = preparer_monstres()
        lancer_combat(heros, monstres)