# Semaine 08/16  

## Mini Project

### Cahier des charges:

- Démo 5-10 minutes selon la taille des groupes dernière semaine
  - Présentation (vidéo, ppt, ...)
  - Démo de votre programme
  - Allocution de toute l'équipe
  - Vendeur, joviale, séduisant
- Livraison du code 
  - Le projet soit sur Git avec des commits de toutes et tous.
  - Est-ce que le prof arrive à faire fonctionner le code ?
  - Est-ce que c'est documenté ?
  - Est-ce que c'est bien écrit (avec ce qu'on appris dans le semestre)
- Participation
  - Est-ce que l'équipe est soudée
  - Est-ce vous êtes autonome...
  
### Déroulement

1. Annonce du cahier des charges
2. Brainstorming
   - Trouver des partenaires pour former un groupe
   - Proposer une idée de projet
3. Rédiger Propositoin du projet
   - 1-2 pages A4
   - Écrit en Markdown 
   - Liste des membres
   - Nom du projet
   - Description du projet
   - Objectifs
   - 17 novembre 2025 à 23h59   

## Module Python Exécutable (CLI)

- [ ] uv (Gestion du module et des dépendances)
- [ ] click (CLI)
- [ ] ruff (Lint)
- [ ] pytest (Tests unitaires)

## UV 

- uv init
- uv sync
- uv pip install 
- uv add <package>
- uv run <...>

## Ligne de commande (CLI)

**Click**
: Bibliothèque pour créer des interfaces en ligne de commande (CLI) en Python. Elle simplifie la création de commandes, la gestion des arguments et des options, et offre une expérience utilisateur conviviale.

Typer
: Typer est un framework de création d'applications en ligne de commande (CLI) basé sur Click. Il utilise les annotations de type Python pour générer automatiquement des interfaces utilisateur conviviales et des aides en ligne.

Rich
: Rich est une bibliothèque Python pour le rendu de texte riche et de beaux formats dans le terminal. Elle permet d'afficher des tableaux, des barres de progression, des arbres, des syntaxe colorée, et bien plus encore, rendant les applications en ligne de commande plus attrayantes visuellement.

Textual
: Textual est un framework Python pour créer des applications en mode texte (TUI) dans le terminal. Il permet de construire des interfaces utilisateur interactives avec des widgets, des mises en page, et des événements, offrant une expérience utilisateur riche dans un environnement en ligne de commande.

## Ruff

Ruff est un linter rapide pour Python. Il permet de vérifier la qualité du code et de détecter les erreurs potentielles comme : 

- Erreurs de syntaxe
- Problèmes de style (PEP 8)
- Importations inutilisées
- Variables non utilisées
- Problèmes de complexité cyclomatique (trop de branches conditionnelles)
- Problèmes de formatage de chaînes f-string 
- Et bien plus encore...

## Exercice

1. Créer un dossier de projet avec `uv init project`
2. Ajouter Click avec `uv add click`
3. Écrire un programme CLI simple dans `project/main.py`
4. Imaginez un programme cool
5. Ajouter des options et des arguments
6. Ajouter une fonction complexe
7. Ajouter un test pour cette fonction
8. Tester le formatage avec `uv run ruff check .`