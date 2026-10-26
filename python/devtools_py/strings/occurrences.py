from typing import cast


def compterNombreOccurences(
    monMot: str,
    onlyThisChar: list[str] | None = None
) -> list[list[str | int]]:
    """
    Compte le nombre d'occurrences de chaque caractère dans 'monMot'.
    Si 'onlyThisChar' est fourni, ne compte que les caractères présents dans cette liste.
    Retourne une liste de paires [caractere, nbOccurences], ex: [['A', 2], ['B', 1]].
    """
    listeOccurences: list[list[str | int]] = []
    caracteresCibles: list[str] = []
    caractere: str
    caractereMot: str
    compteur: int

    if onlyThisChar is not None:
        caracteresCibles = onlyThisChar
    else:
        for caractere in monMot:
            if caractere not in caracteresCibles:
                caracteresCibles.append(caractere)

    for caractere in caracteresCibles:
        compteur = 0
        for caractereMot in monMot:
            if caractereMot == caractere:
                compteur += 1
        listeOccurences.append([caractere, compteur])

    return listeOccurences


def enleverOccurence(
    listeOccurences: list[list[str | int]],
    lettre: str
) -> list[list[str | int]]:
    """
    Décrémente de 1 le compteur d'occurrences associé à 'lettre' dans 'listeOccurences'.
    """
    paire: list[str | int]
    valeurActuelle: int

    for paire in listeOccurences:
        if paire[0] == lettre:
            valeurActuelle = cast(int, paire[1])
            paire[1] = valeurActuelle - 1

    return listeOccurences


def ajouterOccurence(
    listeOccurences: list[list[str | int]],
    lettre: str
) -> list[list[str | int]]:
    """
    Incrémente de 1 le compteur d'occurrences associé à 'lettre' dans 'listeOccurences'.
    """
    paire: list[str | int]
    valeurActuelle: int

    for paire in listeOccurences:
        if paire[0] == lettre:
            valeurActuelle = cast(int, paire[1])
            paire[1] = valeurActuelle + 1

    return listeOccurences


def verifierStockDispo(listeOccurences: list[list[str | int]], lettre: str) -> bool:
    """
    Retourne True si 'lettre' est présente dans 'listeOccurences' avec un compteur strictement positif.
    """
    stockDispo: bool = False
    paire: list[str | int]
    nbRestant: int

    for paire in listeOccurences:
        if paire[0] == lettre:
            nbRestant = cast(int, paire[1])
            if nbRestant > 0:
                stockDispo = True

    return stockDispo
