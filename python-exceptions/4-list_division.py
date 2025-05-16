#!/usr/bin/python3
def list_division(ma_liste_1, ma_liste_2, liste_longueur):
    resultats = []

    for i in range(liste_longueur):
        try:
            a = ma_liste_1[i]
            b = ma_liste_2[i]
            res = a / b
        except TypeError:
            print("wrong type")
            res = 0
        except ZeroDivisionError:
            print("division par 0")
            res = 0
        except IndexError:
            print("out of range")
            res = 0
        finally:
            resultats.append(res)

    return resultats
