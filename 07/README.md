# Semaine 07/16

- [ ] Quiz Surprise (25%), donc 3 autres
- [ ] Fonctionnement de Git

## Git, Hash et Bitcoin

- Le Bitcoin est une cryptomonnaie basée sur le concept de Blockchain
- Une Blockchain est une base de données distribuée et sécurisée
- Git fonctionne sur le même principe de Blockchain
- Chaque commit, fichier, arbre est interconnecté via des hashs
- Un hash comme sha256 est une fonction de hachage qui prend en entrée un message et retourne un hash. C'est une transformation non bijective.

## Exemple de Hash

```python
import hashlib

message = "Hello, World!"
hash = hashlib.sha256(message.encode()).hexdigest()
print(hash)
```

## Commandes utilisées

- `git init` pour initialiser un dépôt
- `git add` pour ajouter des fichiers
- `git commit` pour commiter des fichiers
- `git log` pour voir les commits
- `git checkout` pour revenir à un commit
- `git rev-parse HEAD` pour voir le hash du dernier commit
- `git cat-file -p <hash>` pour voir le contenu d'un commit