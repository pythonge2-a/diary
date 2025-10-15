# Semaine 01/16

## Cours

- Théorie
- Pratique
- Quiz (annoncé ou surprise selon les présences et votre sérieux)
- Labos
- Un mini-projet (semaine 7-8)
  - Travail en groupe (plusieurs personnes)
  - Sujet libre
  - Présentation finale dernière séance (note à la clé)

## Python

- Python est un langage de programmation né en 1991
- Il a été créé par Guido van Rossum
- Jusqu'en 2018, il en était le "Benevolent Dictator For Life" (BDFL)
- Le code source de Python est disponible sur GitHub : [python/cpython](https://github.com/python/cpython)
- Python est un langage open source maintenu par la Python Software Foundation
- Le langage met l'accent sur la lisibilité et plusieurs paradigmes (impératif, objet, fonctionnel)

## Syntaxe

```python
a = 5 # integer
b = 3.14 # float
c = "Hello, World!" # string
d = True # boolean
e = None # null value
f = Ellipsis # special value
g = 1 + 2j # complex number

h = [1, 2.0, "toto", 4+2j, Ellipsis] # list (tableau dynamique)
h.append(h)

i = (1, 2.0, "toto", 4+2j, Ellipsis) # tuple (tableau statique)
j = {1, 2.0, "toto", 4+2j, Ellipsis} # set (ensemble non ordonné)
k = {"name": "Alice", "age": 30, "is_student": False} # dictionary (tableau associatif)
l = (n for n in range(10)) # generator (itérateur paresseux)

m = lambda x: x * 2 # fonction anonyme
def add(x, y): # fonction nommée
    return x + y

class Person: # classe
    pass

obj = Person() # instance de classe
```

## Distributions et exécutables

- Python.org ([download](https://www.python.org/downloads/))
- Anaconda distribution complète (lourde) ([download](https://www.anaconda.com/products/distribution))
- Miniconda distribution légère ([download](https://docs.conda.io/en/latest/miniconda.html))
- WinPython distribution légère (pas recommandée) ([download](https://winpython.github.io/))

## Outils nécessaires

- VSCode (Extensions Python et Pylance)
- Git (Git Bash sous Windows)
- Python 3.10 minimum
- PIP (normalement installé avec Python)

## Exercice

1. Installer ce qui manque
2. Mettre à jour Python en 3.13
3. Installer les extensions VSCode
4. Créer un programme Python depuis VSCode qui affiche "Hello, World!" dans le terminal
5. Exécuter le programme
6. Créer un environnement virtuel avec venv
7. Activer l'environnement virtuel
8. Installer avec pip IPython
9. Tester IPython dans le terminal

Si tout fonctionne, bravo : continuez vers la suite du cours !
