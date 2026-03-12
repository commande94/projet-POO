
personnages_disponibles = [

    {
        "nom": "Guerrier",
        "pv": 40,
        "defense": 15,
        "type_degats": "tranchant",
        "resistances": [],
        "description": "Combattant expérimenté spécialisé dans le combat rapproché.",
        "pouvoir": "Coup puissant : inflige de lourds dégâts avec son arme."
    },

    {
        "nom": "Mage",
        "pv": 25,
        "defense": 10,
        "type_degats": "magique",
        "resistances": [],
        "description": "Maître de la magie capable de lancer des sorts destructeurs.",
        "pouvoir": "Boule de feu : attaque magique infligeant des dégâts de feu."
    },

    {
        "nom": "Archer",
        "pv": 30,
        "defense": 12,
        "type_degats": "perçant",
        "resistances": [],
        "description": "Tireur d'élite capable de toucher ses ennemis à distance.",
        "pouvoir": "Tir précis : augmente ses chances de toucher la cible."
    },

    {
        "nom": "Paladin",
        "pv": 35,
        "defense": 14,
        "type_degats": "tranchant",
        "resistances": ["poison"],
        "description": "Guerrier sacré qui protège ses alliés et utilise la magie divine.",
        "pouvoir": "Soin sacré : peut soigner un allié pendant le combat."
    },

    {
        "nom": "Voleur",
        "pv": 28,
        "defense": 11,
        "type_degats": "perçant",
        "resistances": [],
        "description": "Combattant rapide et discret expert en attaques surprises.",
        "pouvoir": "Attaque sournoise : inflige des dégâts supplémentaires."
    },

    {
        "nom": "Barbare",
        "pv": 45,
        "defense": 13,
        "type_degats": "contondant",
        "resistances": [],
        "description": "Guerrier sauvage utilisant sa force brute pour écraser ses ennemis.",
        "pouvoir": "Rage : augmente fortement ses dégâts pendant quelques tours."
    },

    {
        "nom": "Druide",
        "pv": 32,
        "defense": 12,
        "type_degats": "magique",
        "resistances": ["poison"],
        "description": "Protecteur de la nature capable d'utiliser la magie naturelle.",
        "pouvoir": "Soin de la nature : soigne un allié avec l'énergie de la nature."
    },

    {
        "nom": "Moine",
        "pv": 30,
        "defense": 13,
        "type_degats": "contondant",
        "resistances": [],
        "description": "Maître des arts martiaux utilisant rapidité et agilité.",
        "pouvoir": "Frappe rapide : peut attaquer deux fois dans un même tour."
    },

    {
        "nom": "Nécromancien",
        "pv": 26,
        "defense": 10,
        "type_degats": "magique",
        "resistances": ["poison"],
        "description": "Mage sombre manipulant la magie de la mort.",
        "pouvoir": "Drain de vie : vole la vie de son ennemi pour se soigner."
    },

    {
        "nom": "Chevalier",
        "pv": 38,
        "defense": 16,
        "type_degats": "tranchant",
        "resistances": ["contondant"],
        "description": "Guerrier lourdement armé spécialisé dans la défense.",
        "pouvoir": "Bouclier protecteur : augmente sa défense temporairement."
    }

]

nombre_personnages = len(personnages_disponibles)


