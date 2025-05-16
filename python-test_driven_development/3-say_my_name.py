#!/usr/bin/python3
"""
Ce module contient la fonction say_my_name.
"""

def say_my_name(first_name, last_name=""):
    """
    Imprime "Mon nom est <prénom> <nom>".

    Args :
        first_name (str) : Le prénom.
        last_name (chaîne, facultatif) : Le nom de famille.
        La valeur par défaut est une chaîne vide.

    L'erreur est levée :
        TypeError : Si first_name ou last_name
        n'est pas une chaîne de caractères.
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
