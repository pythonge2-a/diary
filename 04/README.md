# Semaine 04/16

- [ ] Arguments (`*args`, `**kwargs`)

## Arguments de fonctions

En Python, il est possible de définir des fonctions qui prennent un nombre variable d'arguments. On distingue deux types d'arguments : les arguments positionnels (args) et les arguments nommés (kwargs).

Les arguments positionnels peuvent avoir une valeur par défaut:

```python
def foo(a, b=42):
    print(a, b)
```

Les arguments nommés sont stockés dans un dictionnaire:

```python
def bar(**kwargs):
    print(kwargs)

bar(a=1, b=2, c=3)
```

## Syntaxe * et **

L'opérateur `*` est utilisé pour déballer une liste ou un tuple. L'opérateur `**` est utilisé pour déballer un dictionnaire.

Ces opérateurs seront utilisés pour passer des arguments à une fonction.

```python
u = [1,2,3]
v = {'a': 1, 'b': 2, 'c': 3}

def foo(*args, **kwargs):
    print(args)
    print(kwargs)

foo(*u, **v)
```

## Itérables

Un itérable est un objet qui peut être parcouru. Les listes, les tuples, les ensembles, les dictionnaires, les chaînes de caractères, les fichiers, les générateurs, les fonctions génératrices, les objets de type `range`, etc. sont des itérables.

Elles disposent d'une méthode `__iter__` qui renvoie un itérateur.

L'itérateur dispose d'une méthode `__next__` qui renvoie l'élément suivant.

```python
iterable = [1, 2, 3]
iterator = iter(iterable)
print(next(iterator))
```

## Compréhension

Une compréhension, personne ne la comprend...

```python
[x for x in itérable]
[x for x in itérable if condition]

# /!\ Attention, les compréhensions imbriquées sont difficiles à lire
# La logique est de l'intérieur vers l'extérieur
[(x, y) for x in itérable1 for y in itérable2]

# On peut utiliser les compréhension avec des dictionnaires
{x: x**2 for x in range(5)}

# Ou avec des ensembles
{x for x in range(5)}

# Ou avec des générateurs
(x for x in range(5))
```

## Modules

Du moment que j'ai un dossier qui comprend un fichier `__init__.py`, je peux importer les fichiers `.py` comme des modules.

Dans le `__init__.py` on mettera les fonctions et les classes que l'on souhaite rendre accessibles.

Dans le `__main__.py` on aura le programme principal executable depuis la ligne de commande.

Le nom du dossier est le nom du module.

### Utilisation d'un module dans un script

```python
from module import foo, bar, baz

...
```

```bash
$ python script.py
```

### Utilisation d'un module depuis une interface REPL

```bash
$ python
>>> from module import foo, bar, baz
>>> foo()
>>> exit()
```

### Exécution d'un module

```bash
$ python -m module
```

## Environnement virtuels 

On utilise `venv` pour créer un environnement virtuel.

```bash
$ python -m venv venv
$ source venv/bin/activate
```

Sous Windows 

```cmd
> python -m venv venv
> venv\Scripts\activate
```

Et après.... Vous pouvez installer paquets avec `pip`

```bash
$ pip install requests
```

A la fin de la session, vous pouvez quitter l'environnement virtuel avec la commande `deactivate`.

```bash
$ deactivate
```