# Semaine 7/16

- [x] Pandas

## Pandas

Pandas est une bibliothèque Python pour l'analyse de données. C'est Excel on Steroids.

### Séries

Le plus simple pour démarrer est de créer une série à partir d'une liste. La classe Series est un tableau unidimensionnel étiqueté, capable de contenir n'importe quel type de données (entiers, chaînes, flottants, objets Python, etc.). L'avantage par rapport à une liste est que l'on peut accéder aux éléments par leur étiquette (index) et non par leur position. En outre, on peut effectuer des opérations sur l'ensemble de la série, comme additionner tous les éléments ou appliquer une fonction à chaque élément.

- C'est un tableau unidimensionnel comme un tableau numpy.
- Il est étiqueté, c'est-à-dire qu'il a un index.
- Il peut contenir n'importe quel type de données (pas comme numpy)
- Il est mutable, c'est-à-dire que l'on peut modifier ses éléments.
- Il est optimisé pour les opérations sur les données.

```py
s = pd.Series([1, 2, 3])

s.min
```

#### Index

L'index est un tableau d'étiquettes qui identifie chaque élément de la série. Par défaut, l'index est constitué de nombres entiers commençant à 0. On peut le modifier en passant une liste d'étiquettes lors de la création de la série.

```py
s = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
```
