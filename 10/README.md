# Semaine 10/16

- [x] Mots clés Python (keywords)
- [x] `help('keywords')`
- [x] https://github.com/Asabeneh/30-Days-Of-Python
- [x] Idées de mini-projets

## Mots-clés

La commande `help('keywords')` permet d'afficher la liste des mots-clés réservés en Python:

```python
False               class               from                or
None                continue            global              pass
True                def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
(async)             except              lambda              with
(await)             finally             (nonlocal)          yield
break               for                 not
```

### True, False et None

Python dispose de trois valeurs `True`, `False` et `None` qui sont utilisées pour les tests de conditions. Vous connaissez déjà `True` et `False` qui sont utilisées pour les tests de conditions. `None` est utilisée pour les fonctions qui ne retournent pas de valeur.

```python
print(True) # True
print(False) # False

True == False # False
True != False # True
```

Par défaut une fonction retourne `None` si aucune valeur n'est retournée.

```python
def my_function():
    print('Hello')

my_function() is None # True
```

Avec `None` on utilise préféablement `is` ou `is not` pour les tests d'égalité.

```python
a = None
print(a is None) # True
print(a is not None) # False
```

### and, or, not

Ces mots clés sont similaires aux mots-clés `&&`, `||` et `!` en C.

```python
print(True and False) # False
print(True or False) # True
print(not True) # False
```

On va les retrouver dans les tests de conditions.

```python
if a and not b or c:
    print('OK')
```

Alternativement on peut utiliser le `or` pour simplifier certaines expressions:

```python
if not a:
    print('NOK')

a or print('NOK')
```

### for, while, continue et break

Les boucles `for` et `while` sont utilisées pour répéter des instructions.

```python
for i in range(10):
    print(i)

for i, j in enumerate(range(10)):
    print(i, j)

for i, j in zip(range(10), range(10, 20)):
    print(i, j)

for i, (a, b) in enumerate(zip(range(10), range(10, 20))):
    print(i, a, b)
```

While ne prend qu'une condition de maintien.

```python
i = 0
while i < 10:
    print(i)
    i += 1
```

Continue permet de passer à l'itération suivante.

```python
for i in range(10):
    if i == 5:
        continue
    print(i)
```

Tandis que `break` permet d'interrompre la boucle.

```python
for i in range(10):
    if i == 5:
        break
    print(i)
```

### from, import et as

`from` et `import` sont utilisés pour importer des modules ou des fonctions. `as` permet de renommer les modules ou les fonctions importées.

```python
from math import sqrt
import numpy as np
from math import sqrt as sq
```

### Pass

`pass` est utilisé pour ignorer une instruction. C'est l'équivalent d'une instruction vide. On l'utilise principalement pour définir des fonctions ou des classes vides.

```python
def my_function():
    pass

class MyClass:
    pass
```

### if, else et elif

`if`, `else` et `elif` sont utilisés pour les tests de conditions.

```python
if a:
    print('OK')
elif b:
    print('NOK')
else:
    print('KO')
```

On peut également utiliser des conditions ternaires.

```python
print('OK') if a else print('NOK')

a = 42 if b else 23
```

On peut également utiliser `if` dans des compréhensions de listes.

```python
a = [i for i in range(10) if i % 2 == 0]
```

### class et def

`class` et `def` sont utilisés pour définir des classes, des fonctions ou des méthodes.

```python
class MyClass:
    def __init__(self):
        pass

    def my_method(self):
        pass

def my_function():
    pass
```

### return

`return` est utilisé pour retourner une valeur à partir d'une fonction.

```python
def my_function():
    return 42
```

On peut également retourner plusieurs valeurs sous forme de tuple.

```python
def my_function():
    return 42, 23

assert isinstance(my_function(), tuple)
```

### with

`with` est utilisé pour gérer des ressources. Il est utilisé pour ouvrir un fichier, une connexion à une base de données ou un autre objet qui doit être fermé après utilisation.

L'utilisation la plus courante est avec les fichiers.

```python
with open('file.txt', 'r') as f:
    print(f.read())
```

Sous le capot, `with` utilise les méthodes `__enter__` et `__exit__` des objets.

```python
class MyResource:
    def __enter__(self):
        print('Enter')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print('Exit')

with MyResource() as r:
    print('Inside')
```

Ce code va afficher:

```text
Enter
Inside
Exit
```

### global

`global` est utilisé pour déclarer une variable globale à l'intérieur d'une fonction.

```python
i = 42
def my_function():
    i = 23
    print(i)
```

Dans cet exemple la variable `i` n'est pas modifiée car une nouvelle variable `i` est créée dans la fonction (*shadowing*). Pour modifier la variable globale `i` on utilise `global`.

```python
i = 42
def my_function():
    global i
    i = 23
    print(i)
```

Global n'est pas recommandé car il rend le code difficile à lire et à maintenir.

### Raise

`raise` est utilisé pour lever une exception. Lorsqu'une exception est levée le programme s'arrête et la chaîne d'appel est remontée jusqu'à ce qu'une exception soit attrapée. Si personne n'attrape l'exception le programme s'arrête.

```python
raise ValueError('Message')
raise AttributeError('Message')
raise Exception('Message') # Exception est la classe de base pour toutes les exceptions
```

### Try, catch et finally

Pour attraper une exception on utilise `try`, `except` et `finally`.

