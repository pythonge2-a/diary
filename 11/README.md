# Semaine 11/16

## Expressions régulières

Une expression régulière (ou regex, pour "regular expression") est une séquence de caractères qui forme un modèle de recherche. Elles sont principalement utilisées pour la recherche et la manipulation de chaînes de caractères.

### Syntaxe de base

Classes de caractères : `[]`
- `[abc]` : correspond à 'a', 'b' ou 'c'
- `[a-z]` : correspond à toute lettre minuscule
- `[0-9]` : correspond à tout chiffre
- `[a-zA-Z0-9]` : correspond à toute lettre ou chiffre

Multiplicateurs :
- `{n}` : exactement n occurrences
- `{n,}` : au moins n occurrences
- `{n,m}` : entre n et m occurrences
- `+` : une ou plusieurs occurrences
- `*` : zéro ou plusieurs occurrences
- `?` : zéro ou une occurrence

Groupes :
- `(abc)` : correspond exactement à 'abc'
- `|` : opérateur "ou", par exemple `(abc|def)` correspond à 'abc' ou 'def'

Ancrages :
- `^` : début de la chaîne
- `$` : fin de la chaîne
- `\b` : bordure de mot
  
### Exemples

0?x[0-9a-fA-F]+

#### DOI

```py
import requests
import re

headers = {
    "User-Agent": "Mozilla/5.0 (compatible; MyPythonScript/1.0; +https://example.com/contact)"
}
   
r = requests.get("https://en.wikipedia.org/wiki/Albert_Einstein", headers=headers)

re.findall(r'href=\s*"([^"]*?doi[^"]*?)"', r.text)
```