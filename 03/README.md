# Semaine 03/16

- [x] Classes et méthodes
- [x] Itérateurs et générateurs

## Classes

Une classe est un "plan de construction" pour créer des objets. Elle définit des attributs (données) et des méthodes (fonctions) qui caractérisent le comportement de ces objets.

En Python, chaque méthode d'instance reçoit `self` en premier paramètre : c'est la référence à l'objet courant. Le constructeur est la méthode spéciale `__init__`, appelée automatiquement lors de l'instanciation. Toute méthode dont l'intention est "privée" peut être préfixée par `_` pour signaler qu'elle n'est pas destinée à l'API publique.

```python
class CompteBancaire:
    def __init__(self, titulaire, solde_initial=0):
        self.titulaire = titulaire
        self._solde = solde_initial

    def deposer(self, montant):
        self._solde += montant

    def retirer(self, montant):
        if montant > self._solde:
            raise ValueError("Solde insuffisant")
        self._solde -= montant

    def afficher_solde(self):
        return f"{self.titulaire} possède {self._solde} CHF"
```

Les classes peuvent hériter d'autres classes pour réutiliser du comportement (`class CompteEpargne(CompteBancaire): ...`) et implémenter des méthodes spéciales (`__str__`, `__len__`, etc.) pour s'intégrer aux primitives du langage.

## Itérateurs et générateurs

- `__iter__` permet de rendre un objet itérable via une boucle `for` par exemple. Cette boucle appelle secrètement la fonction `iter(objet)` qui délègue ensuite à `objet.__iter__()` pour obtenir un itérateur.
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

Une approche plus concise consiste à utiliser un générateur avec le mot-clé `yield`. Un générateur est une fonction qui produit une série de valeurs au fil de l'eau plutôt que de calculer toute la séquence d'avance. Chaque fois que `next()` est appelé sur le générateur, il reprend l'exécution là où il s'était arrêté.

Les générateurs sont pratiques pour manipuler de grandes quantités de données, streamer un fichier ou chaîner des transformations sans créer de listes intermédiaires.

```python
class Compteur:
    def __init__(self, limite):
        self.limite = limite
    def __iter__(self):
        for i in range(self.limite):
            yield i
```
