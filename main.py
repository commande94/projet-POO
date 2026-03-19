import random
from data import personnages_disponibles, monstres_disponibles, armes_disponibles

def afficher_accueil():
    print("="*50)
    print("      🛡️ RPG COMBAT SIMULATOR 🐉")
    print("="*50)
    print("\nBienvenue Maître du Jeu !\n")
    print("Vous allez pouvoir créer votre équipe de héros,")
    print("sélectionner vos monstres et lancer le combat.")
    print("Chaque créature a ses points de vie, sa défense,")
    print("son type de dégâts et ses pouvoirs spéciaux.\n")
    print("="*50, "\n")

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

def choisir_element(liste):
    for i, obj in enumerate(liste, 1):
        print(f"{i}. {obj['nom']} - {obj.get('description','')}")
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
        arme = choisir_element(armes_disponibles)
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

def choisir_cible(action, lanceur, allies, enemies):
    if isinstance(action, Attaque):
        pool = enemies if isinstance(lanceur, Personnage) else allies
    elif isinstance(action, Soin) or isinstance(action, Buff):
        pool = allies if isinstance(lanceur, Personnage) else enemies
    else:
        pool = allies + enemies
    pool = [c for c in pool if c.est_en_vie()]
    for i, c in enumerate(pool, 1):
        print(f"{i}. {c.nom} ({c.pv_actuels}/{c.pv_max} PV)")
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

def lancer_combat(heros, monstres):
    tous = heros + monstres
    for c in tous:
        c.lancer_initiative()
    ordre = sorted(tous, key=lambda x: x.initiative, reverse=True)
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
            choix.executer(c, cible)
            if not any(m.est_en_vie() for m in monstres) or not any(h.est_en_vie() for h in heros):
                break
    if any(h.est_en_vie() for h in heros):
        print("\n🏆 Les héros ont gagné !")
    else:
        print("\n💀 Les monstres ont vaincu...")

if __name__ == "__main__":
    afficher_accueil()
    heros = preparer_equipe()
    monstres = preparer_monstres()
    lancer_combat(heros, monstres)