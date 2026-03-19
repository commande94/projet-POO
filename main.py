from data import personnages_disponibles, monstres_disponibles, armes_disponibles, armes_monstres_disponibles, boss
from creatures import Personnage, Monstre
from combat import creer_combatants, lancer_initiatives, trier_initiative, afficher_ordre


def afficher_accueil():
    print("="*50)
    print("        RPG COMBAT SIMULATOR ")
    print("="*50)
    print("\nBienvenue Maître du Jeu !\n")
    print("Vous allez pouvoir créer votre équipe de héros,")
    print("sélectionner vos monstres et lancer le combat.")
    print("Chaque créature a ses points de vie, sa défense,")
    print("son type de dégâts et ses pouvoirs spéciaux.\n")
    print("="*50, "\n")


def afficher_heros():
    print("\nListe des héros disponibles :\n")
    for i, hero in enumerate(personnages_disponibles, 1):
        print(f"{i} - {hero['nom']} ({hero['pv']} PV) - {hero['description']}")

def afficher_monstres():
    print("\nListe des monstres disponibles :\n")
    for i, monstre in enumerate(monstres_disponibles, 1):
        print(f"{i} - {monstre['nom']} ({monstre['pv']} PV) - {monstre['description']}")

def selectionner_heros():
    equipe = []
    nombre = int(input("\nCombien de héros participent au combat ? (1-10) : "))
    for i in range(nombre):
        afficher_heros()
        choix = int(input(f"\nChoisir le héros {i+1} : "))
        data = personnages_disponibles[choix-1]
        equipe.append(Personnage(data['nom'], data['description'], data['pv'], data['defense'], data['type_degats']))
    return equipe

def selectionner_monstres():
    groupe = []
    nombre = int(input("\nCombien de monstres participent au combat ? : "))
    for i in range(nombre):
        afficher_monstres()
        choix = int(input(f"\nChoisir le monstre {i+1} : "))
        data = monstres_disponibles[choix-1]
        groupe.append(Monstre(data['nom'], data['description'], data['pv'], data['defense'], data['type_degats']))
    return groupe


def choisir_arme_libre(creature, est_monstre=False):
    """Permet au MJ de choisir n'importe quelle arme pour une créature."""
    if est_monstre:
        armes = armes_monstres_disponibles
    else:
        armes = armes_disponibles

    print(f"\n--- Toutes les armes disponibles pour {creature.nom} ---")
    for i, arme in enumerate(armes, 1):
        utilisateurs = ", ".join(arme["utilisateurs"])
        print(f"{i} - {arme['nom']} ({arme['degats']} | {arme['type']}) | Pour : {utilisateurs}")

    print(f"\nPersonnage : {creature.nom}")
    while True:
        try:
            choix = int(input("Choisir le numéro de l'arme à équiper : "))
            if 1 <= choix <= len(armes):
                creature.arme = armes[choix - 1]
                print(f"{creature.nom} équipé avec {creature.arme['nom']} !\n")
                break
            else:
                print(f"Veuillez entrer un nombre entre 1 et {len(armes)}.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")

def equiper_equipe_libre(equipe, est_monstre=False):
    """Permet au MJ de choisir librement une arme pour chaque créature."""
    for creature in equipe:
        choisir_arme_libre(creature, est_monstre)


def preparation_combat():
    print("\n--- Sélection des combattants ---")
    

    heros = selectionner_heros()
    monstres = selectionner_monstres()


    print("\n--- Héros sélectionnés ---")
    for h in heros:
        print(f"- {h.nom} ({h.pv_actuels} PV | Défense : {h.defense}) - {h.description}")

  
    print("\n--- Monstres sélectionnés ---")
    for m in monstres:
        print(f"- {m.nom} ({m.pv_actuels} PV | Défense : {m.defense}) - {m.description}")


    print("\n--- Choix des armes pour les héros ---")
    equiper_equipe_libre(heros)

    print("\n--- Choix des armes pour les monstres ---")
    equiper_equipe_libre(monstres, est_monstre=True)


    print("\n--- Choix d'arme pour le boss ---")
    boss_creature = Monstre(
        boss['nom'],
        boss['description'],
        boss['pv'],
        boss['defense'],
        boss['type_degats'],
        resistances=boss['resistances']
    )
    print(f"\nBoss sélectionné : {boss_creature.nom} ({boss_creature.pv_actuels} PV | Défense : {boss_creature.defense}) - {boss_creature.description}")
    choisir_arme_libre(boss_creature, est_monstre=True)

  
    print("\nÉquipe de héros prête :")
    for h in heros:
        print(f"- {h.nom} | Arme : {h.arme['nom']}")

    print("\nÉquipe de monstres prête :")
    for m in monstres:
        print(f"- {m.nom} | Arme : {m.arme['nom']}")

    print("\nBoss prêt :")
    print(f"- {boss_creature.nom} | Arme : {boss_creature.arme['nom']}")

    return heros, monstres, boss_creature

if __name__ == "__main__":
    afficher_accueil()
    heros, monstres, boss_creature = preparation_combat()
    combatants = creer_combatants(heros, monstres)
    lancer_initiatives(combatants)
    trier_initiative(combatants)
    afficher_ordre(combatants)