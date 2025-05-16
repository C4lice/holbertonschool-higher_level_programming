#!/usr/bin/python3
"""
Ce module contient la fonction add_integer.
"""

def add_integer(a, b=98):
    '''
    Additionne deux nombres entiers ou flottants et renvoie
    le résultat sous la forme d'un nombre entier.

    Paramètres :
    a (int ou float) : Le premier nombre.
    b (int ou float, optionnel) : Le deuxième nombre, par défaut 98.

    Retourne :
    int : La somme des deux nombres, convertie en un entier.

    Lance :
    TypeError : Si `a` ou `b` n'est pas un entier ou un flottant.
    '''

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Transformer les flottants en entiers
    a = int(a)
    b = int(b)

    return a + b
