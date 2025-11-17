# GMAO – Plateforme de Gestion (Maintenance & Assurance)

Ce projet vise à développer une **application web** permettant de gérer deux types de données :

- **Maintenance industrielle** : machines, interventions, stocks, rapports.
- **Assurance** : dossiers, sinistres, documents, suivi des étapes.

Le nom *GMAO* est utilisé par simplicité, mais le système est conçu pour être **polyvalent**.

## Module et technologies utilisées

- Django / Flask (Python)
- Base de donnée SQL
- Pandas (analyse)
- Visualisations graphiques
- Interface web
- Gestion des rôles utilisateurs

## Objectifs

- Centraliser les données (machines + dossiers).
- Suivi simple et rapide des informations.
- Création automatique de rapports.
- Analyse de données (Pandas).
- Interface claire et accessible à distance.

# Fonctionnalités prévues

## Module Maintenance (Industrie)

- Gestion des pièces et consommables
- Avertissements en cas de stock faible
- Gestion des machines (inventaire complet)
- Création et consultation de rapports de maintenance
- Suivi des techniciens et opérations effectuées
- Export et visualisation des données (Pandas, graphiques)
- Historique des interventions

## Module Assurance (Dossiers & cas d'assurance)

- Création et gestion de dossiers d’assurance
- Suivi des sinistres (étapes, statut, évolution)
- Ajout et stockage de documents (PDF, images…)
- Gestion des rdvs et tâches internes
- Vue d’ensemble des clientes, couvertures, sinistres
- Gestion des rémunérations
- Création de fiche salaire
- Analyse des données (tendance, volume, ...)

## Gestion des utilisateurs

- Système de connexion sécurisé
- Gestion des rôles (ex : administrateur, technicien, gestionnaire, équipes)
- Droits d’accès selon le type d’utilisateur
- Journalisation (log) des actions au besoin

## Analyse & Visualisations

- Extraction des données via Pandas
- Création de graphiques (performance, tendances, taux de sinistres…)
- Export CSV / Excel possible selon les besoins
- Résumés automatiques (pdf, rapports, statistiques)

# Portée du projet (Scope)

Le projet vise à fournir :

1. **Un système unifié** pour gérer deux types de données : maintenance industrielle et assurance.
2. **Une interface web** permettant d’accéder aux informations depuis n’importe quel appareil.
3. **Une base de données complète**, structurée et sécurisée.
4. **Des outils d’analyse** pour extraire et visualiser les données de manière claire.
5. **Une architecture évolutive**, afin d’ajouter d’autres modules dans le futur si nécessaire.
6. **Un cadre professionnel**, utilisable dans une entreprise industrielle ou une agence d’assurance.

## Membres

- **Tom Berthoud** — <tom.berthoud@hes-so.ch>
- **Hadrien Fuentes** — <hadrien.fuentes@hes-so.ch>

## Déroulement

- à définir
