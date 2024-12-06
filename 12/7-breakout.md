# Description du projet

## Objectif

L'objectif est de créer un casse brique modulable. Le jeu sera codé en python avec comme interface graphique Pygame.
Dans un premier temps, nous allons créer programmer une version simple du jeu afin de nous assurer que la base du jeu fonctionne. Pars la suite, nous allons ajouter les fonctionnalitées citées ci-dessous.

## Cahier des charge (basic)

Comme décrit ci-dessus, voici la liste de fonctionnalitées basiques qu'il est nécessaire d'implémenter au
départ

- Une grille de brique fixe (à définir)
- Une balle à angle variable
- Une raquette à taille fixe
- Des briques pouvant subir plusieurs coups avant d'êtres détruites
- Un système de score
- Un menu permettant au joueur de _jouer_ ou _quitter_
- Au moins 3 niveaux de briques différents
- Un système de couleur permettant l'identification des vies des briques
- Système de tests

## Cahier des charge (advanced)

Dans un deuxième temps, voici ce qui est prévu d'être implémenté

- Différents thèmes (tilesets)
- Vitesse variable de la balle
- Ajout de bonus (aggrandissement de la raquette, super balle etc...)
- Briques invincibles, mobiles
- Ajout de malus (inversion des commandes, ratraicissement de la raquette)
- Multiballe

# Gestion GIT

## Phase développement

Dans un premier temps, durant la phase dite de "développement" la totalité de l'équipe travail sur une seule branche (main). Cela permet à tout le monde de modifier les différentes classes, de ce fait, cela permet à tout le monde d'ajouter les fonctionnalitées nécessaires (les dépendances inter-classes) au bon fonctionnement de leurs tâches.
Il est extrement important d'effectuer des Pull réguliers, des commits ainsi que des push afin que tout le monde travail presque constamment sur la dernière version du projet.

## Phase secondaire

Dans cette phase, une version du jeu "stable" est disponible sur la branche main. L'ajout de nouvelles fonctionnalitées nécessitera la création de branches. De cette manière, la version stable du jeu n'est pas altérée par la création de nouvelles fonctions.
Une fois la branche stable (la fonctionnalité implémentée), un merge request est généré, analysé par l'équipe de développement, et soit validée, soit refusé selon les conflits.

# Tâches

## Integration Pygame

Ding Jérémy

- Créer une fenêtre
- Taille fixe
- Gestion d'entrées
- Gestion affichage

## Collisions

Decrausaz Marc

- Ball- brique
- Ball - murs
- Ball - raquette
- Coins ?
- Rebond ?

## Gestion Niveau

Tornare Magali

- Création du champ de brique
- Création des niveaux
- Essayer de comprendre un truc en python...

## Gestion Bonus

Chaignat Bastien

- Création des bonus
- Intégration dans les briques
