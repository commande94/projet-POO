import random
import time
from data import boss
from creatures import Personnage, AttaqueSpeciale, Boss, Attaque, Vol, Chaos, LaPierre

class Arene:
    def __init__(self, nom, description, bonus=None, malus=None):
        self.nom = nom
        self.description = description
        self.bonus = bonus  
        self.malus = malus

def creer_combatants(heros, monstres):
    combatants = []
    combatants.extend(heros)
    combatants.extend(monstres)
    return combatants

def suspense_points():
    for _ in range(3):
        print(".", end="", flush=True)
        time.sleep(0.5)
    print()

def lancer_initiatives(combatants):
    print("\n--- Lancement des initiatives ---\n")
    time.sleep(2)

    for c in combatants:
        print(f"{c.nom} lance le dé", end="")
        suspense_points()
        print("🎲 Le dé roule", end="")
        suspense_points()
        time.sleep(0.5)
        c.initiative = random.randint(1, 20)
        print(f"👉 {c.nom} obtient {c.initiative} !\n")
        time.sleep(1)

def trier_initiative(combatants):
    combatants.sort(key=lambda c: c.initiative, reverse=True)

def afficher_ordre(combatants):
    print("\nCalcul de l'ordre de jeu", end="")
    suspense_points()
    time.sleep(1)
    print("\n===== ORDRE DE JEU =====\n")
    time.sleep(1)
    for i, c in enumerate(combatants):
        print(f"{i+1}. {c.nom} (initiative : {c.initiative})")
        time.sleep(0.8)

def choisir_cible(lanceur, allies, enemies, action):
    if isinstance(action, Attaque):
        pool = enemies
    else:  
        pool = allies
    pool = [c for c in pool if c.est_en_vie()]
    nouvelle_pool = []
    for c in pool:
        if isinstance(c, Boss):
            if hasattr(c, "en_pierre") and c.en_pierre:
                print(f"{c.nom} est en pierre ! {lanceur.nom} ne peut pas l'atteindre !")
                continue
            if hasattr(c, "en_vol") and c.en_vol:
                if hasattr(lanceur, "arme") and lanceur.arme.get("type") == "corps_a_corps":
                    print(f"{c.nom} est en vol ! {lanceur.nom} ne peut pas l'atteindre !")
                    continue
        nouvelle_pool.append(c)
    pool = nouvelle_pool
    if not pool:
        print("Aucune cible disponible !")
        return None
    for i, c in enumerate(pool, 1):
        print(f"{i}. {c.nom} ({c.pv_actuels}/{c.pv_max} PV)")
    while True:
        sel = input("Choisir la cible : ")
        if sel.isdigit():
            idx = int(sel) - 1
            if 0 <= idx < len(pool):
                return pool[idx]
        print("Sélection invalide")

def lancer_combat(heros, monstres, boss=None):
    arenes = [
        Arene("Forêt Dense", "Les arbres gênent les tirs", bonus="perçant"),
        Arene("Plaine Dégagée", "Parfait pour les attaques à distance", malus="perçant"),
        Arene("Grotte Souterraine", "Les sorts rebondissent", bonus="magique")
    ]
    arene = random.choice(arenes)
    print(f"\n🌍 Arène choisie : {arene.nom} - {arene.description}")
    combatants = creer_combatants(heros, monstres)
    lancer_initiatives(combatants)
    trier_initiative(combatants)
    afficher_ordre(combatants)
    tour_count = 0
    while any(h.est_en_vie() for h in heros) and (any(m.est_en_vie() for m in monstres) or (boss and boss.est_en_vie())):
        for c in combatants:
            if not c.est_en_vie():
                continue
            print(f"\n--- Tour de {c.nom} ---")
            for i, act in enumerate(c.actions, 1):
                print(f"{i}. {act.nom}")
            choix = None
            while choix is None:
                sel = input("Choisir action : ")
                if sel.isdigit():
                    idx = int(sel) - 1
                    if 0 <= idx < len(c.actions):
                        choix = c.actions[idx]
            cible = choisir_cible(
                c,
                heros if isinstance(c, Personnage) else monstres,
                (monstres + ([boss] if boss else [])) if isinstance(c, Personnage) else heros,
                choix
            )
            if isinstance(choix, AttaqueSpeciale):
                choix.executer(c, cible, arene, tour_actuel=tour_count)
            elif isinstance(choix, Attaque):
                choix.executer(c, cible, arene)
            else:
                choix.executer(c, cible)
            tour_count += 1
            if boss and tour_count % 5 == 0 and boss.est_en_vie():
                print(f"\n⚡ Le boss {boss.nom} intervient !")
                if boss.nom == "Seigneur Dragon" and not boss.en_vol:
                    print(f"{boss.nom} utilise son pouvoir spécial : Vol !")
                    Vol().executer(boss, None, arene)
                elif boss.nom == "Géant de Pierre":
                    print(f"{boss.nom} utilise son pouvoir spécial : Se transformer en pierre !")
                    LaPierre().executer(boss)
                elif boss.nom == "Démon du Chaos":
                    print(f"{boss.nom} utilise son pouvoir spécial : Chaos !")
                    Chaos().executer(boss, heros, arene)
                if boss.est_en_vie():
                    cible_boss = random.choice([h for h in heros if h.est_en_vie()])
                    degats = random.randint(*boss.degats)
                    print(f"{boss.nom} attaque {cible_boss.nom} !")
                    cible_boss.pv_actuels -= degats
                    print(f"{cible_boss.nom} subit {degats} dégâts ({cible_boss.pv_actuels}/{cible_boss.pv_max} PV)")
            if not any(h.est_en_vie() for h in heros):
                print("\n💀 Les héros ont été vaincus...")
                return False
            if not any(m.est_en_vie() for m in monstres) and (not boss or not boss.est_en_vie()):
                print("\n🏆 Les héros ont gagné !")
                return True
            
def preparer_boss():
    print("\n=== SÉLECTION DU BOSS ===")
    for i, b in enumerate(boss, 1):
        print(f"{i}. {b['nom']} ({b['pv']} PV, Défense: {b['defense']}) - {b['description']}")
    while True:
        choix = input("Quel boss voulez-vous affronter ? (1-3) : ")
        if choix.isdigit() and 1 <= int(choix) <= len(boss):
            data = boss[int(choix)-1]
            break
        print("Sélection invalide")
    boss = Boss(
        nom=data["nom"],
        description=data["description"],
        pv=data["pv"],
        defense=data["defense"],
        type_degats=data["type_degats"],
        resistances=data["resistances"],
        degats=data["degats"],
        peut_voler=data.get("peut_voler", False),
        chance_esquive=data.get("chance_esquive", 0.2)
    )
    print(f"\n👑 Boss choisi : {boss.nom} ({boss.pv_actuels}/{boss.pv_max} PV)")
    if boss.peut_voler:
        print(f"🦅 Peut voler - chance d'esquive {boss.chance_esquive*100}%")
    return boss