from data import personnages_disponibles, monstres_disponibles, armes_disponibles, armes_monstres_disponibles, boss
from creatures import Personnage, Monstre, Boss, Vol, LaPierre, Chaos
from combat import creer_combatants, lancer_combat

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

def afficher_heros():
    print("\nHéros disponibles :\n")
    for i, hero in enumerate(personnages_disponibles, 1):
        print(f"{i} - {hero['nom']} {hero['pv']} PV | {hero['description']}")
    print("\n")

def afficher_monstres():
    print("\nMonstres disponibles :\n")
    for i, monstre in enumerate(monstres_disponibles, 1):
        print(f"{i} - {monstre['nom']} {monstre['pv']} PV | {monstre['description']}")
    print("\n")

def selectionner_heros():
    equipe = []
    while True:
        try:
            nombre = int(input("\nCombien de héros participent au combat ? (1-10) : "))
            if 1 <= nombre <= 10:
                break
            print("❌ Veuillez entrer un nombre entre 1 et 10.\n")
        except ValueError:
            print("❌ Entrée invalide. Veuillez entrer un chiffre.\n")
    
    for i in range(nombre):
        afficher_heros()
        while True:
            try:
                choix = int(input(f"Choisissez le héros {i+1} : "))
                if 1 <= choix <= len(personnages_disponibles):
                    data = personnages_disponibles[choix-1]
                    equipe.append(Personnage(
                        data['nom'], data['description'], data['pv'],
                        data['defense'], data['type_degats'], arme=None
                    ))
                    print(f"✅ {data['nom']} rejoint votre équipe !\n")
                    break
                print(f"⚠️ Choix invalide. Sélectionnez un numéro entre 1 et {len(personnages_disponibles)}.\n")
            except ValueError:
                print("❌ Entrée invalide. Veuillez entrer un chiffre.\n")
    return equipe

def selectionner_monstres():
    groupe = []
    while True:
        try:
            nombre = int(input("\nCombien de monstres attaqueront vos héros ? (1-10) : "))
            if 1 <= nombre <= 10:
                break
            print("❌ Veuillez entrer un nombre entre 1 et 10.\n")
        except ValueError:
            print("❌ Entrée invalide. Veuillez entrer un chiffre.\n")
    
    for i in range(nombre):
        afficher_monstres()
        while True:
            try:
                choix = int(input(f"Choisissez le monstre {i+1} : "))
                if 1 <= choix <= len(monstres_disponibles):
                    data = monstres_disponibles[choix-1]
                    groupe.append(Monstre(
                        data['nom'], data['description'], data['pv'],
                        data['defense'], data['type_degats'], degats=(1,6), resistances=[]
                    ))
                    print(f"{data['nom']} est prêt pour le combat !\n")
                    break
                print(f"⚠️ Numéro invalide. Choisissez entre 1 et {len(monstres_disponibles)}.\n")
            except ValueError:
                print("❌ Entrée invalide. Veuillez entrer un chiffre.\n")
    return groupe

def selectionner_boss():
    print("\nSélection du Boss :\n")
    for i, b in enumerate(boss, 1):
        print(f"{i}. {b['nom']} {b['pv']} PV | Défense : {b['defense']} | {b['description']}\n")
    
    while True:
        choix = input("Quel boss souhaitez-vous affronter ? (1-3) : ")
        if choix.isdigit() and 1 <= int(choix) <= len(boss):
            data = boss[int(choix)-1]
            break
        print("❌ Sélection invalide, veuillez entrer un numéro valide.\n")
    
    boss_creature = Boss(
        nom=data["nom"], description=data["description"], pv=data["pv"],
        defense=data["defense"], type_degats=data["type_degats"],
        resistances=data.get("resistances", []),
        degats=data.get("degats", (2,8)),
        peut_voler=data.get("peut_voler", False),
        chance_esquive=data.get("chance_esquive", 0.2)
    )
    boss_creature.en_vol = False
    boss_creature.en_pierre = False
    if data["nom"] == "Seigneur Dragon": boss_creature.actions.append(Vol())
    elif data["nom"] == "Géant de Pierre": boss_creature.actions.append(LaPierre())
    elif data["nom"] == "Démon du Chaos": boss_creature.actions.append(Chaos())
    
    print(f"\nLe boss {boss_creature.nom} est prêt ! ({boss_creature.pv_actuels}/{boss_creature.pv_max} PV)\n")
    return boss_creature

def choisir_arme_libre(creature, est_monstre=False):
    armes = armes_monstres_disponibles if est_monstre else armes_disponibles
    print(f"\nArmes disponibles pour {creature.nom} :\n")
    for i, arme in enumerate(armes, 1):
        utilisateurs = ", ".join(arme.get("utilisateurs", []))
        print(f"{i} - {arme['nom']} ({arme['degats']} | {arme['type']}) | Pour : {utilisateurs}")
    
    while True:
        try:
            choix = int(input("Choisissez le numéro de l'arme : "))
            if 1 <= choix <= len(armes):
                creature.arme = armes[choix - 1]
                print(f"{creature.nom} est maintenant équipé de {creature.arme['nom']} !\n")
                break
            print(f"⚠️ Entrez un nombre entre 1 et {len(armes)}.\n")
        except ValueError:
            print("❌ Entrée invalide. Veuillez entrer un chiffre.\n")

def equiper_equipe_libre(equipe, est_monstre=False):
    for creature in equipe:
        choisir_arme_libre(creature, est_monstre)

def preparation_combat():
    print("\nPréparation du combat...\n")
    heros = selectionner_heros()
    monstres = selectionner_monstres()
    boss_creature = selectionner_boss()

    print("\nÉquipe de héros prête :\n")
    for h in heros:
        print(f"- {h.nom} | PV : {h.pv_actuels} | Défense : {h.defense}")
    
    print("\nMonstres prêts :\n")
    for m in monstres:
        print(f"- {m.nom} | PV : {m.pv_actuels} | Défense : {m.defense}")
    
    print("\nChoix des armes pour les héros :\n")
    equiper_equipe_libre(heros)

    print("\nChoix des armes pour les monstres :\n")
    equiper_equipe_libre(monstres, est_monstre=True)

    print("\nTout est prêt ! Que le combat commence !\n")
    return heros, monstres, boss_creature

if __name__ == "__main__":
    afficher_accueil()
    try:
        heros, monstres, boss_creature = preparation_combat()
        lancer_combat(heros, monstres, boss_creature)
    except Exception as e:
        print(f"Une erreur est survenue pendant le jeu : {e}\n")
        print("Redémarrez le jeu et tentez votre chance à nouveau.\n")