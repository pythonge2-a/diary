# Semaine 06/16

L'objectif de cette semaine est de se familiariser avec le système de gestion de versions Git, un outil essentiel pour le développement collaboratif et la gestion de projets logiciels.

## Cryptomonnaies et Blockchain

Avant de plonger dans Git, nous allons explorer les concepts fondamentaux des cryptomonnaies et de la blockchain. Comprendre ces technologies est crucial pour saisir l'importance de la gestion de versions dans le développement de logiciels modernes.

Le Bitcoin a été la première cryptomonnaie à utiliser la technologie blockchain, introduite par une personne ou un groupe sous le pseudonyme de Satoshi Nakamoto en 2008. La blockchain est une base de données distribuée qui enregistre les transactions de manière sécurisée et transparente.

Imaginez que l'objectif est de créer un moyen de stocker des transactions monétaires en respectant les règles suivantes :

- Il n'y a pas d'autorité centrale qui contrôle les transactions.
- Les transactions doivent être sécurisées et immuables.
- Tout le monde doit pouvoir vérifier les transactions tout est transparent.
- Le système est anonyme.

Imagions que nous avons des coffres en diamant tansparents et indestructibles. Une fois fermés, personne ne peut plus jamais les ouvrir et que pour fermer le coffre il faut un effort surhumain (des miliers de personnes qui travaillent ensemble).

Si Bob veut envoyer 10 unités monétaires à Alice, il place une note dans le coffre :

```text
BOB -> ALICE : 10
```

Le coffre est ensuite scellé (fermé) et un effort surhumain est fourni pour le fermer. Une fois fermé, le coffre est placé dans une rangée.

Adméttons maintenant qu'Alice veut envoyer 5 unités monétaires à Eve. Elle place une note dans un nouveau coffre :

```text
ALICE -> EVE : 5
```

Avant de fermer le coffre, Alice doit prouver qu'elle a bien reçu 10 unités de Bob. Pour cela, elle inclut une référence au coffre précédent dans le nouveau coffre. Pour ce faire elle prend en photo le premier coffre (comme il est transparent on y voit bien la note à l'intérieur, ainsi que le numéro du coffre: coffre n°1) et elle colle cette photo sur la note qu'elle place dans le nouveau coffre :

```text
           Coffre n°1                            Coffre n°2
  ╔══════════════════════════╗         ╔══════════════════════════╗
  ║ ░░░░░░░░░░░░░░░░░░░░░░░░ ║         ║ ░░░░░░░░░░░░░░░░░░░░░░░░ ║
  ║ ░ ╭──────────────────╮ ░ ║         ║ ░ ╭──────────────────╮ ░ ║
  ║ ░ │ Transaction      │ ░ ║         ║ ░ │ Transaction      │ ░ ║
  ║ ░ │ BOB → ALICE : 10 │ ░ ║ <-----  ║ ░ │ ALICE → EVE : 5  │ ░ ║
  ║ ░ │ Coffre scellé    │ ░ ║         ║ ░ │ Réf. coffre n°1  │ ░ ║
  ║ ░ │ Note visible     │ ░ ║         ║ ░ │ Photo intérieure │ ░ ║
  ║ ░ ╰──────────────────╯ ░ ║         ║ ░ ╰──────────────────╯ ░ ║
  ║ ░░░░░░░░░░░░░░░░░░░░░░░░ ║         ║ ░░░░░░░░░░░░░░░░░░░░░░░░ ║
  ╚══════════════════════════╝         ╚══════════════════════════╝
```

Ce processus se répète pour chaque nouvelle transaction, chaque coffre faisant référence au coffre précédent. Cela crée une chaîne de coffres (blockchain) où chaque coffre est sécurisé et lié au précédent.

## Hashing

Dans notre exemple précédant pour sceller les coffres, nous avons mentionné qu'un effort surhumain était nécessaire. En réalité, dans la blockchain, ce processus est réalisé à l'aide d'une fonction de hachage cryptographique, et la photo du coffre précédent est remplacée par le hash du contenu du coffre précédent.

Nous devons donc définir ce qu'est une fonction de hachage. Une fonction de hachage est un algorithme qui prend une entrée (ou 'message') et retourne une chaîne de caractères de longueur fixe, généralement sous forme de nombre hexadécimal. Cette sortie est appelée le 'hash' ou 'empreinte'.

Le hash de type SHA-256 (Secure Hash Algorithm 256 bits) est largement utilisé dans les applications de sécurité, la blockchain et même Git. Il produit un hash de 256 bits (32 octets) représenté par une chaîne hexadécimale de 64 caractères. Pour simplifier la compréhension, nous allons considérablement simplifier le fonctionnement mais garder l'idée principale.

On a une chaîne de caractère d'entrée "BONJOUR!" et on veut générer une chaîne de sortie. Le B va sur la seconde position, le O sur la troisième. Pour calculer cinquième case on fait un ou exclusif (XOR) entre la 4e et la 5e case (J et O) auquel on fait également un XOR avec une valeur fixe K dépendante de la valeur. On fait pareil avec la fonction J qui contient une table de 8 valeurs fixes utilisées pour le calcul:

```text
+---+---+---+---+---+---+---+---+
| B | O | N | J | O | U | R | ! |
+---+---+---+---+---+---+---+---+
  |   |   |   |   |   |   |   |
  |   |   |   | +---+ |   |   '----.
  |   |   |   '-| K | |   |        |
  |   |   '---. +---+ |   +---.    |
  |   '---.   |   |   |   |   |    |
  '---.   |   |   | +-------+ |    |
      |   |   |   | |   J   | |    |
      |   |   |   | +-------+ |    |
      |   |   |   |   .-'     |    |
      |   |   |   |   |   .---'    |
      v   v   v   v   v   v        |
+---+---+---+---+---+---+---+---+  |
| ! | B | O | N | Z | S | R | ! |  |
+---+---+---+---+---+---+---+---+  |
  ^                                |
  '--------------------------------'
```

