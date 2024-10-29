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

Les exceptions sont un mécanisme qui permet de gérer les erreurs en python. Il existe dans de nombreux langage (C++, Java, C#, etc.).

En C vous n'avez pas les exceptions, vous devez gérer manuellement les erreurs en retournant des codes d'erreurs. Ceci implique que vous devez tester le code d'erreur à chaque appel de fonction à tout les niveaux de la pile d'appel. C'est long et fastidieux.

Avec les exceptions vous avez un mécanisme qui permet d'abandonner l'exécution du programme et de remonter la pile d'appel soit jusqu'à la fin du programme (et le programme se termine avec une erreur) soit jusqu'à un bloc `try` qui capture l'exception.

Un exemple simple:

```python
def devide(a, b):
    if b == 0:
        raise ZeroDivisionError("Division par zéro")
    return a / b
try:
    # code qui peut lever une exception
    devide(1, 0)
except ZeroDivisionError as e:
    # code qui gère l'exception
    print("Division par zéro")
```

### 7. C'est quoi l'héritage ?

L'héritage c'est le troisième pilier de la programmation orientée objet après l'objet et la classe. Cela vous permet de récupérer des classes existantes et de les étendre ou de les modifier en les spécialisant.

Voir l'exemple [heritage.py](./heritage.py)

### 8. C'est quoi le `.` dans l'expression `self.words_list` ?

Le point `.` est l'opérateur de sélection de membre. Il permet d'accéder à un attribut ou une méthode d'un objet. Considérons une classe `Point`:

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
```

Cette classe dispose de 3 membres : `x`, `y` et `move`. Pour accéder à `x` et `y` vous devez utiliser l'opérateur `.`:

```python
p = Point(1, 2)
p.x = 3 # Accès en écriture
print(p.x) # Accès en lecture
p.move(1, 1) # Appel de la méthode move
```

### 9. Comment structurer un programme en Python et par où commencer ?

Généralement vous commencez par créer un module en créant un dossier avec un fichier `__init__.py` et un fichier `__main__.py`. Vous pouvez ensuite créer des sous modules en créant des dossiers avec un fichier `__init__.py` et un fichier `__main__.py`.

En général vous commencez votre programme par implémenter les éléments les plus simples et les plus basiques. Par exemple si vous avez besoin de gérer des vecteurs et exécuter des opérations sur ces vecteurs vous aurez besoin de créer une classe `Vector` et d'implémenter les opérations de base (addition, soustraction, multiplication, division, etc.).

Vous pourriez ensuite imaginer une classe `Matrix` qui vous permet d'implémenter des transformations linéaires sur des vecteurs comme le déplacement, la rotation, l'homothétie, etc.

Étape après étape vous créez donc les briques de base de votre programme et vous les assemblez pour créer des fonctionnalités plus complexes.

```python

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

class TransformationMatrix:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def apply(self, vector):
        return Vector(self.a * vector.x + self.b * vector.y, self.c * vector.x + self.d * vector.y)

    def __repr__(self):
        return f"TransformationMatrix({self.a}, {self.b}, {self.c}, {self.d})"

class RotationMatrix(TransformationMatrix):
    def __init__(self, angle):
        super().__init__(math.cos(angle), -math.sin(angle), math.sin(angle), math.cos(angle))

class TranslationMatrix(TransformationMatrix):
    def __init__(self, dx, dy):
        super().__init__(1, 0, dx, dy)

v1 = Vector(1, 2)
r = RotationMatrix(math.pi / 2)
t = TranslationMatrix(1, 1)

v2 = r.apply(v1)
v3 = t.apply(v2)
```

Généralement vous avez également a écrire des tests unitaires pour vérifier que vos classes et vos fonctions fonctionnent correctement. Vous testez chaque niveau. Plus vous avancer plus vous avez confiance dans votre code et dans vos briques de bases. Vous pouvez alors assembler ces briques pour créer des fonctionnalités plus complexes.

### 10. Comment doit-on structurer la création d'une classe ?

Une classe doit être structurée de la manière suivante:

- Un constructeur `__init__` qui initialise les attributs de la classe
- Des méthodes qui définissent les actions que l'objet peut faire
- Des attributs qui définissent l'état de l'objet

Le constructeur peut prendre des paramètres qui permettent d'initialiser les attributs de la classe. La classe `Point` plus haut possède un constructeur qui prend deux paramètres `x` et `y` et initialise les attributs `x` et `y` de l'objet.

N'oubliez pas le `self` qui est une référence à l'objet lui même. Cela vous permet d'accéder aux attributs et méthodes de l'objet.

### 11. C'est quoi ces méthodes magiques avec un double underscore `__` ?

Le datamodel Python définit des méthodes spéciales qui permettent de définir le comportement d'un objet dans un contexte particulier. Par exemple `__add__` permet de définir le comportement de l'opérateur `+` pour un objet. `__getitem__` permet de définir le comportement de l'opérateur `[]` pour un objet.

Vous pouvez vous aider du [datamodel](https://docs.python.org/3/reference/datamodel.html) pour voir la liste des méthodes spéciales et leur comportement, et comment les implémenter.

Certaines de ces méthodes magiques réagissent soit à un opérateur `+`, `*`, `[]`, `()`, etc. soit à une fonction `len`, `str`, `repr`, `iter`, `next` etc.

### 12. Pourquoi faire des classes plutôt qu'un seul fichier avec des fonctions ?

Les classes permettent de structurer le code de manière plus logique et plus naturelle. Elles permettent de regrouper des données et des fonctions qui agissent sur ces données. Cela permet de créer des objets qui modélisent des entités du monde réel.

Python est un langage orienté objet, il encourage l'utilisation de classes et d'objets. Cela permet de créer des programmes plus modulaires, plus réutilisables et plus maintenables.

C'est très pratique de savoir tout de suite quelles sont les actions associées à un objet plutôt qu'avoir un tas de fonctions qui ne sont pas nécessairement relatives aux autres.

### 13. Quelles sont les bases de l'indentation en Python ? Pourquoi est-ce important ?

Contrairement au C, Python n'utilise pas les accolades `{}` pour structurer les blocs de codes. Python utilise l'indentation pour structurer le code. Cela signifie que vous devez indenter votre code de manière cohérente pour que Python puisse comprendre la structure de votre code.

Malheureusement Python n'impose pas la taille de votre indentation. Vous pourriez choisir 2 espaces, 3 espaces, 4 espaces, 8 espaces, une tabulation, etc. C'est à vous de choisir. Cependant il est recommandé d'utiliser 4 espaces pour l'indentation. C'est la convention la plus répandue. C'est surtout la convention imposées par PEP8.

PEP8 impose un tas d'autres choses comme la longueur maximum d'une ligne, le fait de séparer les opérateurs avec des espaces `2 + 2` et non `2+2`, etc.

Avoir une bonne indentation et mise en forme pour votre code est importante pour éviter les conflits lorsque vous travaillez à plusieurs sur un même projet notamment avec Git.

### 14. C'est quoi @property ?

`@property` est un décorateur qui permet de transformer une méthode en propriété. Cela permet de définir une méthode qui se comporte comme un attribut. Cela permet de définir un attribut calculé qui dépend d'autres attributs de la classe. Voici un exemple

```python
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius ** 2

    @property
    def perimeter(self):
        return 2 * math.pi * self.radius

c = Circle(12)
print(c.area) # 452.3893421169302
```

Notez que vous n'avez pas à utiliser de parenthèses pour appeler la méthode `area`. Cela se comporte comme un attribut. Car en effet `area` est plutôt une propriété d'un cercle plutôt qu'une action sur ce cercle. C'est pourquoi il est plus naturel de l'appeler comme un attribut.

On utilise également les décorateurs pour définir un attribut en lecture seule:

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius
```

On cache l'attribut `_radius` avec un underscore, c'est une convention pour dire que cet attribut est privé. On expose un attribut `radius` en lecture seule qui retourne la valeur de `_radius`.

Comme il n'y a pas de setter défini, vous ne pouvez pas modifier la valeur de `radius`:

```python
c = Circle(12)
print(c.radius) # 12
c.radius = 42 # AttributeError: can't set attribute
```

### 15. Quel est le but du cours ?

> Quel est le but du cours ? Je ne vous pas le lien avec notre filière et j'ai l'impression qu'on fait du Python juste pour faire du Python parce que tout le monde en fait.

La direction de la filière Génie Électrique dépend d'un plan d'étude cadre imposé par la HES-SO dans lequel un cours de projet informatique est prévu. Il a été décider d'axer ce cours sur la programmation Python parce que cela devient un outil de plus en plus utilisé dans le monde professionnel et dans l'ingénierie. Quelque soit le pédigrée de l'ingénieur, il est fort probable qu'il ait à un moment donné à utiliser Python.

Nous pensons qu'il n'est pas raisonnable qu'un jeune ingénieur mette sur son CV qu'il connaît Python alors qu'il n'a eu qu'un seul cours dessus. Nous pensons qu'il est important pour tout ingénieur de connaître un minimum de Python pour être à l'aise dans le monde professionnel.

### 16. Comment donner des arguments à un programme ?

Lorsque vous exécutez un programme (quelque soit le programme) il prend des arguments, une entrée standard et deux canaux de sorties (stdout, stderr). Il dipose également d'un statut de sortie.

En C nous gérions les arguments à la main avec une boucle:

```c
int main(int argc, char **argv) {
    for (int i = 0; i < argc; i++) {
        if (strncmp(argv[i], "--foo=", 6) == 0) {
            printf("Argument %d: %s\n", i, argv[i] + 6);
        } else if (strncmp(argv[i], "--bar=", 6) == 0) {
            printf("Argument %d: %s\n", i, argv[i] + 6);
        }
        ...
    }
}
```

En Python la notion de `argv` existe également mais elle est encapsulée dans le module `sys`:

```python
import sys

for i, arg in enumerate(sys.argv):
    if arg.startswith("--foo="):
        print(f"Argument {i}: {arg[6:]}")
    elif arg.startswith("--bar="):
        print(f"Argument {i}: {arg[6:]}")
```

En pratique on utilisera plutôt une bilbliothèque du type `click` pour gérer plus facilement les arguments :

```python
import click

@click.command()
@click.option("--foo", help="Foo option")
@click.option("--bar", help="Bar option")
def main(foo, bar):
    print(f"Foo: {foo}")
    print(f"Bar: {bar}")

if __name__ == "__main__":
    main()
```

### 17. Peut-on faire un convertisseur de document en Python ?

Oui, en Python on peut écrire par exemple un programme qui effectue une rotation de 13 caractères sur un fichier pour le chiffrer. C'est ce qu'on appelle le chiffrement de César à 13 caractères.

```python
import click

def rot13(text):
    return "".join([chr((ord(c) - 65 + 13) % 26 + 65) if c.isalpha() else c for c in text.upper()])

@click.command()
@click.argument("file", type=click.File("r"))
def main(file):
    for line in file:
        print(rot13(line), end="")

if __name__ == "__main__":
    main()
```

La propriété intéressante de `rot13` c'est que c'est une fonction réversible. Si vous appliquez `rot13` deux fois vous obtenez le texte original. C'est un chiffrement très faible mais qui a le mérite d'exister.

### 18. Dans quel cas utilise-t-on des décorateurs ?

Un décorateur est une fonctionnalité spécifique à certains langages de programmation comme le Python, le C#, le Java, JavaScript, Ruby, PHP, Go, Scala etc. qui permet de modifier le comportement d'une fonction ou d'une méthode. En Python un décorateur est une fonction qui prend une fonction en argument et retourne une fonction.

Un décorateur se comporte comme une fonction qui enveloppe une autre fonction. Cela permet de modifier le comportement de la fonction enveloppée sans la modifier. Cela permet de rajouter des fonctionnalités à une fonction sans la modifier.

Prenons l'exemple de la fonction `fib` qui calcul la suite de Fibonacci de manière récursive:

```python
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)
```

Cette fonction n'est pas du tout performante pour des valeurs de `n` supérieures à 20 car le nombre d'appels récursifs est exponentiel. Pour améliorer les performances on peut décider de conserver en mémoire les résultats des précédants appels pour éviter de les recalculer. On peut écrire un décorateur qui fait cela:

```python
def memoize(f):
    cache = {}
    def wrapper(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return wrapper
```

Cette fonction `memoize` crée un décorateur ici `wrapper` qui appelle la fonction enveloppée `f` si le résultat n'est pas déjà en cache. On peut alors décorer la fonction `fib` avec le décorateur `memoize`:

```python
@memoize
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)
```

De manière plus simple, si on a une fonction toute bête qui attends 3 secondes avant de répondre 42:

```python
import time

def slow_function():
    time.sleep(3)
    return 42
```

Si on utilise `@memoize` on va stocker le résultat de la fonction dans un cache pour ne pas avoir à la recalculer à chaque fois, et donc on attendra plus que 3 secondes la première fois et 0 la seconde fois.

Les décorateurs sont utilisés également pour rendre plus lisible le développement de certains programmes. Click utilise massivement les décorateurs pour définir des commandes et des options.

La bibliothèque Flask utilise également les décorateurs pour définir des routes.

Des décorateurs de base comme `@property` permettent de transformer une méthode en propriété.

### 19. Comment parcourir un document pour chercher un mot ou une phrase ?

Il faut définir ce que l'on entend par un mot ou une phrase. C'est déjà un problème complexe. Néanmoins si on défini qu'un mot c'est une suite des caractères a à z et A à Z séparé soit par le début de chaine, la fin de la chaîne ou des espaces, on peut écrire un programme qui parcourt un document pour chercher un mot.

```python
with open('document.txt', 'r') as file:
    for line in file:
        for word in line.split():
            if word == "foo":
                print("Trouvé")
```

### 20. Comment installer et vérifier un paquet avec Poetry ?

Poetry est un outil de gestion de dépendances pour Python. Il permet de gérer les dépendances de votre projet et de les installer. Il permet également de gérer les versions des dépendances et de les figer pour éviter les problèmes de compatibilité.

Il est souvent associé à un fichier `pyproject.toml` qui contient la liste des dépendances de votre projet. Lorsque vous récupérez un programme qui dispose d'un `pyproject.toml` vous pouvez l'installer avec la commande `poetry install`.

Cela va installer les dépendances de votre projet dans un environnement virtuel. Vous pouvez ensuite activer cet environnement virtuel avec la commande `poetry shell`.

Vous pouvez ajouter une nouvelle dépendence avec :

```bash
poetry add numpy
```

Vous pouvez vérifier les dépendances de votre projet avec la commande `poetry show`.


## Notes

Dans le __main__.py on utilises des fonctionnalités du __init__.py
