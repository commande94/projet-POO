## 🚀 Prérequis et lancement

Le projet fonctionne avec Python 3.6+. Pour lancer l'application :

```bash
python main.py
```

Placez-vous dans le dossier du projet ; `data.py` contient les listes de personnages, monstres et armes, il est chargé automatiquement.

## ✨ Fonctionnalités supplémentaires

- Possibilité de modifier les points de vie d'un héros au moment de la création.
- Chaque créature dispose d'actions `Soin` et `Buff` en plus de l'attaque classique.
- Les buffs augmentent temporairement la défense de la cible (+2).
- Les monstres et héros possèdent des dés de dégâts différents et les résistances des monstres sont appliquées automatiquement.
- Le MJ peut choisir librement la cible et l'action de chaque créature ; l'ordre d'initiative est calculé automatiquement.
