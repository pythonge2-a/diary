# Semaine 04/16

- [ ] Surcharge d'opérateurs
- [ ] Mini-labo point 2D

## Surcharge d'opérateurs

En Python, la surcharge d'opérateurs permet de définir le comportement des opérateurs standards (comme +, -, *, etc.) pour des objets de classes personnalisées. Cela se fait en définissant des méthodes spéciales dans la classe.

Voici un exemple simple d'une classe `Point` qui surcharge l'opérateur `+` pour additionner deux points:

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        return NotImplemented
```

Avec cette définition, vous pouvez maintenant additionner deux objets `Point`:

```python
p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2
```
