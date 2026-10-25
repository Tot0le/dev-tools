from math import sqrt


def estPremier(nombre: int) -> bool:
    """
    Fonction qui renvoie vrai si le nombre donné est premier, faux sinon.
    """
    i: int
    resultat: bool

    if nombre <= 1:
        resultat = False
    else:
        resultat = True
        i = 2
        while i <= sqrt(nombre) and resultat:
            if nombre % i == 0:
                resultat = False
            i += 1

    return resultat


def fibonacci_iterative(k: int) -> int:
    """
    Fonction itérative qui calcule le k-ième élément de Fibonacci.
    """
    valeur: int = 1
    Un: int = 0
    Un1: int = 1
    Un2: int

    if k == 0:
        valeur = 0
    elif k == 1:
        valeur = Un1
    else:
        for _ in range(2, k + 1):
            Un2 = Un + Un1
            valeur = Un + Un1
            Un = Un1
            Un1 = Un2

    return valeur


def fibonacci_recursive(k: int) -> int:
    """
    Fonction récursive qui calcule le k-ième élément de Fibonacci.
    """
    resultat: int

    if k == 1:
        resultat = 1
    elif k == 0:
        resultat = 0
    else:
        resultat = fibonacci_recursive(k - 1) + fibonacci_recursive(k - 2)

    return resultat


def factorielle(nombre: int) -> int:
    """
    Fonction retournant la valeur factorielle du nombre en entrée.
    """
    resultat: int

    if nombre <= 1:
        resultat = 1
    else:
        resultat = nombre * factorielle(nombre - 1)

    return resultat