On répète ce processus 1000 fois, a chaque passe le texte sera mélangé un peu plus. Le résultat final est le hash. Si le texte est beaucoup plus long que 8 caractères, pas de problème, on le découpe en blocs de 8 caractères et on se déplace dans le texte en faisant un XOR entre le hash courant et le bloc suivant, ce jusqu'à la fin du texte.

Depuis votre terminal vous pouvez utiliser la commande `sha256sum` pour calculer le hash SHA-256 d'un fichier ou d'une chaîne de caractères. Par exemple :

```bash
echo -n 'BONJOUR!' | sha256sum
d71746d53d395dc19a10e3b5470b7b5f94a428216b887e9288924e679ad77d4e
```

Cette valeur est parfaitement unique pour l'entrée "BONJOUR!". Même un petit changement dans l'entrée produira un hash complètement différent, illustrant la sensibilité des fonctions de hachage.

Calculer ce hash est relativement rapide sur un ordinateur moderne, mais trouver une entrée qui produit un hash spécifique n'est aujourd'hui pas faisable en un temps raisonnable avec la puissance de calcul actuelle, ce qui rend les fonctions de hachage très utiles pour la sécurité et l'intégrité des données.

Dans le cas de notre coffre, pour le fermer l'idée est de prendre le contenu (du texte) et de calculer le hash, mais pour rendre la tâche plus difficile, on ajoute un nombre aléatoire (appelé "nonce") au texte avant de calculer le hash. On répète ce processus en changeant le nonce jusqu'à ce que le hash résultant commence par un certain nombre de zéros (ce qui est difficile à trouver). Cela nécessite beaucoup de calculs, d'où l'idée d'un "effort surhumain".

Si vous voulez rajouter un nombre après `BONJOUR!` pour que le hash commence par six zéros, vous pouvez essayer différentes valeurs jusqu'à trouver la bonne. Par exemple :

```bash
$ echo -n 'BONJOUR!10225210' | sha256sum
0000005a5de15142614343334960cf4345f45a97d5943c674f78ea6fd649ea3f
```

Le programme [`sha256-zeros.py`](sha256-zeros.py) automatise ce processus en cherchant le nonce approprié pour vous. Vous pouvez constater si vous exécutez le script qu'il prend un certain temps pour trouver le bon nonce, illustrant la difficulté de ce processus. Plus on veut de zéros au début du hash, plus le temps de calcul augmente exponentiellement.

Avec les Bitcoin on appelle cela la preuve de travail (proof of work), et c'est ce mécanisme qui sécurise la blockchain contre les attaques et garantit l'intégrité des transactions. Il faut une puissance de calcul considérable pour trouver le nonce correct, ce qui rend les attaques coûteuses et peu pratiques. Ce sont des centaines de miliers d'ordinateurs à travers le monde qui participent à ce processus de minage pour sécuriser le réseau Bitcoin. Personne ne sait qui va réussir à trouver le nonce en premier, mais celui qui y parvient est récompensé par de nouveaux bitcoins.

## Git

Git est un système de gestion de versions distribué qui permet aux développeurs de suivre les modifications apportées à leur code source au fil du temps. Il a été créé par Linus Torvalds en 2005 pour gérer le développement du noyau Linux.

Il est basé sur le concept de la blockchain dans le sens où chaque commit (modification enregistrée) dans Git est lié au commit précédent par un hash SHA-1. Cela garantit l'intégrité de l'historique des modifications, car toute altération d'un commit précédent changerait son hash, rompant ainsi la chaîne.

### Plomberie

La commande Git `git cat-file -p <hash>` permet d'afficher le contenu d'un objet Git (commit, arbre, blob, etc.) en utilisant son hash. C'est un outil de "plomberie" qui permet d'explorer les objets internes de Git. Essayons de jouer avec :

```bash
$ git init .
$ echo "Hello, World!" > hello.txt
$ git add hello.txt
$ git commit -m "Initial commit"
$ tree .git
.git
├── objects
│   ├── 325a58471ef76c9b31976ad6269dab5ec17d73e1
│   ├── 8ab686eafeb1f44702738c8b0f24f2567c36da6d
│   └── bc225ea23f53f06c0c5bd3ba2be85c2120d68417
└── refs
    ├── heads
    │   └── main
    └── tags
```

On obtiens dans le dossier `.git/objects/` trois fichiers. Ce sont les objets Git qui représentent notre commit, l'arbre (tree) et le blob (le contenu du fichier). On peut utiliser `git cat-file -p <hash>` pour afficher leur contenu :

```bash
$ git cat-file -p 325a
tree bc225ea23f53f06c0c5bd3ba2be85c2120d68417
author Yves Chevallier <yves.chevallier@heig-vd.ch> 1761846891 +0100
committer Yves Chevallier <yves.chevallier@heig-vd.ch> 1761846891 +0100

Initial commit

$ git cat-file -p bc225ea23f53
100644 blob 8ab686eafeb1f44702738c8b0f24f2567c36da6d    hello.txt

$ git cat-file -p 8ab686eafeb1f44702738c8b0f24f2567c36da6d
Hello, World!
```

Ainsi, on peut voir comment Git utilise les fonctions de hachage pour lier les objets entre eux et garantir l'intégrité de l'historique des modifications. Chaque commit référence un arbre, qui à son tour référence des blobs (fichiers), créant une structure en chaîne similaire à une blockchain.

### Commandes principales
