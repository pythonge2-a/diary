# Semaine 05/16

- [x] `*args` et `**kwargs`
- [x] `zip`
- [x] Paramètres positionnels, nommés et notation `*` / `/`
- [x] Créer un module
- [x] Importer un module

## *args et **kwargs

En Python, `args` fait référence aux arguments positionnels et `kwargs` aux arguments nommés. Il est possible de récupérer de manière générique tous les arguments passés à une fonction en utilisant `*args` (tuple) et `**kwargs` (dictionnaire).

```python
def ma_fonction(*args, **kwargs):
    print("Arguments positionnels:", args)
    print("Arguments nommés:", kwargs)

ma_fonction(1, 2, 3, a=4, b=5)
```

Les arguments positionnels sont récupérés dans un tuple et les arguments nommés dans un dictionnaire.

On peut demander à Python, lors de la déclaration d'une fonction, de forcer l'utilisation d'arguments nommés en utilisant un `*` dans la signature :

```python
def ma_fonction(a, b, *, c, d):
    print(a, b, c, d)
```

On peut également forcer l'utilisation d'arguments positionnels en utilisant un `/` dans la déclaration :

```python
def ma_fonction(a, b, /, c, d):
    print(a, b, c, d)
```

### Exemple avec les boissons (généré par chatGPT)

```python
def drink(qty, **kwargs):
    # Récupération des contextes
    when = kwargs.get('when', 'anytime')
    weather = kwargs.get('weather', 'normal')
    thirsty = kwargs.get('thirsty', False)
    on_date = kwargs.get('on_date', False)
    mood = kwargs.get('mood', 'normal')
    exam_week = kwargs.get('exam_week', False)
    broke = kwargs.get('broke', False)
    sport_day = kwargs.get('sport_day', False)
    hangover = kwargs.get('hangover', False)
    apocalypse = kwargs.get('apocalypse', False)

    # Liste des boissons pour le fun
    boissons = {
        'beer': "🍺 bière",
        'milk': "🥛 lait",
        'coffee': "☕ café",
        'water': "🚰 eau",
        'tea': "🍵 tisane",
        'smoothie': "🥤 smoothie",
        'wine_red': "🍷 vin rouge",
        'wine_white': "🍷 vin blanc",
        'soda': "🥤 soda",
        'mojito': "🍹 mojito",
        'energy': "⚡ Red Bull",
        'whisky': "🥃 whisky",
        'nothing': "💨 rien du tout (dommage !)",
        'blood': "🩸 sang (faut qu’on parle...)",
    }

    # Logique pleine de jugements gratuits
    if apocalypse:
        print(f"💥 Fin du monde ? Je te donne {qty}l de {boissons['whisky']}, dernier apéro avant les zombies.")
    elif hangover:
        print(f"🤢 Gueule de bois ? {qty}l de {boissons['water']} + {boissons['tea']} pour survivre.")
    elif broke:
        print(f"💸 T’as plus un rond ? {qty}l de {boissons['water']} du robinet, c’est bio.")
    elif exam_week:
        print(f"📚 Semaine d’examens ? {qty}l de {boissons['coffee']} puissance 1000.")
    elif on_date and when == 'evening':
        print(f"💘 Tu dragues ? Voilà {qty}l de {boissons['wine_red']} pour impressionner (ou pas).")
    elif when == 'morning':
        if sport_day:
            print(f"🏋️ Matin sportif ? {qty}l de {boissons['smoothie']} blindé de protéines.")
        elif weather == 'cold':
            print(f"🥶 Il caille ? {qty}l de {boissons['coffee']} pour te réchauffer.")
        else:
            print(f"☀️ Matin chill ? {qty}l de {boissons['milk']}, retour en enfance.")
    elif when == 'afternoon':
        if thirsty:
            print(f"😩 T’as soif ? {qty}l de {boissons['soda']} bien sucré (diabète en DLC).")
        else:
            print(f"🌤️ Après-midi pépère ? {qty}l de {boissons['tea']} façon mamie.")
    elif when == 'evening':
        if mood == 'sad':
            print(f"😢 Tristesse ? {qty}l de {boissons['whisky']}... mais appelle un pote aussi.")
        else:
            print(f"🎉 Soirée ? {qty}l de {boissons['beer']}, la base.")
    elif when == 'night':
        print(f"🌙 Nuit tardive ? {qty}l de {boissons['mojito']} pour bien finir... ou mal commencer demain.")
    elif thirsty:
        print(f"🚰 T’as la dalle en flotte ? {qty}l de {boissons['water']}, gorgée d’espoir.")
    else:
        print(f"🤖 Pas compris le contexte, donc {qty}l de {boissons['nothing']}. Reviens quand t’es prêt.")

# Testons avec des contextes randoms
drink(1, when='evening', on_date=True)
drink(0.3, when='morning', weather='cold')
drink(2, when='afternoon', thirsty=True)
drink(0.5, thirsty=True)
drink(0.75, broke=True)
drink(1, when='evening', mood='sad')
drink(0.6, hangover=True)
drink(1.5, apocalypse=True)
drink(1, when='morning', sport_day=True)
```

