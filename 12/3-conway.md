# Conway, jeux de la vie

## Introduction

Le jeu de la vie de Conway est un automate cellulaire inventé par le mathématicien britannique John Horton Conway en 1970. 
Il s'agit d'un jeu à zéro joueurs sans objectif, et où la seule interaction possible est de créer un état initial (seed).

## Règles et principe

Le jeu consiste en une grille infinie en deux dimensions de l'espace et une dimension de temps, où chaque cellule peut être à l'état "mort" ou "vivant". Quand la cellule est "morte", elle
est blanche. Quand la cellule est "vivante", elle est noire. Ces cellules peuvent naître ou mourir selon quatre règles simples :

1. Toute cellule vivante avec moins de deux cellules vivantes avoisinantes meurt (sous-population)

2. Toute cellule avec deux ou trois cellules vivantes avoisinantes reste vivante jusqu'à la prochaine unité de temps.

3. Toute cellule avec plus de trois cellules vivantes avoisinantes meurt (surpopulation).

4. Toute cellule morte avec exactement trois cellules vivantes avoisinantes devient une cellule vivante (reproduction).

Ces règles en apparence simples permettent en réalité de recréer des pattern et des systèmes multicellulaires bien plus complexes, certaines pouvant même se reproduire, créer des patterns aléatoires et/ou d'avoir des durées
de vie infinies. 

## Objectifs du projet

L'idée est de recréer un jeu de la vie sur Python à partir de rien, avec une interface simple pour le joueur. Pour rajouter de l'interactivité, nous donnerons
la possibilité aux joueurs de rajouter des cellules pendant la simulation. L'option de ralentir ou accélerer l'écoulement du temps sur le tas sera également possible.