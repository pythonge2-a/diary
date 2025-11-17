# Babisstat – Cahier des charges du projet
_Application Python pour l’analyse de matchs de babyfoot_

**Auteurs** : Affolter Jérémy, Do Carmo Antonio, Mousquès Noémie, Osaje Jordan
**Date** : 16 novembre 2025

---

## Table des matières

- [Babisstat – Cahier des charges du projet](#babisstat--cahier-des-charges-du-projet)
  - [Table des matières](#table-des-matières)
  - [1. Contexte du projet](#1-contexte-du-projet)
  - [2. Objectifs du projet](#2-objectifs-du-projet)
  - [3. Fonctionnalités attendues](#3-fonctionnalités-attendues)
  - [4. Module d’analyse vidéo](#4-module-danalyse-vidéo)
  - [5. Architecture technique](#5-architecture-technique)
  - [6. Ressources utilisées](#6-ressources-utilisées)
  - [7. Scénarios possibles d’utilisation](#7-scénarios-possibles-dutilisation)
    - [Scénario 1 : Saisie manuelle](#scénario-1--saisie-manuelle)
    - [Scénario 2 : Analyse vidéo](#scénario-2--analyse-vidéo)
  - [8. Priorité de développement](#8-priorité-de-développement)

---

## 1. Contexte du projet

Le babyfoot présent dans le bar de l’école, surnommé *chillout*, est largement utilisé par des joueurs occasionnels ou assidus, mais sans aucun système de suivi ou d’analyse des performances. Le projet **Babisstat** est conçu pour combler ce manque. Il vise à développer une application qui permet de recueillir et d’afficher des informations pertinentes sur les matchs joués, d’établir un classement dynamique des joueurs et, à terme, d’intégrer des outils d’analyse vidéo pour automatiser la collecte des statistiques de jeu.

---

## 2. Objectifs du projet

L’objectif principal du projet est de permettre la saisie et l’analyse des performances lors des matchs de babyfoot en utilisant une application Python. Cette application doit offrir deux modes de fonctionnement :

- Un **mode manuel**, où les utilisateurs peuvent saisir les scores et les buteurs.
- Un **mode vidéo**, où les actions de jeu sont automatiquement détectées à partir des images capturées par une caméra.

Le projet intègre également un système de classement basé sur l’algorithme **Elo**, permettant de refléter de manière pertinente les performances des joueurs. Une base de données doit être mise en place afin de conserver un **historique complet** des matchs, des scores et des statistiques associées.

---

## 3. Fonctionnalités attendues

L’application doit permettre d’enregistrer les joueurs et de les associer en équipes. Lors du lancement d’un match, l’utilisateur doit pouvoir :

- Choisir les joueurs impliqués et leur rôle (attaque ou défense).
- Sélectionner le mode de saisie des scores (manuel ou vidéo).

En mode manuel, l’interface propose des boutons pour incrémenter ou décrémenter les scores, ainsi qu’un menu permettant d’enregistrer le buteur. Une fois le match terminé, les statistiques sont mises à jour : victoires, défaites, buts marqués et encaissés, moyenne de buts par match et mise à jour du classement Elo.

---

## 4. Module d’analyse vidéo

L’analyse vidéo est une fonctionnalité avancée et facultative pour le MVP. Elle repose sur **OpenCV**, une librairie Python de traitement d’images. Le système pourra analyser un flux vidéo provenant soit d’une webcam, soit d’un téléphone utilisé comme caméra IP.

Le flux vidéo sera décodé pour :

- Détecter la balle.
- Suivre son mouvement.
- Identifier le franchissement des lignes de but.

Des améliorations futures pourraient intégrer la détection des tirs cadrés, arrêts, autogoals ou prise de possession. Des tests sur plusieurs babyfoots seront nécessaires pour fiabiliser le modèle.

---

## 5. Architecture technique

L’application sera développée en **Python** et sera composée de trois éléments principaux :

1. Une **interface graphique** (Tkinter ou PyQt) pour l’interaction utilisateur.
2. Un **backend** contenant la logique métier (gestion des matchs, calcul des stats, classement).
3. Une **base de données SQLite** gérée via SQLAlchemy, stockant les informations persistantes (joueurs, équipes, matchs, buts).

Le module vidéo s’appuiera sur OpenCV pour la capture et l’analyse de la séquence vidéo et sur NumPy pour les calculs numériques.

---

## 6. Ressources utilisées

Les principales technologies et librairies utilisées dans le projet :

- **OpenCV** : traitement des images et vidéo.
- **NumPy** : calcul matriciel.
- **Pandas** : manipulation des données.
- **Tkinter** ou **PyQt** : interface utilisateur graphique.
- **SQLAlchemy** : interface ORM pour la base de données SQLite.
- **Matplotlib** (optionnel) : visualisation de graphiques.

---

## 7. Scénarios possibles d’utilisation

### Scénario 1 : Saisie manuelle

1. L'utilisateur lance l'application.
2. Il sélectionne les joueurs et forme les équipes.
3. Il choisit le mode manuel et lance le match.
4. À chaque but, il utilise les boutons pour mettre à jour le score.
5. À la fin du match, les stats et le classement sont mis à jour.

### Scénario 2 : Analyse vidéo

1. Le match est filmé puis la vidéo est importée.
2. L’application analyse la vidéo pour détecter les buts et événements.
3. L’utilisateur valide ou corrige les résultats.
4. Les stats sont sauvegardées dans la base.

---

## 8. Priorité de développement

La première version (MVP) inclut uniquement les éléments suivants :

- Gestion des joueurs et équipes.
- Saisie manuelle des scores.
- Calcul des statistiques principales.
- Mise à jour du classement Elo.

L’analyse vidéo constitue un module avancé et sera implémentée dans une version suivante, même si nous souhaitons en intégrer un prototype dans le rendu final du projet.
