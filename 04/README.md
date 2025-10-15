# Semaine 04/16

- [x] Surcharge d'opérateurs
- [x] Mini-labo point 2D

## Surcharge d'opérateurs

En Python, la surcharge d'opérateurs permet de définir le comportement des opérateurs standards (comme `+`, `-`, `*`, etc.) pour des objets de classes personnalisées. Cela se fait en définissant des méthodes spéciales dans la classe (`__add__`, `__sub__`, `__mul__`, ...). Le couple `__repr__` / `__str__` est souvent implémenté en complément afin de faciliter le débogage.

Voici un exemple simple d'une classe `Point` qui surcharge l'opérateur `+` pour additionner deux points :

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"

    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return NotImplemented
```

Avec cette définition, vous pouvez maintenant additionner deux objets `Point`:

```python
p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2
assert p3 == Point(4, 6)
```

## Mini-labo : point 2D

Le mini-labo consiste à implémenter une classe `Point` robuste :

- validation des coordonnées (entiers ou flottants uniquement) ;
- surcharge de `__add__`, `__sub__`, `__mul__` (produit par un scalaire) et `__eq__` ;
- ajout d'une méthode `distance` qui calcule la distance euclidienne entre deux points ;
- écriture d'une petite séquence de tests (ex. avec `pytest` ou asserts) pour valider les cas frontières.

Pensez à documenter la classe (`"""Docstring"""`) et à utiliser `__repr__` pour obtenir une représentation claire lors du débogage.
