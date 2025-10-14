# Semaine 05/16

- [x] args kwargs
- [x] zip
- [x] Notation ** et *

- [x] Modules
- [x] Importer un module

## Args Kwargs

En python les args font référence aux arguments positionnels, et les kwargs aux arguments nommés. Il est possible de récupérer de manière générique les arguments passés à une fonction en utilisant `*args` et `**kwargs`.

```python
def ma_fonction(*args, **kwargs):
    print("Arguments positionnels:", args)
    print("Arguments nommés:", kwargs)

ma_fonction(1, 2, 3, a=4, b=5)
```

Les arguments positionnels sont récupérés dans un tuple, et les arguments nommés dans un dictionnaire.

On peut demander à Python lors de la déclaration de d'une fonction de forcer l'utilisation d'arguments nommés en utilisant un `*` dans la déclaration:

```python
def ma_fonction(a, b, *, c, d):
    print(a, b, c, d)
```

On peut également forcer l'utilisation d'arguments positionnels en utilisant un `/` dans la déclaration:

```python
def ma_fonction(a, b, /, c, d):
    print(a, b, c, d)
```

## Zip

La fonction `zip` permet de combiner plusieurs itérables (listes, tuples, etc.) en un seul itérable de tuples. Chaque tuple contient un élément de chaque itérable.

```python
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
zipped = zip(list1, list2)
print(list(zipped))  # [(1, 'a'), (2, 'b'), (3, 'c')]
```

Ce qui intéressant c'est qu'on peut dézipper un itérable de tuples en utilisant l'opérateur `*`:

```python
zipped = [(1, 'a'), (2, 'b'), (3, 'c')]
list1, list2 = zip(*zipped)
print(list1)  # [1, 2, 3]
print(list2)  # ['a', 'b', 'c']
```

Zip est souvent utilisé dans une boucle 

```python
for a, b in zip(list1, list2):
    print(a, b)
``` 

## Modules

En python un fichier est considéré comme un module.
Un dossier est considéré comme un module s'il contient un fichier `__init__.py`. Si vous avez des sous-modules, veillez à bien aussi à avoir un `__init__.py` dans chaque dossier.

Attention à ne jamais mettre de code exécutable dans un `__init__.py`, car il sera exécuté à chaque import du module.

## Importer 

En Python les syntaxes possibles sont: 

```python
import module # importe le module en entier comme un namespace
from module import fonction # importe une fonction spécifique
from module import fonction as f # importe une fonction spécifique avec un alias
from module import * # importe toutes les fonctions du module (caca)```
```

Dans le contexte d'un module, on peut aussi faire des imports relatifs:

```python
from . import module # importe un module dans le même dossier
from .. import module # importe un module dans le dossier parent
from .module import fonction # importe une fonction spécifique dans le même dossier
from ..module import fonction # importe une fonction spécifique dans le dossier parent
```

