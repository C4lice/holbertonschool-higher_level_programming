#!/usr/bin/python3
"""
Ce module contient la fonction matrix_divided.
"""

def matrix_divided(matrix, div):
    """
    Divise tous les éléments d'une matrice par div et renvoie une nouvelle
    matrice avec chaque élément arrondi à 2 décimales.

    Args :
        matrix (liste de listes de int/float) : La matrice à diviser.
        div (int/float) : Le nombre par lequel diviser les éléments de la matrice.

    Retourne :
        liste de listes de flottants : Une nouvelle matrice
        dont chaque élément est divisé par div.

    Lance :
        TypeError : Si la matrice n'est pas une liste de listes
        d'entiers/floats ou
                   si div n'est pas un nombre, ou si
                   les lignes de la matrice ne sont pas de taille égale.
        ZeroDivisionError : Si div est égal à zéro.
    """
    
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
    
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    # Create a new matrix with divided elements rounded to 2 decimal places
    return [[round(num / div, 2) for num in row] for row in matrix]
