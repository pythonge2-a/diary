# Semaine 03/16

- [x] Comment intéragir avec les arguments et l'entrée standard
- [x] Utilisation de `sys.argv` (moche)
- [x] C'est quoi un décorateurs (`@decorator`)
- [x] Click pour faire des CLI

## Arguments

Il est possible de récupérer les arguments passés à un script Python en utilisant la variable `sys.argv` du module `sys`. C'est une liste qui contient les arguments passés au script. Le premier élément est le nom du script lui-même.

```python
import sys

for arg in sys.argv:
    print(arg)
```

La gestion des arguments est néanmoins compliquée et il est préférable d'utiliser une librairie comme `argparse` ou `click`.

## Décorateurs

Un décorateur est une fonction qui prend une autre fonction en argument et qui retourne une nouvelle fonction. Cela permet d'ajouter des fonctionnalités à une fonction sans la modifier.

C'est une manière d'emballer une fonction dans une autre fonction. Cela permet de factoriser du code.

Voici un exemple de décorateur qui affiche `Before` et `After` avant et après l'exécution d'une fonction:

```python
def my_decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper


@my_decorator
def say_hello():
    print("Hello")
```

Lorsque `say_hello` est appelée, c'est en fait `wrapper` qui est exécutée. Cela permet d'ajouter des fonctionnalités à `say_hello` sans la modifier.

## Click

Click est une librairie pour créer des interfaces en ligne de commande (CLI) en Python. Vous pouvez l'installer avec:

```bash
$ pip install click
```

Elle est très simple à utiliser et permet de créer des CLI rapidement notamment le support de :

- Les options (options courtes et longues avec ou sans valeurs)
- La validation des options (types, valeurs, etc.)
- Les arguments positionnels
- La coloration de la sortie
- La gestion des erreurs
- La génération de l'aide
- Les barres de progression
- Les prompts
- ...

Voici un exemple de base:

```python
import click
import time

@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name',
              help='The person to greet.')
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo(f"Hello {name}!")
    with click.progressbar([1, 2, 3]) as bar:
        for x in bar:
            print(f"sleep({x})...")
            time.sleep(x)

if __name__ == '__main__':
    hello()
```