monstres_disponibles = [

    {
        "nom": "Gobelin",
        "pv": 20,
        "defense": 10,
        "type_degats": "perçant",
        "resistances": [],
        "description": "Petite créature rusée et agressive.",
        "pouvoir": "Attaque rapide : peut frapper rapidement un ennemi."
    },

    {
        "nom": "Loup",
        "pv": 25,
        "defense": 11,
        "type_degats": "perçant",
        "resistances": [],
        "description": "Prédateur rapide qui attaque en meute.",
        "pouvoir": "Morsure féroce : inflige de lourds dégâts."
    },

    {
        "nom": "Araignée géante",
        "pv": 30,
        "defense": 12,
        "type_degats": "poison",
        "resistances": ["poison"],
        "description": "Araignée monstrueuse capable d'empoisonner ses victimes.",
        "pouvoir": "Morsure empoisonnée : inflige des dégâts de poison."
    },

    {
        "nom": "Troll",
        "pv": 50,
        "defense": 13,
        "type_degats": "contondant",
        "resistances": [],
        "description": "Créature énorme et brutale.",
        "pouvoir": "Régénération : récupère quelques PV chaque tour."
    },

    {
        "nom": "Orc",
        "pv": 35,
        "defense": 13,
        "type_degats": "tranchant",
        "resistances": [],
        "description": "Guerrier sauvage très dangereux.",
        "pouvoir": "Coup brutal : attaque très puissante."
    },

    {
        "nom": "Squelette",
        "pv": 22,
        "defense": 12,
        "type_degats": "perçant",
        "resistances": ["poison"],
        "description": "Mort-vivant animé par la magie noire.",
        "pouvoir": "Attaque osseuse : attaque avec ses armes rouillées."
    },

    {
        "nom": "Zombie",
        "pv": 40,
        "defense": 9,
        "type_degats": "contondant",
        "resistances": ["poison"],
        "description": "Créature morte-vivante lente mais résistante.",
        "pouvoir": "Résistance mort-vivante : difficile à tuer."
    },

    {
        "nom": "Golem de pierre",
        "pv": 60,
        "defense": 16,
        "type_degats": "contondant",
        "resistances": ["contondant"],
        "description": "Créature faite de pierre presque indestructible.",
        "pouvoir": "Poing de pierre : attaque extrêmement puissante."
    },

    {
        "nom": "Démon",
        "pv": 45,
        "defense": 14,
        "type_degats": "feu",
        "resistances": ["feu"],
        "description": "Créature infernale venue des profondeurs.",
        "pouvoir": "Flamme infernale : attaque magique de feu."
    },

    {
        "nom": "Dragon",
        "pv": 80,
        "defense": 18,
        "type_degats": "feu",
        "resistances": ["feu", "contondant"],
        "description": "Créature légendaire extrêmement puissante.",
        "pouvoir": "Souffle de feu : attaque massive infligeant des dégâts de feu."
    }

]

nombre_monstres = len(monstres_disponibles)


armes_disponibles = [
    {"nom": "Épée courte", "degats": "1d6", "type": "tranchant", "utilisateurs": ["Guerrier", "Paladin", "Chevalier"]},
    {"nom": "Épée longue", "degats": "1d8", "type": "tranchant", "utilisateurs": ["Guerrier", "Paladin", "Chevalier"]},
    {"nom": "Hache", "degats": "1d8", "type": "tranchant", "utilisateurs": ["Barbare", "Guerrier"]},
    {"nom": "Bâton", "degats": "1d6", "type": "magique", "utilisateurs": ["Mage", "Druide", "Nécromancien"]},
    {"nom": "Arc", "degats": "1d6", "type": "perçant", "utilisateurs": ["Archer", "Voleur"]},
    {"nom": "Dague", "degats": "1d4", "type": "perçant", "utilisateurs": ["Voleur", "Moine"]},
    {"nom": "Marteau de guerre", "degats": "1d10", "type": "contondant", "utilisateurs": ["Paladin", "Chevalier"]},
    {"nom": "Bâton de feu", "degats": "1d8", "type": "magique", "utilisateurs": ["Mage", "Druide"]},
    {"nom": "Lance", "degats": "1d8", "type": "perçant", "utilisateurs": ["Guerrier", "Paladin"]},
    {"nom": "Fléau", "degats": "1d8", "type": "contondant", "utilisateurs": ["Barbare", "Chevalier"]},
]

armes_monstres_disponibles = [
    {"nom": "Cimeterre rouillé", "degats": "1d6", "type": "tranchant", "utilisateurs": ["Gobelin"]},
    {"nom": "Crocs acérés", "degats": "1d6", "type": "perçant", "utilisateurs": ["Loup"]},
    {"nom": "Venin d'araignée", "degats": "1d6", "type": "poison", "utilisateurs": ["Araignée géante"]},
    {"nom": "Massue", "degats": "2d6", "type": "contondant", "utilisateurs": ["Troll"]},
    {"nom": "Hache lourde", "degats": "2d4", "type": "tranchant", "utilisateurs": ["Orc"]},
    {"nom": "Os tranchant", "degats": "1d6", "type": "perçant", "utilisateurs": ["Squelette"]},
    {"nom": "Coup de poing zombie", "degats": "2d6", "type": "contondant", "utilisateurs": ["Zombie"]},
    {"nom": "Poing de pierre", "degats": "2d8", "type": "contondant", "utilisateurs": ["Golem de pierre"]},
    {"nom": "Flamme infernale", "degats": "3d6", "type": "feu", "utilisateurs": ["Démon"]},
    {"nom": "Souffle de feu", "degats": "4d6", "type": "feu", "utilisateurs": ["Dragon"]},
]