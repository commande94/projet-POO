# 🎲 Projet POO - Système de combat RPG

Projet Python REPL (**R**ead **E**valuate **P**rint **L**oop) visant à utiliser les concepts de POO (**P**rogrammation **O**rientée **O**bjet) afin de créer un système de jeu de combat type RPG (**R**ole **P**laying **G**ame).

Tous les concepts de POO du cours Advanced 2 devront être utilisés, à savoir **les classes, les attributs, les méthodes, l'héritage et le polymorphisme**.

Le projet est prévu pour des groupes de 3 personnes, pour environ une quinzaine d'heure. Il est important de bien séparer les taches, savoir qui fait quoi et mettre le code en commun régulièrement. Utiliser Git pour travailler en collaboration est vivement conseillé.

Les consignes suivantes servent de base, les élèves peuvent ensuite ajouter des éléments à leur guise.

## 🐉 Contexte DnD

Le jeu Donjons et Dragons (abrégé **_DnD_**) est probablement le jeu de rôle (**_JDR_**) le plus populaire depuis de nombreuses années. Dans ce jeu, on incarne un personnage vivant des aventures exceptionnelles, la plupart du temps à plusieurs. Les joueurs forment donc un groupe d'aventuriers, et l'histoire est jouée au fur et à mesure. L'histoire est décrite par un Maître du Jeu (**_MJ_**) incarnant tous les autres personnages du monde.

Lors de leurs aventures, les joueurs font régulièrement face à des adversaires, le plus souvent des monstres qu'il faut vaincre pour sauver leur peau. Le **MJ** doit alors gérer le combat en jouant les adversaires.

Dans DnD, le système de combat repose autour de jets de dés, le joueur décide de ce qu'il veut faire, lance un dé et soit il réussit, soit il échoue. Les chances de réussite du jet dépendent des caractéristiques du lanceur ET de la cible, par exemple il est plus facile de mettre un coup d'épée quand on joue un guerrier et que l'on cible une grand-mère que l'inverse...

Dans DnD les combats sont géré au tour par tour, c'est à dire que les personnages jouent les uns après les autres. Pour déterminer qui joue le premier tous les participants lancent l'_initiative_, c'est à dire un dés à 20 face (_1d20_), celui obtenant le meilleur score commence, le second le suis...

En combat il est possible de faire autre chose qu'attaquer, par exemple on peut soigner (**_Heal_**) ou rendre un personnage plus fort ou resistant (**_BUFF_**).

Le jeu utilise différents type de dés avec différents nombres de faces (4, 6, 8, 10, 12, 20, 100). On utilise pafois plusieurs dés pour certaines actions, par exemple pour faire des dégats on pourrait utiliser 3 dés à 6 faces, l'addition des 3 nous donne le nombre de dégats à appliquer. Pour simplifier l'écriture on note le lancé de 3 dés à 6 faces **_3d6_**.

Le contexte décrit ci dessus est immuables, mais les consignes qui vont suivre ne reflettent pas la totalités des règles de **DnD**, elles ont étées largement simplifiées pour être réalisable par tous dans le temps imparti. Si vous en avez le temps n'hésitez pas à ajouter des choses en plus de ces consignes (précisez le simplement en commentaire au début du fichier principal afin que je le sache pour la correction).

## ✉️ Demande

Un maitre du jeu fatigué de devoir compter les jets de dés de ses joueurs de tête vous demande de créer un système de combat simplifié pour ses parties.

Il vous demande de **pouvoir séléctionner les personnages et les monstres du combat**, puis gérer automatiquement l'_initiative_. Ensuite le combat se déroule tour par tour, le MJ sera le seul à utiliser l'application, il demandra à ses joueurs ce qu'ils souhaitent faire et à chaque tour il séléctionnera l'**action faite** par la **créature** et la **cible** de cette action, et tous les jets de dés seront automatiquement simulés.

On **affichera clairement au MJ les résultats des jets de dés** et toutes les informations importantes (créature qui joue, liste des actions, liste des cibles possible pour une action, nombre de pv restant après une attaque...)

Le maitre du jeu aimerait également que vous proposiez une ou plusieurs fonctionnalités supplémentaires dans votre programme afin de lui facilité la vous ou d'étoffer ses possibilités

## 🧑‍🏫 Consignes

Le jeu devra se dérouler de la façon suivante

- Accueil de l'utilisateur sur le jeu
- Demander à l'utilisateur combien de **_personnage_** vont combattre
- Séléctionner les **_personnages_** parmi une liste (que vous aurez créé vous même)
- Pour chaque personnage séléctionner une arme parmi une liste (que vous aurez créé vous même)
- Demander à l'utilisateur combien de **_monstre_** vont combattre
- Séléctionner les **_monstres_** parmi une liste (que vous aurez créé vous même)
- Lancer l'_initiative_ pour déterminer l'ordre de jeu
- Pour chaque créature demander à l'utilisateur l'**action** qu'il souhaite réaliser
- Demander à l'utilisateur de séléctionner la **cible** de cette action
- Le jeu s'arrête quand tous les personnages **ou** tous les heros sont KO

## 🏃‍♂️ Actions

### ⚔️ Attaque

Quand une créature lance une attaque, il choisi sa cible, puis lance un dés à 20 face (_1d20_), si le résultat est supperieur à la defense (**CA**) de la cible, alors on dit que l'attaque _touche_, sinon elle _échoue_.

