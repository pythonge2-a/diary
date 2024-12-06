# Projet StratoPrediction
## Membres du groupe
Isha Melvi
Dany Caputo
Valentin Imhof
Yanis Laville
Théo Welker

## Descritpion du projet 
Utilisation des données NOAA (Vent) pour la prédiction d'un parcout de vol d'un ballon stratosphérique. Pour remettre en contexte le besoin d'un tel système. Les ballons stratosphériques sont utilisés quotidiennement pour la récolte de donné météorologique ainsi que d'autres expériences dans la stratosphère. Le vol du ballon est dit "Libre" car il n'a aucune moyen de naviguer dans l'espace. Il subit obligatoirement les vents et se laisse guider librement. Un système de prédition est intéressant afin de connaitre approximativement le point de chute afin d'éviter les lacs où les montagnes. Certains vols enmènent de l'équipement onéreux et il est nécessaire d'assurer un parcout convenable. Il sera ainsi possible de modifier la date de décollage ou les paramètres de vols (vitesse ascentionelle, etc) pour modifier la trajectoire.

## Objectifs du projet 
- Comprendre les données Grib puis télécharger les fichiers nécessaire.
- Rechercher un moyen d'importer ces fichiers avec Python
- Structurer ces données afin d'avoir accès rapidement aux informations
- Créer une fonction d'interpolation pour obtenir un vecteur V à la position souhaitée (Latitude, Longitude et Altitude)
- Fonction itérative pour faire naviguer un point du sol jusqu'au point d'explosiion puis la chute jusqu'à 0m
- Recherche d'une librairie permettant d'afficher ces points en 3D
- Recherche un moyen d'afficher ces points sur une carte

Fonctions supplémentaires en cas de temps à disposition:
- Système en pyhton pour télécharger automatiquement les fichiers Grib
- Interpolation en 4D avec la gestion du temps inter-fichier