#!/usr/bin/python3
def list_division(ma_liste_1, ma_liste_2, list_length):
    resultats = []

    for i in range(list_length):
        try:
            a = ma_liste_1[i]
            b = ma_liste_2[i]
            res = a / b
        except ZeroDivisionError:
            print("division par 0")
            res = 0
        except IndexError:
            print("out of range")
            res = 0
        except TypeError:
            print("wrong type")
            res = 0
        finally:
            resultats.append(res)

    return resultats
