# Semaine 03/16

- [x] Classes et méthodes
- [x] Itérateurs et générateurs

## Classes

Une classe est un "plan de construction" pour créer des objets. Elle définit des attributs (données) et des méthodes (fonctions) qui caractérisent le comportement de ces objets.

En python chaque classe peut faire référence à ses membres via le mot-clé `self`.

## Itérateurs et générateurs

- `__iter__` permet de rendre un objet itérable via une boucle `for` par exemple. Cette boucle appelle secrètement la méthode `__iter__` pour obtenir un itérateur.
- `__next__` est une méthode qui doit être définie dans un itérateur. Elle est appelée pour obtenir le prochain élément de la séquence. Si la séquence est épuisée, elle doit lever l'exception `StopIteration`.

```python
class Compteur:
    def __init__(self, limite):
        self.limite = limite
        self.compte = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.compte < self.limite:
            valeur = self.compte
            self.compte += 1
            return valeur
        else:
            raise StopIteration
```

Une approche plus propre est d'utiliser un générateur avec le mot-clé `yield`. Un générateur est une fonction qui utilise `yield` pour produire une série de valeurs au lieu de retourner une seule valeur. Chaque fois que `next()` est appelé sur le générateur, il reprend l'exécution là où il s'était arrêté.

```python
class Compteur:
    def __init__(self, limite):
        self.limite = limite
    def __iter__(self):
        for i in range(self.limite):
            yield i
```
