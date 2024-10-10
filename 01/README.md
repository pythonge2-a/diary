# Semaine 01/16

- [x] Type de base (int, float, bool, str, complex)
- [x] Collections de base (list, tuple, dict, set)
- [x] Interface REPL
- [x] Inventé par Guido van Rossum en 1991
- [x] Il n'est plus BDFL (Benevolent Dictator For Life) depuis 2018
- [x] Python est open source et communautaire
- [x] Il est multi-paradigme (impératif, orienté objet, fonctionnel)

## Types de base

### Scalaires

| Type      | Description          | Exemple           |
| --------- | -------------------- | ----------------- |
| `int`     | Entier               | `42`              |
| `float`   | Flottant             | `3.14`            |
| `complex` | Complexe             | `2 + 4j`          |
| `bool`    | Booléen              | `True` ou `False` |
| `str`     | Chaîne de caractères | `'Hello, World!'` |

```python
c = 2 + 4j  # Nombre complexe
h = 0x1234 # Nombre hexadécimal
o = 0o1234 # Nombre octal
b = 0b1010 # Nombre binaire
```

### Collections

| Type    | Description  | Exemple            |
| ------- | ------------ | ------------------ |
| `list`  | Liste        | `[1, 2, 3]`        |
| `tuple` | Tuple        | `(1, 2, 3)`        |
| `dict`  | Dictionnaire | `{'a': 1, 'b': 2}` |
| `set`   | Ensemble     | `{1, 2, 3}`        |

Dans un `set` ou un `dict` les clés ne peuvent pas être mutables (listes, dictionnaires, etc.). Autrement dit les clés doivent être hashables.

## Console REPL

- **R**ead: Lire une instruction
- **E**valuate: Évaluer l'instruction
- **P**rint: Afficher le résultat
- **L**oop: Recommencer

Lorsque vous exécutez `python` ou mieux `ipython` sur votre machine vous entrez en mode REPL et vous pouvez exécuter des instructions Python directement dans la console.
