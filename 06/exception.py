

def expectEvenNumber(a):
    if a % 2 != 0:
        raise Exception("Number is not even")
    return a

try:
    # Essaie d'exécuter la fonction
    print(expectEvenNumber(3))
except Exception as e:
    # Attrappe l'exception et affiche le message
    print(e)
