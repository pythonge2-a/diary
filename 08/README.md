# Semaine 08/16

- [ ] Pandas

## Pandas

Pandas est une librairie Python qui permet de manipuler des données de manière simple et efficace. Elle est basée sur deux structures de données principales : les `Series` et les `DataFrame`.

On peut assimiler un `DataFrame` à une feuille de calcul Excel, avec des lignes et des colonnes. Les `Series` sont des colonnes de ce `DataFrame`.

Une des fonction les plus puissante de Pandas sont les pivots de tableaux hérités de Excel. Un pivot de tableau permet de réorganiser les données d'un tableau pour les analyser sous un autre angle, il utilise les commande `groupby`, `pivot_table` et `crosstab`.

### Installation

Utilisez une des commandes suivantes pour installer Pandas :

```bash
pip install pandas
```

ou

```bash
sudo apt-get install python3-pandas
```

Préférez utiliser la première commande pour installer Pandas dans un environnement virtuel.

### Import

```python
import pandas as pd
import matplotlib.pyplot as plt
```

### Chargement de données dans un dataframe

```python
url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
df = pd.read_csv(url)
```

Tête et Queue du dataframe :

```python
df.head()  # Affiche les 5 premières lignes
df.tail()  # Affiche les 5 dernières lignes
df.describe()  # Affiche les statistiques descriptives
df.columns  # Affiche les noms des colonnes
```

### Groupes et aggregations

```python
df.groupby('Pclass')['Age'].mean()
df[df.Pclass == 2].groupby('Sex')['Age'].mean()
df[df.Pclass == 2].groupby('Sex')['Age'].count()
```

### Pivots et index

Index sur plusieurs colonnes ('Pclass' et 'Sex') :

```python
df.set_index(['Pclass', 'Sex']).sort_index()
df.reset_index()


du = df.pivot_table(index='Pclass', columns='Sex', values='PassengerId', aggfunc='count')
print(du)
```

### Tableaux croisés

```python
pd.crosstab(df['Pclass'], df['Survived'])
```

### Histogrammes

```python
df['Age'].plot(kind='hist', bins=30, edgecolor='black')
plt.title('Distribution des âges des passagers')
plt.xlabel('Âge')
plt.ylabel('Nombre de passagers')
plt.show()
```

```python
pd.crosstab(df['Pclass'], df['Survived']).plot(kind='bar', stacked=True)
plt.title('Nombre de survivants par classe')
plt.xlabel('Classe')
plt.ylabel('Nombre de passagers')
plt.legend(['Non survivants', 'Survivants'])
plt.show()
```

### Rechercher

On recherche tout les Margaret :

```python
df[df['Name'].str.contains('Margaret')]
```

### Modifications des données

Suppression d'une colonne:

```python
df.drop('Name', axis=1, inplace=True)
```

Suppression des NaN:

```python
df.dropna(inplace=True)
```

Conversion du type de colonne (age en int)

```python
df['Age'] = df['Age'].astype(int)
```

Ajout colonne calculée:

```python
df['FareCHF'] = df['Fare'] * 1.1
df['category'] = df['Age'].apply(lambda x: 'adult' if x > 18 else 'child')
```
