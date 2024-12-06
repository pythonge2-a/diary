# Cahier des charges - Projet domotique chalet "Binlin"

## 1. Présentation du projet

### Contexte

Ce projet consiste à développer un système domotique simulé pour un chalet. L'objectif est de proposer une gestion automatisée et intelligente de certains équipements du chalet à partir de données externes et de critères définis. Le système est entièrement réalisé en Python et repose sur des données simulées ou récupérées en ligne.
### Objectifs :
- Offrir une solution réaliste de simulation de domotique.
- Tester et valider les interactions entre les différentes fonctionnalités du système.
- Coder la simulation en python

---

## 2. Fonctionnalités principales
### 1. Régulation de la température :

- Récupération des données de température via une API Internet ou des fichiers locaux (ex. OpenWeatherMap).
- Contrôle automatique du chauffage pour maintenir une température confortable.
- Simulation de la consommation énergétique.

### 2. Ouverture/Fermeture des volets et/ou Velux :

- Gestion automatisée en fonction de la luminosité ou de l’heure (simulée).
- Possibilité de contrôle manuel via une interface utilisateur.

### 3. Contrôle des lumières :

- Allumage et extinction des lumières en fonction de la présence simulée ou des horaires.
- Réglage de l’intensité lumineuse (dimmer).

### 4. Interface utilisateur :

- Interface en ligne de commande ou graphique pour :
  - Visualiser l’état actuel du système (température, lumières, volets).
  - Modifier les réglages manuellement (ex. température souhaitée, forcer l’ouverture des volets).

---

## 3. Contraintes techniques
- **langage** : python
- **Données externes** :
  - Utilisation d'une API pour récupérer les températures et la luminosité (ex. OpenWeatherMap).
  - Alternativement, exploitation de fichiers CSV/JSON pour simuler les données.
- **Simulation** : Le projet doit être réalisable sans matériel physique (ou Raspberry, a voir l'avancée du projet).
- **Interface utilisateur** : Simplicité et clarté, adaptée pour une démonstration.

---

## 4. Principe de fonctionnement

### A. Régulation de la température

- Entrée : Température externe via API ou fichiers.
- Sortie : Ajustement automatique du chauffage pour maintenir la température.

### B. Gestion des volets/Velux

- Entrée :
  - Horaires simulés.
  - Luminosité externe (API ou fichier).
- Sortie :
  - Ouverture des volets à l’aube et fermeture au crépuscule.
  - Ajustement en cas de forte luminosité ou météo défavorable.
  -
### C. Contrôle des lumières

- Entrée : Boutons et/ou luminosité et menu en ligne.
- Sortie : Allumage/extinction des lumières et menu en ligne.

### D. Interface utilisateur

- Affichage en temps réel des données système (température, état des volets, état des lumières).
- Commandes interactives pour modifier les réglages.

---

*Yverdon-les-Bains le 05.12.2024*
*Aurore Delessert, Alexis Lantier, Thomas Bachmann*
