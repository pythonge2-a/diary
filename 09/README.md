# Semaine 09/16

| Étudiant-e              | Groupe | Projet          |
| ----------------------- | ------ | --------------- |
| Affolter Jérémy         | 1      | Babisstat       |
| Asani Adi               | 9      | Éclairage       |
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
| Kosher Ali              | 9      | Éclairage       |
| Lambiel Ludovic         | 3      | Solar           |
| Luisoni Tom             | 5      | FingerFlow      |
| Majstorovic Martin      | 9      | Éclairage       |
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

Les affectations correspondent aux cahiers des charges fournis pour Babisstat, Audio, Solar, Objectif Lune, FingerFlow, GMAO, Orientation PV et SwissEcoAdvisor. Le projet d'éclairage (`lights.md`) cite six prénoms (Adi, Martin, Elisa, Gab, Ali, Pablo) mais seuls Adi Asani, Ali Kosher et Martin Majstorovic figurent dans la liste officielle : la composition doit être confirmée avant la phase d'implémentation. Jad Bechara n'a pas communiqué de projet pour l'instant.

## Groupes

| GRP | Projet           | Pax | Charge (h) | Qualité CdC | Remarques                                             |
| --- | ---------------- | --- | ---------- | ----------- | ----------------------------------------------------- |
| 1   | Babisstat        | 4   | 180        | Solide      | CdC complet, MVP priorisé.                            |
| 2   | Audio            | 5   | 225        | À étoffer   | Description fonctionnelle OK, architecture manquante. |
| 3   | Solar            | 5   | 225        | Correct     | Objectifs de calcul clairs, UI à préciser.            |
| 4   | Objectif Lune    | 2   | 90         | Insuffisant | Texte très court, orthographe et portée à clarifier.  |
| 5   | FingerFlow       | 3   | 135        | Bon         | Vision cohérente, planning et critères à détailler.   |
| 6   | GMAO & Assurance | 2   | 90         | Complet     | Portée large (maintenance + assurance) à cadrer.      |
| 7   | Orientation PV   | 3   | 135        | Structuré   | Paramètres bien listés, mécanique à prototyper.       |
| 8   | SwissEcoAdvisor  | 2   | 90         | Solide      | Concept clair, dépendances données à préciser.        |
| 9   | Éclairage        | 3*  | 135*       | À clarifier | Cahier `lights.md`, équipe mentionnée plus large.     |

\*Selon la liste officielle; la proposition cite six membres, d'où l'incertitude sur la charge réelle.

## Projets

### 1 Babisstat

Babisstat est une application Python destinée au babyfoot du Chillout : elle enregistre les joueurs, permet de configurer des matchs, saisit les buts en mode manuel ou par analyse vidéo (OpenCV) et stocke l’historique dans SQLite pour alimenter un classement Elo et des statistiques détaillées. La première version livrera la gestion des profils, la saisie fiable de résultats et la visualisation des indicateurs, tandis que la détection automatique de buts reste un module exploratoire.

**Revue** — Qualité : cahier des charges très structuré (contexte, objectifs, scénarios) et ton professionnel. Fond : périmètre réaliste pour quatre personnes, avec un MVP clair et une trajectoire progressive vers l’analyse vidéo.

### 2 Éditeur Audio

Le projet vise à créer un mini-Audacity en Python capable de charger des fichiers MP3/WAV/OGG, d’afficher la forme d’onde sur deux pistes et de proposer les actions usuelles (lecture/pause/stop, mute, annuler/rétablir, découpe, réglage de pitch/tempo) avant export. L’équipe prévoit une interface PyQt/Tkinter et un backend basé sur Pydub ou modules équivalents, chaque membre prenant une fonctionnalité en parallèle.

**Revue** — Qualité : écriture correcte mais le document reste très succinct (listes sans sections, quelques fautes mineures). Fond : objectifs réalistes, mais l’absence d’architecture, de format de données et de critères de réussite complique l’estimation des efforts.

### 3 Installation solaires

Le programme Solar dimensionne une installation photovoltaïque à partir de la localisation, du type d’usage et des contraintes de site : il calcule orientation et inclinaison optimales, estime le nombre de panneaux, la puissance totale ainsi que le coût et restitue les recommandations dans une interface simple avec saisie guidée. Les résultats combinent donc calculs techniques et synthèse économique au même endroit.

**Revue** — Qualité : description claire, orthographe soignée, mais la structure gagnerait à préciser sources de données et format de restitution. Fond : périmètre cohérent pour cinq personnes si les hypothèses (modèle de rayonnement, catalogue de panneaux) sont documentées rapidement.

