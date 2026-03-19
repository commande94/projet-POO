class Attaque(Action):
    def __init__(self):
        super().__init__("Attaque")
    def executer(self, lanceur, cible):
        print(f"⚔️ {lanceur.nom} attaque {cible.nom} !")
        jet = random.randint(1, 20)
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