```python
try:
    print(1 / 0)
except ZeroDivisionError as e:
    print(e)
finally:
    print('Finally')
```

Le finally est exécuté que l'exception soit levée ou non. Le `finally` est optionnel.

Rappelez-vous de la règle de PEP20:

> Errors should never pass silently.
> Unless explicitly silenced.

Cela veut dire que les erreurs ne doivent pas être ignorées sauf si c'est explicitement demandé. Donc le code suivant ne devrait pas être utilisé.

```python
try:
    print(1 / 0)
except ZeroDivisionError as e:
    pass
```

### Assert

`assert` est utilisé pour vérifier une condition. Si la condition est fausse, une exception `AssertionError` est levée.

```python
assert True
assert a < 42, Message si faux
```

C'est un moyen simple de vérifier les préconditions et les postconditions on peut obtenir le même essai avec un `if` et un `raise`.

```python
if not a < 42:
    raise AssertionError('Message si faux')
```

### Yield

`yield` est utilisé pour retourner une valeur à partir d'une fonction génératrice. Une fonction génératrice est une fonction qui retourne un itérable.

```python
def my_generator():
    yield 42
    yield 23

>>> g = my_generator()
>>> next(g)
42
>>> next(g)
23
>>> next(g) # Lève une exception StopIteration
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration ...
```

On peut l'utiliser par exemple pour générer des nombres premiers en utilisant le criblage d'Ératosthène.

```python
def primes():
    n = 2
    while True:
        for i in range(2, n):
            if n % i == 0:
                break
        else:
            yield n
        n += 1

>>> g = primes()
>>> next(g)
2
>>> next(g)
3
>>> next(g)
5
>>> next(g)
7
>>> next(g)
11
```

Èvidemment il ne vaut pas consommer tout le générateur car il est infini.

```python
for i in primes(): # Ne se termine jamais
    print(i)
```

Par contre on peut utiliser `zip` pour limiter le nombre de valeurs générées.

```python
for i, p in zip(range(10), primes()):
    print(i, p)
```

Ici `zip` va s'arrêter le plus petit des deux itérables.

### Del

`del` est utilisé pour supprimer une variable ou un élément d'une liste.

```python
a = 42
del a
```

Ou pour supprimer un élément d'une liste.

```python
a = [1, 2, 3]
del a[1]
>>> a
[1, 3]
```

### IN

`in` est utilisé pour vérifier si un élément est dans une liste, un dictionnaire ou un ensemble. Il est également utilisé comme mot clé dans les boucles `for`.

```python
a = [1, 2, 3]
print(1 in a) # True
print(4 in a) # False

d = {'a': 1, 'b': 2}
print('a' in d) # True
```

### is

`is` est utilisé pour vérifier si deux objets sont identiques. C'est l'équivalent de `==` pour les objets.

1. `is` compare les adresses mémoires des objets.
2. `==` compare les valeurs des objets.

```python
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b) # True
print(a is b) # False

a = b
print(a is b) # True
```

Pourquoi utiliser `a is None` plutot que `a == None` ? La réponse est que `None` est un singleton et il n'y a qu'une seule instance de `None` dans la mémoire. Mais il est préférable d'utiliser `is` pour la clarté du code.

### lambda

`lambda` est utilisé pour créer des fonctions anonymes. C'est une fonction qui n'a pas de nom. C'est également une *closure*. Une *closure* est une fonction qui capture les variables de l'environnement dans lequel elle est définie.

```python

x = 5
f = lambda y: y * x
print(f(2)) # 10
```

Les lambdas sont utilisées pour les fonctions simples qui ne sont utilisées qu'une seule fois. On les utilise souvent avec `map`, `filter` et `reduce` qui sont des fonctions de la programmation fonctionnelle (comme Lisp, Scheme, Haskell, etc.).

```python
a = [1, 2, 3]
b = map(lambda x: x * 2, a)
# b = [2, 4, 6]

a = [1, 2, 3, 4, 5]
b = filter(lambda x: x % 2 == 0, a)
# b = [2, 4]

from functools import reduce
a = [1, 2, 3, 4, 5]
b = reduce(lambda x, y: x + y, a)
# b = 15
```

### (async) et (await)

`async` et `await` sont utilisés pour la programmation asynchrone. Ils sont utilisés pour les coroutines. Les coroutines sont des fonctions qui peuvent être suspendues et reprises. Elles sont utilisée pour les entrées-sorties (I/O) asynchrones.

Nous ne les verrons pas dans ce cours.

### (nonlocal)

`nonlocal` est utilisé pour déclarer une variable qui n'est pas locale à la fonction mais qui n'est pas globale non plus.

```python
def my_function():
    a = 42
    def my_inner_function():
        nonlocal a # Permet de modifier la variable `a` de la fonction parente
        a = 23
    my_inner_function()
    print(a)
```

Nous ne les verrons pas dans ce cours.

## Built-in Functions

Types:

```python
bool
bytes
dict
float
frozenset
int
list
set
slice
str
tuple
type
```

Fonctions:

```python
abs
all
any
bin
chr
delattr
dir
divmod
enumerate
eval
filter
getattr
hash
help
hex
id
input
isinstance
iter
len
min
next
oct
open
ord
pow
print
@property
range
repr
sorted
sum
vars
zip
```

Autres fonctions built-in:

```python
locals
object
setattr
staticmethod
super
ascii
breakpoint
bytearray
callable
classmethod
exec
format
issubclass
memoryview
```

