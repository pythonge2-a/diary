# Semaine 11/16

- [ ] Projets Python (brainstorming)
- [ ] Poetry / Venv
- [ ] Koch Snowflake avec Turtle

## Théorie restante 

- [ ] Charger des données (excel), afficher...
- [ ] Webscraping

## Projets Python

Le cours "Python GE2", nommé "Python par la pratique", est un cours qui a pour but de vous faire pratiquer Python, la fiche d'unité décrit un mini-projet
réalisé en groupe.

### Contexte

| Orientation | Nombre |
| ----------- | ------ |
| EEM         | 21     |
| EN          | 9      |
| EAI         | 3      |

### Modalités

- Groupes de 3-4 étudiants
- 1 projet par groupe
- Travail collaboratif sur GitHub avec Git
- Réalisable d'ici la fin du semestre
- Projet Python sous forme d'un module Python
- Présentation orale en fin de semestre devant toute la classe (5-7 min)

### Cahier des charges

- Le projet **doit** manipuler/traiter des données. 
- Le module **doit** comporter un ou plusieurs affichage graphique.
- Le projet **doit** s'appuyer sur des algorithmes.
- Le projet **doit** être en lien avec votre formation.
- Le projet **doit** être original (pas de copier-coller de projet existant).
- Le projet **doit** être documenté (docstring, README.md).
- Le projet **doit** comporter des tests unitaires (pytest).
- Le projet **peut** avoir des synergies avec d'autres groupes.

### Livrable du brainstorming

1. Dimanche 2024-12-01T23:59 
   - Idées de projet 
   - Membres du groupe
2. Jeudi 2024-12-05T23:59
   - Document de description du projet

Un document de environ 1 page en Markdown qui décrit le projet et ses objectifs.
Le document doit comporter les sections suivantes :

- Nom du projet
- Membres du groupe
- Description du projet (croquis, schéma, etc.)
- Objectifs

### Quelques idées

- [ ] Créer un banc de test (oscilloscope, generateur, alim). Avec une interface graphique. 
- [ ] Gérer des données (genre Pandas)
- [ ] Simulateur de circuit électrique (LT spice)
- [ ] Moyen de lire les notes sur GAPS
- [ ] Gestionnaire de batteries (simulation)
- [x] Simulateur de panneaux solaires (simulation)
- [x] Jeu de la vie (Conway)
- [x] Application météo (collecter les données web, aggregation, affichage)
- [x] Casse-brique (pygame)
- [ ] Idle game style Cookie Clicker (paperclip)
- [x] Projet avec Manim
- [ ] Chiffrement de messages (César, Vigenère, etc.)
- [ ] Simulateur d'Enigma
- [ ] Mastermind (pygame)
- [ ] Uno (pygame)
- [ ] Jeu Memory


## Turtle

```python
import turtle
t = turtle.Turtle()
t.screen.bgcolor("black")
t.pencolor("yellow")
t.screen.title("Turtle")
t.screen.setup(800, 800)
t.forward(100)
t.left(90)
```
