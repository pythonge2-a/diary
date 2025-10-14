# Semaine 03/16

## Classes 

Une classe est un "plan de construction" pour créer des objets. Elle définit des attributs (données) et des méthodes (fonctions) qui caractérisent le comportement de ces objets.

En python chaque classe peut faire référence à ses membres via le mot-clé `self`.

## Itérateurs et générateurs

- `__iter__` permet de rendre un objet itérable via une boucle `for` par exemple. Cette boucle appelle secrètement la méthode `__iter__` pour obtenir un itérateur. 
- `__next__` est une méthode qui doit être définie dans un itérateur. Elle est appelée pour obtenir le prochain élément de la séquence. Si la séquence est épuisée, elle doit lever l'exception `StopIteration`.

