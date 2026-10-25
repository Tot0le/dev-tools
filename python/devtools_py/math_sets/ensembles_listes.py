from random import randint
from typing import Any


def genererListeValeurEntierAleatoire(nombre: int, borneMin: int, borneMax: int) -> list[int]:
    """
    Fonction qui génère une liste de valeurs entières aléatoires entre 2 bornes données.
    """
    liste: list[int] = []

    for _ in range(nombre):
        liste.append(randint(borneMin, borneMax))

    return liste


def nbElementUniqueDansListe(liste: list[int]) -> int:
    """
    Fonction qui renvoie le nombre d'éléments en doublon dans une liste.
    """
    elementUnique: list[Any] = []
    indiceElement: int
    indiceIteraElement: int
    compteurElementUnique: int = 0

    for indiceElement in range(len(liste) + 1):
        for indiceIteraElement in range(indiceElement + 1, len(liste)):
            if (
                liste[indiceElement] == liste[indiceIteraElement]
                and liste[indiceElement] not in elementUnique
                and liste[indiceIteraElement] not in elementUnique
            ):
                elementUnique.append(liste[indiceElement])
                compteurElementUnique += 1

    return compteurElementUnique


def estUnEnsemble(liste: list[int]) -> bool:
    """
    Renvoie True si la liste n'a pas de doublons.
    """
    resultat: bool = False

    if nbElementUniqueDansListe(liste) == 0:
        resultat = True

    return resultat


def rajoutSiPasDedans(valeur: int, liste: list[int]) -> list[int]:
    """
    Rajoute la valeur en entrée dans la liste si elle n'est pas déjà dedans.
    Lève une ValueError si la liste n'est pas un ensemble.
    """
    if not estUnEnsemble(liste):
        raise ValueError("Erreur, la liste donnée n'est pas un ensemble")

    if valeur not in liste:
        liste.append(valeur)

    return liste


def union(liste1: list[int], liste2: list[int]) -> list[int]:
    """
    Fonction qui renvoie l'union des deux listes en entrée.
    """
    listeUnion: list[int] = liste1
    element: int

    for element in liste2:
        listeUnion = rajoutSiPasDedans(element, listeUnion)

    return listeUnion


def intersection(liste1: list[int], liste2: list[int]) -> list[int]:
    """
    Fonction qui renvoie l'intersection des deux listes en entrée.
    """
    listeIntersection: list[int] = []
    element: int

    for element in liste1:
        if element in liste2:
            listeIntersection.append(element)

    return listeIntersection


def difference(liste1: list[int], liste2: list[int]) -> tuple[list[int], list[int]]:
    """
    Fonction qui renvoie les deux différences (liste1 \\ liste2 et liste2 \\ liste1).
    """
    listeDiff1_2: list[int] = liste1.copy()
    listeDiff2_1: list[int] = liste2.copy()
    element: int

    for element in liste2:
        if element in listeDiff1_2:
            listeDiff1_2.remove(element)

    for element in liste1:
        if element in listeDiff2_1:
            listeDiff2_1.remove(element)

    return listeDiff1_2, listeDiff2_1


def disjointes(liste1: list[int], liste2: list[int]) -> bool:
    """
    Fonction renvoyant un booléen indiquant si les deux listes sont disjointes.
    """
    sontDisjointes: bool = True
    indElement: int = 0

    while sontDisjointes and indElement < len(liste1):
        if liste1[indElement] in liste2:
            sontDisjointes = False
        indElement += 1

    return sontDisjointes
