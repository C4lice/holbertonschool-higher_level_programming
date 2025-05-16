#!/usr/bin/python3
"""
Ce module contient la fonction print_square.
"""

def print_square(size):
    """
    Imprime un carré avec le caractère # en fonction de la taille fournie.

    Args :
        size (int) : La taille et la longueur du carré.

    L'erreur est levée :
        TypeError : Si size n'est pas un entier.
        Erreur de valeur : Si la taille est inférieure à 0.
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    
    if size < 0:
        raise ValueError("size must be >= 0")
    
    for _ in range(size):
        print("#" * size)
