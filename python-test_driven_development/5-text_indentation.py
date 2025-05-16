#!/usr/bin/python3
"""
Ce module contient la fonction text_indentation.
"""

def text_indentation(text):
    """
    Imprime un texte avec deux nouvelles lignes après chacun
    des caractères suivants : '.', '?', ':'.

    Args :
        text (str) : Le texte à traiter.

    L'erreur est levée :
        TypeError : Si le texte n'est pas une chaîne de caractères.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text) and text[i] == ' ':
        i += 1

    while i < len(text):
        print(text[i], end="")
        if text[i] == "\n" or text[i] in ".?:":
            if text[i] in ".?:":
                print("\n")
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        i += 1
