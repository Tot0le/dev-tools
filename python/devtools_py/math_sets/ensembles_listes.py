from random import randint


def genererListeValeurEntierAleatoire(nombre: int, borneMin: int, borneMax: int) -> list[int]:
    """
    Génère une liste de 'nombre' entiers aléatoires compris entre 'borneMin' et 'borneMax' inclus.
    """
    liste: list[int] = []

    for _ in range(nombre):
        liste.append(randint(borneMin, borneMax))

    return liste


def nbValeursEnDoublon(liste: list[int]) -> int:
    """
    Retourne le nombre de valeurs qui apparaissent plusieurs fois (en doublon) dans la liste.
    """
    valeursDoublons: list[int] = []
    indiceElement: int
    indiceComparaison: int
    compteurDoublons: int = 0

    for indiceElement in range(len(liste)):
        for indiceComparaison in range(indiceElement + 1, len(liste)):
            if (
                liste[indiceElement] == liste[indiceComparaison]
                and liste[indiceElement] not in valeursDoublons
            ):
                valeursDoublons.append(liste[indiceElement])
                compteurDoublons += 1

    return compteurDoublons


def nbElementUniqueDansListe(liste: list[int]) -> int:
    """
    Retourne le nombre de valeurs distinctes présentes dans la liste.
    """
    elementsVus: list[int] = []
    element: int

    for element in liste:
        if element not in elementsVus:
            elementsVus.append(element)

    nbUniques: int = len(elementsVus)
    return nbUniques


def estUnEnsemble(liste: list[int]) -> bool:
    """
    Retourne True si la liste est un ensemble (ne contient aucun doublon), False sinon.
    """
    resultat: bool = nbValeursEnDoublon(liste) == 0
    return resultat


def rajoutSiPasDedans(valeur: int, liste: list[int]) -> list[int]:
    """
    Ajoute 'valeur' dans 'liste' si elle n'y est pas déjà présente.
    Lève une ValueError si la liste fournie n'est pas un ensemble (contient des doublons).
    """
    nouvelleListe: list[int] = liste.copy()

    if not estUnEnsemble(nouvelleListe):
        raise ValueError("Erreur : la liste donnée n'est pas un ensemble (elle contient des doublons).")

    if valeur not in nouvelleListe:
        nouvelleListe.append(valeur)

    return nouvelleListe


def union(liste1: list[int], liste2: list[int]) -> list[int]:
    """
    Retourne l'union de deux listes représentant des ensembles.
    Lève une ValueError si l'une des listes contient des doublons.
    """
    if not estUnEnsemble(liste1) or not estUnEnsemble(liste2):
        raise ValueError("Erreur : les deux listes doivent être des ensembles sans doublons.")

    listeUnion: list[int] = liste1.copy()
    element: int

    for element in liste2:
        listeUnion = rajoutSiPasDedans(element, listeUnion)

    return listeUnion


def intersection(liste1: list[int], liste2: list[int]) -> list[int]:
    """
    Retourne l'intersection (éléments communs) de deux listes représentant des ensembles.
    Lève une ValueError si l'une des listes contient des doublons.
    """
    if not estUnEnsemble(liste1) or not estUnEnsemble(liste2):
        raise ValueError("Erreur : les deux listes doivent être des ensembles sans doublons.")

    listeIntersection: list[int] = []
    element: int

    for element in liste1:
        if element in liste2:
            listeIntersection.append(element)

    return listeIntersection


def difference(liste1: list[int], liste2: list[int]) -> tuple[list[int], list[int]]:
    """
    Retourne un tuple contenant les deux différences symétriques : (liste1 \\ liste2, liste2 \\ liste1).
    Lève une ValueError si l'une des listes contient des doublons.
    """
    if not estUnEnsemble(liste1) or not estUnEnsemble(liste2):
        raise ValueError("Erreur : les deux listes doivent être des ensembles sans doublons.")

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
    Retourne True si les deux ensembles sont disjoints (aucun élément en commun), False sinon.
    Lève une ValueError si l'une des listes contient des doublons.
    """
    if not estUnEnsemble(liste1) or not estUnEnsemble(liste2):
        raise ValueError("Erreur : les deux listes doivent être des ensembles sans doublons.")

    sontDisjointes: bool = True
    indElement: int = 0

    while sontDisjointes and indElement < len(liste1):
        if liste1[indElement] in liste2:
            sontDisjointes = False
        indElement += 1

    return sontDisjointes
