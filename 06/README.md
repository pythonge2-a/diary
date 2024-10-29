# Semaine 06/16

## Activité Questions

### 1. Comment on travaille à plusieurs 

- VCS (Version Control System) : Git, SVN, Mercurial
- SCCS, RCS, CVS, SVN: Centralisé et numérotation de version
- Git: Décentralisé, numérotation de commit

On utilise un outil de gestion de version (Git)
On travailler sur des branches (branch)
On cherche a éviter les conflits (merge conflict)
On fait des push fréquent pour partager son travail
On fait de petits commits
On cherche a être atomique (chirurgical) dans ses commits

### 2. Est-ce nécessaire de séparer les différentes classes dans différents fichiers ? 

- Oui, pour la lisibilité
- Oui, pour la maintenance
- Oui, pour la modularité
- Oui, pour la réutilisabilité

### 3. À quoi sert le `self` en Python ?

Dans une classe chaque fonction (méthode) doit avoir un paramètre `self` qui est une référence à l'instance de la classe. Cela permet d'accéder aux attributs et méthodes de l'instance.

Un attribut c'est une variable de la classe, une méthode c'est une fonction de la classe.

(voir exemple dans module/__init__.py)

### 4. C'est quoi un itérable ? 

Le datamodel en python défini des méthodes spéciales avec des double underscore `__` qui permettent de définir le comportement d'un objet dans un contexte particulier.

- __add__ : +
- __init__ : initialisateur
- __str__ : Convertir l'objet en chaine de caractère
- __iter__ : Retourne un itérateur
- __next__ : Est propre à chaque itérateur et retourne l'élément suivant

Un itérable c'est un objet qui dispose d'une méthode `__iter__` qui retourne un itérateur.

Un itérateur c'est un objet qui dispose d'une méthode `__next__` qui retourne l'élément suivant.

### 5. Programmation orientée objet

C'est un paradigme de programmation qui permet de modéliser le monde réel en utilisant des objets.

- Classes: C'est un modèle (un plan de fabrication) qui définit un ensemble d'attributs et de méthodes (actions et variables d'état)
- Objet: C'est une instance d'une classe, c'est quelque chose concret.
- Attribut: C'est une variable propre à chaque objet
- Méthode: C'est une fonction propre à chaque objet, autrement dit une action que l'objet peut faire.

En poo il y a les concepts suivants: 

- Objet
- Classe
- Héritage
- Polymorphisme
- Encapsulation
- Abstraction

### 6. Comment fonctionne les exceptions en Python ? 

## Notes

Dans le __main__.py on utilises des fonctionnalités du __init__.py