def compterNombreOccurences(
    monMot: str,
    onlyThisChar: list[str] | None = None
) -> list[list[str | int]]:
    """
    Fonction générant une liste de listes [caractere, nbOccurences].
    Exemple de retour : [['A', 2], ['B', 1]]
    """
    listeOccurences: list[list[str | int]] = []
    compteur: int
    listeCaractereDejaTraites: list[str]
    caractereACompter: str
    caractereDansMot: str
    caractere: str
    caractereBis: str

    if onlyThisChar is not None:
        for caractereACompter in onlyThisChar:
            compteur = 0
            for caractereDansMot in monMot:
                if caractereDansMot == caractereACompter:
                    compteur += 1

            listeOccurences.append([caractereACompter, compteur])
    else:
        listeCaractereDejaTraites = []
        for caractere in monMot:
            if caractere not in listeCaractereDejaTraites:
                compteur = 0
                for caractereBis in monMot:
                    if caractere == caractereBis:
                        compteur += 1

                listeCaractereDejaTraites.append(caractere)
                listeOccurences.append([caractere, compteur])

    return listeOccurences


def enleverOccurence(
    listeOccurences: list[list[str | int]],
    lettre: str
) -> list[list[str | int]]:
    """
    Cherche la lettre et fait -1 sur son occurrence.
    """
    listeLettAndOcc: list[str | int]

    for listeLettAndOcc in listeOccurences:
        if listeLettAndOcc[0] == lettre:
            listeLettAndOcc[1] = int(listeLettAndOcc[1]) - 1

    return listeOccurences


def ajouterOccurence(
    listeOccurences: list[list[str | int]],
    lettre: str
) -> list[list[str | int]]:
    """
    Cherche la lettre et fait +1 sur son occurrence.
    """
    listeLettAndOcc: list[str | int]

    for listeLettAndOcc in listeOccurences:
        if listeLettAndOcc[0] == lettre:
            listeLettAndOcc[1] = int(listeLettAndOcc[1]) + 1

    return listeOccurences


def verifierStockDispo(listeOccurences: list[list[str | int]], lettre: str) -> bool:
    """
    Renvoie Vrai si la lettre existe et qu'il en reste au moins 1.
    """
    stockDispo: bool = False
    listeLettAndOcc: list[str | int]

    for listeLettAndOcc in listeOccurences:
        if listeLettAndOcc[0] == lettre and int(listeLettAndOcc[1]) > 0:
            stockDispo = True

    return stockDispo
