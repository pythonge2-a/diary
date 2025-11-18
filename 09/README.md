# Semaine 09/16

| Étudiant-e              | Groupe | Projet          |
| ----------------------- | ------ | --------------- |
| Affolter Jérémy         | 1      | Babisstat       |
| Asani Adi               | 8      | Éclairage       |
| Beaud Corentin          | 2      | Audio           |
| Bechara Jad             |        |                 |
| Berthoud Tom            | 6      | GMAO            |
| Blatti Thomas           | 3      | Solar           |
| Brêchet Thomas          | 2      | Audio           |
| Conde Garea Gabriel     | 7      | PV              |
| Conod Enzo              | 4      | Lune            |
| Cossy Corentin          | 3      | Solar           |
| Dahman Elisa            | 7      | PV              |
| do Carmo Afonso Antonio | 1      | Babisstat       |
| do Vale Lopes Andre     | 2      | Audio           |
| Ferreira Tomovic Dani   | 3      | Solar           |
| Fuentes Hadrien         | 6      | GMAO            |
| Gloor Lorentin          | 7      | PV              |
| Kosher Ali              | 8      | Éclairage       |
| Lambiel Ludovic         | 3      | Solar           |
| Luisoni Tom             | 5      | FingerFlow      |
| Majstorovic Martin      | 8      | Éclairage       |
| Marchand Luc            | 5      | FingerFlow      |
| Martinez Théo           | 8      | SwissEcoAdvisor |
| Moore Alexandre         | 4      | Lune            |
| Mousquès Noémie         | 1      | Babisstat       |
| Osaje Jordan            | 1      | Babisstat       |
| Sieve Alexandre         | 3      | Solar           |
| Tenkeu Azegha Franklin  | 2      | Audio           |
| Torrent Valentin        | 8      | SwissEcoAdvisor |
| Weber Jason             | 5      | FingerFlow      |
| Yusuf Anas              | 2      | Audio           |

## Groupes

| Groupe | Projet     | Qualité CdC | Remarques |
| ------ | ---------- | ----------- | --------- |
| 1      | Babisstat  |             |           |
| 2      | Audio      |             |           |
| 3      | Solar      |             |           |
| 4      | Lune       |             |           |
| 5      | FingerFlow |             |           |

## Projets

### 1 Babisstat

Le projet Babisstat vise à développer une application Python permettant de suivre et d'analyser les performances des joueurs de babyfoot du chillout. L'application offre un mode manuel pour saisir les scores, buteurs et résultats, ainsi qu'un mode avancé d'analyse vidéo reposant sur OpenCV pour détecter automatiquement les actions de jeu. Une base de données SQLite conserve l'historique des matchs, tandis qu'un système de classement Elo évalue les joueurs. Le MVP se concentre sur la gestion des joueurs, la saisie manuelle et les statistiques essentielles, l'analyse vidéo étant prévue comme amélioration future.

### 2 Éditeur Audio

Le projet Éditeur Audio consiste à créer un logiciel semblable à Audacity permettant de lire, visualiser, éditer et exporter des fichiers audio dans différents formats. L’application offrira une interface graphique affichant la forme d’onde sur deux pistes et intégrant des outils d’édition essentiels comme découpage, annulation/rétablissement, lecture/pause/stop, mute ou modifications de pitch et tempo. Le développement s’appuiera sur des modules spécialisés tels que Pydub pour le traitement audio et PyQt/Tkinter pour l’interface, avec une organisation du travail en parallèle selon les fonctionnalités.

### 3 Installation solaires

Le projet Programme de calcul pour installation solaire consiste à développer un outil Python capable de dimensionner une installation photovoltaïque. À partir de la localisation, du type d’installation et des informations sur l’emplacement, le programme calcule l’inclinaison et l’orientation optimales des panneaux, estime le nombre de modules nécessaires, la puissance totale ainsi que le coût global du système. Une interface graphique permet de saisir facilement les paramètres, d’afficher les résultats et de fournir des recommandations claires pour guider l’utilisateur dans la conception de son installation solaire.

### 4. Objectif Lune

Ce projet, développé dans le cadre du cours PythonGE et inspiré par la mission Apollo ainsi que par le domaine aérospatial, consiste à piloter une fusée jusqu’à la Lune afin d’y larguer un module d’exploration. Le programme doit permettre de calculer une trajectoire entre deux planètes, d’afficher en 2D le flux d’air, de détacher un étage de la fusée via une touche du clavier, de présenter le voyage final et de sélectionner un cratère à partir d’une image satellite.

### 5. FingerFlow

Le projet FingerFlow vise à développer un programme Python utilisant MediaPipe pour la reconnaissance de la main en temps réel. Grâce à la détection des points clés de la main (landmarks), l’utilisateur pourra interagir avec son ordinateur sans contact, en simulant des actions telles que le déplacement du curseur, les différents clics par gestes et le dessin dans l’air avec un doigt. L’application exploitera la webcam pour capter les mouvements de la main et traduire ces gestes en commandes interactives, combinant ainsi vision par ordinateur, interaction homme-machine et créativité numérique. Le programme sera exécuté directement sous Windows pour garantir un accès fiable à la caméra.

### 6. GMAO & Assurance

Le projet vise à développer une application Python de gestion de maintenance assistée par ordinateur (GMAO) et de gestion des dossiers d’assurance. L’application permettra de gérer les pièces, machines, techniciens et interventions pour la maintenance industrielle, ainsi que la création et le suivi des dossiers d’assurance, sinistres et documents associés. Une interface web accessible à distance offrira une vue d’ensemble claire, tandis qu’une base de données sécurisée stockera toutes les informations. Des outils d’analyse et de visualisation des données seront intégrés pour faciliter la prise de décision et le suivi des performances.

### 7. Orientation des Panneaux Photovoltaïques

Ce projet vise à développer un système intelligent de gestion d'orientation pour panneaux photovoltaïques. Ce programme optimisera automatiquement la position des panneaux en fonction de la trajectoire solaire et gérera efficacement l'énergie produite.

### 8. SwissEcoAdvisor

Le projet SwissEcoAdvisor a pour objectif de développer un programme en Python visant à aider les particuliers à s’orienter vers la technologie d’énergie renouvelable la plus adaptée à leur domicile en Suisse. Le système utilise une "black box" d’orientation pour fournir des estimations précises des technologies possibles (photovoltaïque, éolien, hydraulique) en fonction des données environnementales et des contraintes de l’utilisateur. Une seconde "black box" d’optimisation permet de sélectionner le produit ou la configuration la plus adaptée pour la technologie choisie. Des fonctionnalités optionnelles incluent un comparatif multi-énergie et une carte interactive de la Suisse. Les résultats sont présentés sous forme de graphiques et tableaux pour faciliter l’interprétation des données.

### 9. Éclairage Intelligent

Le programme est un outil d’aide au dimensionnement d’éclairage intérieur. Il permet de déterminer le type de luminaire le plus adapté à une pièce en se basant sur la surface, la fonction du local, le type de bâtiment et une base de luminaires avec leurs caractéristiques techniques et économiques. Il calcule automatiquement le nombre de luminaires nécessaires et propose la solution la plus avantageuse selon l’efficacité énergétique et le coût.