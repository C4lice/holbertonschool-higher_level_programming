#!/usr/bin/python3
def roman_to_int(roman_string):
    # Vérification de la présence d'une chaîne de caractères romains incorrecte
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    # Inversion de la chaîne romaine pour faciliter son traitement
    rom = list(reversed(roman_string))

    conv = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    res = conv[rom[0]]  # Commencer par la première valeur de la chaîne inversée

    # Boucle sur la chaîne romaine inversée en commençant par le deuxième élément
    for i in range(1, len(rom)):
        # Si le chiffre actuel est inférieur au précédent, soustraire sa valeur
        if conv[rom[i]] < conv[rom[i - 1]]:
            res -= conv[rom[i]]
        else:
            # Sinon, il suffit d'ajouter sa valeur
            res += conv[rom[i]]

    return res