Si l'attaque a touché on lance alors les **dégats**. Toutes les créatures ne font pas les mêmes dégats (un gobelin frappe moins fort qu'un dragon). Les dégats sont souvent défini par un nombre de dés à 4, 6, 8, 10 ou 12 faces je vous laisse définir _vous même_ quelle créature jette quelles dés pour faire ses dégats.

Les attaques peuvent aussi rentrer dans 2 cas particuliers : **les critiques**.

- Si le lanceur fait **_20_** à son jet d'attaque (score max) c'est une **_réussite critique_**. Il a particulièrement bien frappé, on **double ses dégats**
- Si le lanceur fait **_1_** à son jet d'attaque (score min) c'est un **_echec critique_**. Il s'est completement loupé, il s'inflige des **dégats à lui même**.

Les dégats ont aussi un certain **_type_** (_tranchant, percant, contondant, feu, poison, magique_...). Pour les personnages le type de dégat **dépend de l'arme** choisi. Pour les monstres il est défini par défaut (feu pour un dragon, poison pour une araignée, percant pour un loup...).

Les monstres peuvent avoir des **_resistances_** à certain type de dégat, par exemple un dragon resiste au feu et au dégat contondant grace à sa peau epaisse. Cela signifie que si une attaque de feu ou contondante le touche il **divise** automatiquement ces dégats par 2.

### 💊 Soin

Une créature peut se soigner ou soigner les autres lors de son tour de jeu. C'est une action bénéfique donc **pas besoin de faire de jet**, on applique simplement l'effet du soin (par exemple _2d8_) à la cible

### 💪 Buff / De-buff

Une créature peut augmenter ou diminuer les caracteristique d'une autre créature, par exemple augmenter les dégats, ou baisser la défense. Je vous laisse libre de choisir des capacités cohérente pour chaque créature.

## ⚙️ Technique

Il faudra donc une classe **Personnage** pour créer un héros et une classe **Monstre** pour créer un monstre.

**Personnage** et **Monstre** ont beaucoup en commun, on peut donc considérer qu'ils vont hériter d'une classe commune: **Créature**

Toute **créature** possède :

- Un `nom`
- Une `description`
- Des points de vie `pv`
- Une `defense` (CA pour les connaisseurs)
- Une `initiative` (permet de déterminer qui joue en premier)
- Une liste d'action (ce qu'il pourra faire à son tour de jeu)
- Un type de dégats (`typeDegats`) parmi la liste suivante
  - Contondant
  - Tranchant
  - Percant
  - Feu
  - Poison
  - Magique
- Une liste d'états `etats` (il pourrait être empoisoné / paralysé / inspiré...)
- Une attaque classique `attaque()` (action d'attaquer qui inflige les dégats de l'attribut `degat`)

Les créatures peuvent :

- Lancer l'initiative
- Afficher leurs actions
- Afficher leurs caracteristiques (attention les personnage et les monstres ont aussi des caraceristique particulière qu'il faudra afficher)

Un **_personnage_** a en plus :

- Une arme
- Un inventaire

Un **_monstre_** à en plus :

- Une liste de resistance

Les actions seront également de objets contenant **au minimum** :

- Un nom
- Un lanceur
- Une cible

Vous aurez probablement besoin d'autres classes, attributs et méthode, n'hésitez pas à ajouter des choses.

### 💡 Idées d'ajout supplémentaires

- Le joueur peut saisir certaine caracteristique du héros (`pv`, `dégat` par exemple)
- Ajouter des actions bonus
- Ajouter les modificateur aux attaques
- Ajouter des jets de sauvegarde
- Ajouter d'autre options dans le combat à votre guise

## 📂 Rendu demandé

- Le **planning du projet**, comportant la répartition des taches et une estimation de temps pour chaque tache (utilisez un outil type [Trello](https://trello.com/))
- Le code terminé, sans bug et à jour
- Une ou plusieurs **fonctionnalités supplémentaire**
- Un fichier `readme.md` contenant les prérequis pour lancer le script et l'explication de vos fonctionnalités supplémentaires.
- Un repo **git propre**

## ✅ Condition de réussite

- Créer une classe **Creature** avec des attributs, des méthodes et un constructeur
- Créer les classes **Heros** et **Monstre**, qui hérite de **Creature**
- Ajouter les spécificités des 2 classes, ajouter un constructeur qui override le constructeur de **Creature**
- Gérer la saisie utilisateur
- Gérer le combat
- Prévoir un cas de victoire et un cas de défaite
- Gérer **les erreurs**

## ☝ Conseils

Avancez **pas à pas**, ne commencez pas 3 choses en même temps.

Aidez vous du cours.

N'hésitez pas à utiliser la fonction `print()` pour afficher les valeur contenu dans les variables

Prenez le temps de lire les erreurs et essayer de les comprendre avant de les copier-coller bêtement sur internet

Travailler en équipe **prend du temps** ! Prévoyez ce temps, mettre en commun le travail de 3 personnes ça ne se fait pas avec un simple copier coller. Pour vous simplifier la vie mettez le code en commun **régulièrement**, pas au moment d'envoyer le code.

**Communiquez** ! Il faut que vous sachiez qui travaille sur quoi, pour ne pas faire le travail en double ET pour que vos codes se complètent intelligement.

## 📚 Ressources

- [Documentation Python](https://docs.python.org/3/)
- [Tutoriel POO en Python](https://realpython.com/python3-object-oriented-programming/)
- [Règles de Donjons et Dragons](https://dnd.wizards.com/)
