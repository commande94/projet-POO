from data import personnages_disponibles, monstres_disponibles
from creatures import Personnage, Monstre

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
    print("\nListe des monstres disponibles :")
    for i, monstre in enumerate(monstres_disponibles, 1):
        print(f"{i} - {monstre['nom']} ({monstre['pv']} PV) - {monstre['description']}")

def selectionner_heros():
    equipe = []
    nombre = int(input("\nCombien de héros participent au combat ? : "))
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

def preparation_combat():
    print("\n--- Sélection des combattants ---")
    heros = selectionner_heros()
    monstres = selectionner_monstres()

    print("\nL'Équipe de héros selectionnée est :")
    for h in heros:
        print("-", h.nom)

    print("\nL'Équipe de monstres selectionnée est :")
    for m in monstres:
        print("-", m.nom)

    return heros, monstres


if __name__ == "__main__":
    afficher_accueil()
    heros, monstres = preparation_combat()