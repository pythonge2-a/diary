# Semaine 01/16

## Types de base

### Scalaires

| Type | Description | Exemple |
|------|-------------|---------|
| `int` | Entier | `42` |
| `float` | Flottant | `3.14` |
| `bool` | Booléen | `True` ou `False` |
| `str` | Chaîne de caractères | `'Hello, World!'` |

```python
c = 2 + 4j  # Nombre complexe
h = 0x1234 # Nombre hexadécimal
o = 0o1234 # Nombre octal
b = 0b1010 # Nombre binaire
```

### Collections

| Type | Description | Exemple |
|------|-------------|---------|
| `list` | Liste | `[1, 2, 3]` |
| `tuple` | Tuple | `(1, 2, 3)` |
| `dict` | Dictionnaire | `{'a': 1, 'b': 2}` |
| `set` | Ensemble | `{1, 2, 3}` |

Dans un `set` ou un `dict` les clés ne peuvent pas être mutables (listes, dictionnaires, etc.). Autrement dit les clés doivent être hashables.
