# Semaine 05/16

## IPython

### Run

IPython dispose de plusieurs commandes magiques commencant par `%`. Par exemple `%run` permet d'exécuter un script Python.

```python
%run script.py
```

C'est très pratique pour tester votre programme. 

### Autoreload

IPython dispose d'extensions. L'extension `autoreload` permet de recharger automatiquement les modules Python avant l'exécution de la ligne de commande.

```python
%load_ext autoreload
%autoreload 2
```

À partir de cet instant vous pouvez modifier vos modules Python sans avoir à redémarrer le noyau IPython.