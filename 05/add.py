"""Un module est un fichier python, avec des fonctions, des classes, etc."""

def add(a,b):
    """Retourne la somme de a et b"""
    return a + b

# Ici un problème car à chaque importation du module, le print s'exécute
# On n'utilise donc jamais du code exécutable dans un module
# On utilise un "truc" spécial : __name__
# Si le module est exécuté directement, __name__ vaut "__main__"
#
# if __name__ == "__main__":
#     print("Heee salut !, tu m'as exécuté ?")
print("Heee salut !, tu m'as importé ?")
