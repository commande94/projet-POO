import random
import time


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