## Zip

La fonction `zip` permet de combiner plusieurs itérables (listes, tuples, etc.) en un seul itérable de tuples. Chaque tuple contient un élément de chaque itérable.

```python
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
zipped = zip(list1, list2)
print(list(zipped))  # [(1, 'a'), (2, 'b'), (3, 'c')]
```

Ce qui est intéressant, c'est qu'on peut dézipper un itérable de tuples en utilisant l'opérateur `*` :

```python
zipped = [(1, 'a'), (2, 'b'), (3, 'c')]
list1, list2 = zip(*zipped)
print(list1)  # [1, 2, 3]
print(list2)  # ['a', 'b', 'c']
```

`zip` retourne un itérateur paresseux : une fois consommé, il faut en recréer un nouveau si l'on souhaite itérer à nouveau. Il est souvent utilisé dans une boucle `for` :

```python
for a, b in zip(list1, list2):
    print(a, b)
```

Pour traiter des séquences de longueur différente, utilisez `itertools.zip_longest` :

```python
from itertools import zip_longest

for a, b in zip_longest(list1, list2, fillvalue=None):
    print(a, b)
```

## Modules

En Python, chaque fichier (`.py`) est un module. Un dossier devient un package lorsqu'il contient un fichier `__init__.py`. Depuis Python 3.3, les namespace packages permettent de s'affranchir de ce fichier, mais dans un contexte pédagogique il reste recommandé de garder un `__init__.py` explicite, surtout en présence de sous-packages.

Évitez de mettre du code exécutable dans un `__init__.py`, car il sera exécuté à chaque import du package. Limitez-vous à l'initialisation de l'API (`__all__`, import de sous-modules, constantes, etc.).

## Importer

En Python les syntaxes possibles sont :

```python
import module  # importe le module en entier comme un namespace
from module import fonction  # importe une fonction spécifique
from module import fonction as f  # importe une fonction spécifique avec un alias
from module import *  # importe tout le namespace du module (fortement déconseillé)
```

Dans le contexte d'un module, on peut aussi faire des imports relatifs :

```python
from . import module  # importe un module dans le même dossier
from .. import module  # importe un module dans le dossier parent
from .module import fonction  # importe une fonction spécifique dans le même dossier
from ..module import fonction  # importe une fonction spécifique dans le dossier parent
```

Privilégiez les imports absolus (`from package.module import ...`) pour la lisibilité et utilisez les imports relatifs uniquement à l'intérieur d'un package cohérent.

Pour rendre un module exécutable tout en conservant un comportement correct à l'import, encapsulez le code dans un `if __name__ == "__main__":` :

```python
def main():
    print("Ce bloc s'exécute seulement quand le module est lancé directement")


if __name__ == "__main__":
    main()
```
