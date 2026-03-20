🎲 Projet POO – Système de Combat RPG

Ce projet Python REPL (Read Evaluate Print Loop) est un système de combat RPG basé sur la programmation orientée objet (POO). Il a été conçu pour mettre en pratique tous les concepts de POO : classes, héritage, polymorphisme, attributs, méthodes et constructeurs.

Le projet simule des combats au tour par tour entre héros, monstres et boss, avec des actions variées, des jets de dés, et des bonus/malus d’arène.

🐉 Contexte du jeu

Le système s’inspire du jeu Donjons & Dragons (DnD) :

Les joueurs incarnent des héros qui affrontent des monstres et des boss dans des combats au tour par tour.

Un Maître du Jeu (MJ) gère les adversaires et sélectionne les actions des créatures.

Les jets de dés déterminent la réussite ou l’échec d’une action (attaque, soin, buff) mais aussi l'initiative et l'ordre du jeu.

Les combats prennent en compte les caractéristiques des créatures, les armes utilisées, et les résistances des cibles.

Certaines actions ont des effets spéciaux, par exemple Vol, LaPierre ou Chaos.

Les règles sont simplifiées pour rendre le jeu jouable et gérable automatiquement par l’application.

👥 Structure des créatures

Toutes les créatures héritent de la classe Creature, qui contient :

nom : nom de la créature

description : description courte

pv_max et pv_actuels : points de vie

defense : défense ou Classe d’Armure (CA)

initiative : pour déterminer l’ordre de jeu

type_degats : type de dégât (Contondant, Tranchant, Percant, Feu, Poison, Magique)

actions : liste des actions disponibles

etats : états de la créature (buffs, debuffs, en pierre, en vol…)

Personnages

Héritent de Creature

Possèdent une arme (choisie par l’utilisateur)

Possèdent un inventaire

Actions disponibles : Attaque, Soin, Buff, AttaqueSpéciale

Leur type de dégâts dépend de l’arme choisie

Monstres

Héritent de Creature

Possèdent des résistances aux types de dégâts

Actions disponibles : Attaque, Soin, Buff

Les dégâts sont fixes ou définis par des dés (ex : 1d6)

Boss

Héritent de Creature

Peuvent avoir des capacités spéciales : Vol, LaPierre, Chaos

Possèdent des résistances et des dégâts personnalisés

Actions spéciales activables selon le tour ou le type de boss

Possibilité de s’envoler pour esquiver certaines attaques

Possibilité de se transformer en pierre pour devenir presque invincible

Chaos : inflige aléatoirement dégâts ou malus aux alliés

⚔️ Actions disponibles

Chaque action est un objet avec :

nom

executer(lanceur, cible, arene)

Types d’actions

Attaque :

Jet de 1d20 pour toucher la cible

Dégâts selon l’arme ou le type de la créature

Critique : double les dégâts si 20

Échec critique : le lanceur subit des dégâts si 1

Respecte les résistances des cibles

Soin :

Restaure les PV de la cible (ex : 2d8)

Pas de jet nécessaire

Buff :

Augmente la défense ou une autre caractéristique

Peut aussi être un debuff pour diminuer une caractéristique ennemie

AttaqueSpéciale :

Dégâts supplémentaires avec un cooldown de 3 tours

Vol :

Permet au lanceur de s’envoler et d’esquiver les attaques de corps à corps

LaPierre :

Transformation en pierre, rend la cible presque invincible

Impossible à toucher par certaines attaques

Chaos :

Inflige aléatoirement des dégâts ou des malus à toutes les cibles alliées

Exemple : dégâts, réduction de défense, réduction d’initiative

🌍 Arènes

Chaque combat se déroule dans une arène avec :

nom et description

Bonus/malus selon le type de dégâts

Exemple :

Forêt Dense : bonus/malus aux attaques perçantes

Plaine Dégagée : favorise les attaques à distance

Grotte Souterraine : bonus aux attaques magiques

🔱 Fonctionnalités principales

Accueil clair pour le Maître du Jeu

Sélection des héros et nombre de participants

Choix des armes pour chaque héros

Sélection des monstres et leur nombre

Choix du boss

Attribution d’armes aux monstres

Lancement de l’initiative pour déterminer l’ordre de jeu

Tour par tour : choix de l’action et de la cible

Affichage des résultats : jets de dés, dégâts, PV restants

Effets spéciaux : transformation, vol, chaos

Fin du combat : victoire ou défaite selon les participants encore en vie

Gestion des erreurs de saisie utilisateur

💡 Fonctionnalités supplémentaires

Résistances aux types de dégâts

Actions spéciales avec cooldown

Bonus/malus liés à l’arène

Possibilité de gérer plusieurs héros et monstres simultanément

Affichage clair des combats pour le Maître du Jeu

📂 Structure du projet

data.py : données des personnages, monstres, boss et armes

creatures.py : classes Creature, Personnage, Monstre, Boss et actions

combat.py : logique du combat, initiative, tours, sélection des cibles

main.py : interface utilisateur pour lancer le jeu et préparer le combat

README.md : explications et guide d’utilisation

✅ Conditions de réussite

Création des classes Creature, Personnage, Monstre, Boss

Implémentation des actions et effets

Gestion des résistances et bonus/malus d’arène

Tour par tour avec sélection de l’action et de la cible

Vérification des conditions de victoire/défaite

Gestion des erreurs et saisies invalides