### 4. Objectif Lune

Objectif Lune ambitionne de simuler le pilotage d’une fusée vers la Lune dans un esprit rétro-gaming : calcul d’une trajectoire entre deux planètes, affichage 2D de flux d’air, séparation d’un étage au clavier, cinématique finale et sélection d’un cratère sur image satellite pour y larguer un module. Le projet s’inscrit dans le cadre du cours PythonGE avec une forte composante visuelle.

**Revue** — Qualité : document très court, bourré de fautes (« Appolo », « planete », « calcuation ») et sans structure Markdown ; un vrai cahier des charges reste à rédiger. Fond : ambitions élevées (simulateur physique, rendu graphique) pour deux personnes, sans indication de modèles ou de limites techniques.

### 5. FingerFlow

FingerFlow consiste à exploiter MediaPipe pour détecter en temps réel les repères de la main via la webcam et mapper ces gestes sur des interactions desktop : déplacement de curseur, clics, dessin dans l’air ou actions créatives, le tout dans un exécutable Windows afin de garantir l’accès à la caméra. L’équipe veut proposer une interface intuitive qui visualise la main et laisse paramétrer les gestes.

**Revue** — Qualité : proposition bien écrite et structurée, même si certaines sections (charge, jalons) restent esquissées. Fond : cas d’usage clair et réalisable en 135 h, mais il faudra définir précisément la bibliothèque GUI, les gestes supportés et les critères de performance.

### 6. GMAO & Assurance

Ce projet veut livrer une application web unifiée qui couvre à la fois la maintenance industrielle (machines, pièces, stocks, interventions, techniciens) et la gestion de dossiers d’assurance (sinistres, documents, rendez-vous, rémunérations). Le backend Python (Django/Flask + base SQL) expose une interface sécurisée avec rôles, visualisations via Pandas et exports vers rapports ou dashboards.

**Revue** — Qualité : cahier très complet, organisé par modules et fonctionnalités, avec un ton professionnel. Fond : la double portée maintenance + assurance est ambitieuse pour deux personnes et demandera un cadrage précis des MVPs et des modèles de données partagés.

### 7. Orientation des Panneaux Photovoltaïques

Orientation_PV ambitionne de modéliser l’orientation optimale de panneaux photovoltaïques : le logiciel calcule la position du soleil en fonction de la saison, de l’heure, de la localisation et de capteurs (luminosité, météo), pilote virtuellement des moteurs azimut/inclinaison et inclut un module de gestion d’énergie pour batteries, distribution et réinjection réseau. Une interface simulateur présente les comportements et tableaux de bord.

**Revue** — Qualité : document bien structuré (équipe, paramètres, objectifs) et sans fautes majeures. Fond : idée intéressante mais très ambitieuse (calculs astro, contrôle moteur, gestion énergétique) pour trois personnes ; il faudra prioriser rapidement ce qui reste purement logiciel.

### 8. SwissEcoAdvisor

SwissEcoAdvisor vise à remettre une application d’aide au choix énergétique : l’utilisateur renseigne son adresse et ses contraintes, une première « black box » analyse météo, ensoleillement, vent ou débit pour recommander les technologies adaptées (PV, éolien, hydraulique) avec coûts/production/amortissement, puis une seconde « black box » optimise la configuration retenue. En option, un comparatif multi-énergie et une carte interactive de la Suisse complètent les tableaux et graphiques produits.

**Revue** — Qualité : texte bien structuré (sections, gras, listes) et ton professionnel. Fond : approche crédible pour deux membres, mais la dépendance à des données externes et à des modèles « black box » nécessite de préciser rapidement les sources et méthodes de calcul.

### 9. Éclairage Intelligent

Ce calculateur d’éclairage intérieur récupère des données chez les fournisseurs, classe les luminaires et, selon le type de pièce et le bâtiment, dimensionne la quantité nécessaire avant de proposer plusieurs configurations optimisées en coût et efficacité. Après validation, le système génère un plan 2D illustrant l’implantation, liste les accessoires associés et produit un document récapitulatif (quantités, prix, disponibilité, devis).

**Revue** — Qualité : contenu riche mais stocké dans un notebook, avec quelques fautes et un manque de structure formelle (rôles non nominatifs). Fond : fonctionnalités pertinentes pour un projet logiciel, toutefois l’aspiration à scraper des sites fournisseurs et à générer un plan lumineux complet doit être cadrée pour rester réaliste.
