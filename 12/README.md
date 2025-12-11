# Semaine 12/16

- [ ] Quiz 
  - [ ] Regex
  - [ ] Formats de sérialisation
- [ ] SQL Lite
- [ ] Projet

## Formats de sérialisation

La sérialisation est le processus de conversion d'une structure de données ou d'un objet en un format qui peut être facilement stocké ou transmis, puis reconstruit ultérieurement. Les formats de sérialisation couramment utilisés incluent JSON, XML, YAML, et CSV.

### Lequel choisir ?

XML: Utile pour les documents avec une structure hiérarchique complexe. Souvent utilisé dans les services web et les configurations. Il est de moins en moins populaire pour les nouvelles applications en raison de sa verbosité et de la difficulté de lecture par rapport à d'autres formats.

JSON: Très populaire pour les applications web et les API. Facile à lire et à écrire pour les humains, et largement supporté par de nombreux langages de programmation. Idéal pour les échanges de données entre un client et un serveur. C'est par exemple le format de sérialisation par défaut dans vscode pour les paramètres utilisateur.

YAML: Lisible par l'homme et souvent utilisé pour les fichiers de configuration. Supporte des structures de données complexes, mais peut être plus difficile à analyser correctement en raison de sa dépendance à l'indentation. Utile lorsque la lisibilité est une priorité.

TOML: Conçu pour être simple et facile à lire, souvent utilisé pour les fichiers de configuration. Moins courant que JSON ou YAML, mais gagne en popularité pour les configurations d'applications. Il a été choisi par défaut par uv et poetry pour leurs fichiers de configuration (pyproject.toml).

CSV: Simple et largement utilisé pour les données tabulaires. Facile à lire et à écrire, mais limité aux structures de données simples. Idéal pour les échanges de données entre des applications, notamment dans les contextes de feuilles de calcul et de bases de données.

### XML

Extensible Markup Language (XML) est un langage de balisage qui définit un ensemble de règles pour l'encodage des documents dans un format lisible par l'homme et par la machine.

Il est utilisé notamment par HTML et dans de nombreux protocoles de communication, par exemple les flux RSS:

```xml
<person>
    <name>Alice</name>
    <age>30</age>
    <city>Wonderland</city>
</person>
```

### JSON

JavaScript Object Notation (JSON) est un format léger d'échange de données, facile à lire et à écrire pour les humains, et facile à analyser et à générer pour les machines.

```js
const data = {
    name: "Alice",
    age: 30,
    city: "Wonderland"
};
const array = [1, 2, 3, 4, 5];
```

```json 
{
    "name": "Alice",
    "age": 30,
    "city": "Wonderland",
    "numbers": [1, 2, 3, 4, 5]
}
```

### YAML

YAML Ain't Markup Language (YAML) est un format de sérialisation de données lisible par l'homme, souvent utilisé pour les fichiers de configuration et dans les applications où les données sont stockées ou transmises.

```yaml
cities: 
  - Paris
  - London:
      population: 9 million
      country: UK
  - New York
people:
  - name: Alice
    age: 30
    city: Wonderland
  - name: Bob
    age: 25
    city: Builderland
date: 2024-06-15
complex: !!python/complex '1+2j'
int: 42
float: 3.14
boolean: true
null_value: null
reference: &ref_anchor
  key: value
alias: *ref_anchor
long_text: |
    Ceci est un texte sur
    plusieurs lignes.
long_continuous_text: >
    Ceci est un texte sur
    plusieurs lignes, mais
    il sera traité comme
    une seule ligne.
```

### TOML

Tom's Obvious, Minimal Language (TOML) est un format de fichier de configuration conçu pour être facile à lire et à écrire par les humains, tout en étant simple à analyser pour les machines.

```toml
[people]
[[people.person]]
name = "Alice"
age = 30
city = "Wonderland"

[[people.person]]
name = "Bob"
age = 25
city = "Builderland"
```

### CSV

Comma-Separated Values (CSV) est un format de fichier simple utilisé pour stocker des données tabulaires, où chaque ligne représente un enregistrement et chaque valeur est séparée par une virgule (ou un autre délimiteur).

```csv
name,age,city
Alice,30,Wonderland
Bob,25,Builderland
```

## SQL Lite

SQLite est un système de gestion de base de données relationnelle léger et autonome. Il est intégré dans de nombreuses applications et systèmes d'exploitation en raison de sa simplicité et de sa portabilité.

Il utilise le langage SQL (Structured Query Language) pour gérer et manipuler les données. 

Exemple d'un programme qui crée une base de données pour stocker des utilisateurs associés à des villes. Deux tables : people and cities. On démontre l'insertion de données et une requête de sélection avec jointure.

```py
import sqlite3

# Connexion à la base de données (ou création si elle n'existe pas)
conn = sqlite3.connect('example.db')
c = conn.cursor()
# Création des tables
c.execute('''CREATE TABLE IF NOT EXISTS cities
             (id INTEGER PRIMARY KEY, name TEXT)''')
c.execute('''CREATE TABLE IF NOT EXISTS people
             (id INTEGER PRIMARY KEY, name TEXT, age INTEGER, city_id INTEGER,
              FOREIGN KEY(city_id) REFERENCES cities(id))''')
# Insertion de données
c.execute("INSERT INTO cities (name) VALUES ('Wonderland')")
c.execute("INSERT INTO people (name, age, city_id) VALUES ('Alice', 30, 1)")
# Requête de sélection avec jointure
c.execute('''SELECT people.name, people.age, cities.name
             FROM people
             JOIN cities ON people.city_id = cities.id''')
rows = c.fetchall()
for row in rows:
    print(row)
# Fermeture de la connexion
conn.commit()
conn.close()
```
