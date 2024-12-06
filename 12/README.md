# Semaine 12/16

## Modalités du mini-projet

- Groupes de 3-5 étudiants
- 1 projet par groupe
- Travail collaboratif sur GitHub avec Git
- Réalisable d'ici la fin du semestre
- Projet Python sous forme d'un module Python
- Présentation orale en fin de semestre devant toute la classe (5-7 min)

## Critères d'évaluation

| Critère                                                          | Poids |
| ---------------------------------------------------------------- | ----- |
| Authenticité du projet (pas de plagiat, créativité)              | 5     |
| Module Python avec Poetry, dépendances à jour                    | 6     |
| Le `README.md` du projet décrit le projet et son utilisation     | 6     |
| Contribution équilibrée de tous les membres sur Git              | 7     |
| Qualité du code (PEP8, docstring, etc.), test avec black et ruff | 6     |
| Tests unitaires (pytest) avec couverture du code d'au moins 40%  | 6     |
| Documentation, votre code/readme est compréhensible par tous     | 6     |
| Qualité de la présentation finale                                | 20    |
| Démonsration réussie (attention à Murphy)                        | 20    |

## Points théorique (dans le prochain quiz)

- Poetry / Venv
- Module Python
- Tests unitaires

### Cahier des charges

- Le projet **doit** manipuler/traiter des données. 
- Le module **doit** comporter un ou plusieurs affichage graphique.
- Le projet **doit** s'appuyer sur des algorithmes.
- Le projet **doit** être en lien avec votre formation.
- Le projet **doit** être original (pas de copier-coller de projet existant).
- Le projet **doit** être documenté (docstring, README.md).
- Le projet **doit** comporter des tests unitaires (pytest).
- Le projet **peut** avoir des synergies avec d'autres groupes.

## Livrable du Jeudi 2024-12-05T23:59

Un document de environ 1 page en Markdown qui décrit le projet et ses objectifs.
Le document doit comporter les sections suivantes :

- Nom du projet
- Membres du groupe
- Description du projet (croquis, schéma, etc.)
- Objectifs

## Groupes de projet

Groupes de projets :

| Groupe | Projet                             | Taille |
| ------ | ---------------------------------- | ------ |
| 1      | [Chalet](./1-chalet.md)            | 3      |
| 2      | [Powerplant](./2-powerplant.md)    | 5      |
| 3      | [Conway](./3-conway.md)            | 3      |
| 4      | [Banc de test](./4-test-bench.pdf) | 4      |
| 5      | [Filtres](./5-filtres.md)          | 5      |
| 6      | Ballon sonde                       | 5      |
| 7      | [Casse brique](./7-breakout.md)    | 5      |
| 8      | [Django-Manim](./8-manim.md)       | 4      |

## Composition des groupes

| Etudiant-e                        | Formation | Groupe |
| --------------------------------- | --------- | ------ |
| Bachmann Thomas                   | EAI       | 1      |
| Delessert Aurore                  | EAI       | 1      |
| Lantier Alexis                    | EAI       | 1      |
| Djehiche Jérémie                  | EEM       | 2      |
| dos Santos Yann                   | EEM       | 2      |
| Porret Leo                        | EEM       | 2      |
| Sena Bion Pablo Picasso           | EEM       | 2      |
| Uluçinar Can                      | EEM       | 2      |
| Perez Jonas                       | EN        | 3      |
| Richard Rémi                      | EN        | 3      |
| Schorro Romain                    | EN        | 3      |
| Di Giovanni Rémy                  | EEM       | 4      |
| Lüthi Martin                      | EEM       | 4      |
| Vullioud Julien                   | EEM       | 4      |
| Zaco Nicolas                      | EEM       | 4      |
| Magnenat Maxime                   | EN        | 5      |
| Oliveira Barbosa Francisco Rafael | EEM       | 5      |
| Otero Maxime                      | EEM       | 5      |
| Pfister Sébastien                 | EN        | 5      |
| Vuillemier David                  | EEM       | 5      |
| Caputo Dany                       | EEM       | 6      |
| Imhof Valentin                    | EEM       | 6      |
| Laville Yanis                     | EEM       | 6      |
| Melvi Isha                        | EEM       | 6      |
| Welker Théo                       | EEM       | 6      |
| Chaignat Bastien                  | EEM       | 7      |
| Decrausaz Marc                    | EEM       | 7      |
| Ding Jérémy                       | EEM       | 7      |
| Tornare Magali                    | EEM       | 7      |
| Cinelli Estebán                   | EN        | 8      |
| Grodent Clément                   | EN        | 8      |
| Ricchieri Meven                   | EN        | 8      |
| Valiante Santiago                 | EN        | 8      |

## Description sommaire des projets

### 1. Gestion domotique de Chalet

- Afficher Chalet "Le binlin"
- Gestion des données
- Prise d'information de température (fichier ou web)
- +/- Chaufage suivant la température intérieur
- Statistique
- Bilbiothèque pandas et matplotlib pour la gestion de données
- Interface utilisateur avec les fonctions (en ligne ou local)

### 2. Universal Paperclip

Le jeux sera du même type que l'usina à trombone mais plus dans l'univers de l'électricité. Nous pensoions à usine électrique.

Production -> Vente -> Argent -> Composants -> plus d'électrons -> minigames style paperclip -> etc.

### 3. Jeu de la vie de Conway

Implémenter un jeu de la vie de conway avec une interface ou on peut contrôler la vitesse de sinue, le pattern de bare, etc.

### 4. Banc de test

Création d'un banc de test qui gère principalement un oscilloscope et un générateur de fonction. Le but étant d'automatiser une mesure d'un filtre, bode (amplitude et Phase).

### 5. Calcul de filtres

Librairie Python qui permettra de calculer des filtres passifs/actifs jusqu'à l'ordre 8. Type Techebytchev, Butterworth, Bessel

Fonction qui prend en entrée:

- Type de filtre
- Fréquence de coupure / caractéristique
- Facteur de qualité

Dépôt GitHub open source et réutilisable.

### 6. Ballon Sonde

Estimation trajectoire sante météo via données sou forme de champ vectorielle.

### 7. Casse brique

Notre objectif est de créer un casse brique modulable avec différents changements que nous allons apporter pour une meileure exérience de jeu :D, différents niveaux, changement des couleurs du jeu et bien plus encore !

### 8. Django-Manim

Manim est une bibliothèque Python populaire pour produire des animations mathématiques et pédagogiques. Cependant, son utilisation nécessite des compétences en programmation Python, ce qui peut être un frein pour les enseignants, les étudiants, ou les créateurs de contenu ayant peu d'expérience technique.

De même, `matplotlib.animation` est un outil puissant pour créer des animations basées sur des graphiques, mais il reste largement inexploité pour des applications pédagogiques accessibles.

Le projet vise à démocratiser l'accès à ces outils via une plateforme web intuitive qui offre plusieurs fonctionnalités :

- La possibilité de soumettre et coder des scripts personnalisés pour Manim ou Matplotlib.

- Une bibliothèque de scripts pré-codés permettant de générer rapidement des animations pédagogiques de base avec Manim ou Matplotlib.

- Des options d'interaction où les utilisateurs peuvent entrer des paramètres spécifiques (comme des valeurs ou des configurations) pour personnaliser les animations.
