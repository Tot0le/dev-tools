from typing import cast
from devtools_py import constante

def _convertirType(typeVoulu: str, valeur: str, msgErreurType: str) -> int | float | str | None:
    """
    Convertit une chaîne de caractères vers le type souhaité ('int', 'float', 'str').
    Affiche un message d'erreur et retourne None si la conversion échoue.
    """
    resultat: int | float | str | None = None

    match typeVoulu:
        case "float":
            try:
                resultat = float(valeur)
            except ValueError:
                print(f"Erreur : Impossible de convertir la valeur '{valeur}' en float.")
                print(msgErreurType)
                resultat = None

        case "int":
            try:
                resultat = int(valeur)
            except ValueError:
                print(f"Erreur : Impossible de convertir la valeur '{valeur}' en int.")
                print(msgErreurType)
                resultat = None

        case "str":
            resultat = valeur

        case _:
            print(f"Erreur : Le type '{typeVoulu}' n'est pas géré. (Choix : float, int, str)")
            resultat = None

    return resultat


def _estDansIntervalle(
    valeur: int | float,
    borneMin: int | float,
    borneMax: int | float,
    minInclus: bool,
    maxInclus: bool
) -> bool:
    """
    Vérifie si une valeur numérique respecte les bornes minimale et maximale.
    """
    respecteMin: bool = (valeur >= borneMin) if minInclus else (valeur > borneMin)
    respecteMax: bool = (valeur <= borneMax) if maxInclus else (valeur < borneMax)
    estValide: bool = respecteMin and respecteMax

    return estValide


def saisieFloat(
    message: str = "Veuillez saisir une valeur réelle : ",
    msgErreur: str = "Erreur de saisie, veuillez saisir une valeur réelle valide : ",
    borneMin: float = constante.MINFLOAT,
    borneMax: float = constante.MAXFLOAT,
    MinInclus: bool = True,
    MaxInclus: bool = True
) -> float:
    """
    Demande à l'utilisateur de saisir un nombre réel compris dans l'intervalle spécifié.
    Redemande la saisie tant que le type ou les bornes ne sont pas respectés.
    """
    msgErreurType: str = "Veuillez saisir un nombre réel, pas une chaîne de caractères."
    valeurStr: str = input(message)
    valeurConvertie: int | float | str | None = _convertirType("float", valeurStr, msgErreurType)
    valeurFloat: float
    estValide: bool = False
    resultat: float = 0.0

    while not estValide:
        if valeurConvertie is not None:
            valeurFloat = cast(float, valeurConvertie)
            if _estDansIntervalle(valeurFloat, borneMin, borneMax, MinInclus, MaxInclus):
                resultat = valeurFloat
                estValide = True

        if not estValide:
            valeurStr = input(msgErreur)
            valeurConvertie = _convertirType("float", valeurStr, msgErreurType)

    return resultat


def saisieEntier(
    message: str = "Veuillez saisir une valeur entière : ",
    msgErreur: str = "Erreur de saisie, veuillez saisir une valeur entière valide : ",
    borneMin: int = constante.MININT,
    borneMax: int = constante.MAXINT,
    MinInclus: bool = True,
    MaxInclus: bool = True
) -> int:
    """
    Demande à l'utilisateur de saisir un nombre entier compris dans l'intervalle spécifié.
    Redemande la saisie tant que le type ou les bornes ne sont pas respectés.
    """
    msgErreurType: str = "Veuillez saisir un nombre entier, pas une chaîne de caractères ni un réel."
    valeurStr: str = input(message)
    valeurConvertie: int | float | str | None = _convertirType("int", valeurStr, msgErreurType)
    valeurInt: int
    estValide: bool = False
    resultat: int = 0

    while not estValide:
        if valeurConvertie is not None:
            valeurInt = cast(int, valeurConvertie)
            if _estDansIntervalle(valeurInt, borneMin, borneMax, MinInclus, MaxInclus):
                resultat = valeurInt
                estValide = True

        if not estValide:
            valeurStr = input(msgErreur)
            valeurConvertie = _convertirType("int", valeurStr, msgErreurType)

    return resultat


def _verifStrInL(chaine: str, listValidChaine: list[str], msgErreur: str) -> str:
    """
    Vérifie si la chaîne saisie appartient à la liste des choix autorisés.
    """
    while chaine not in listValidChaine:
        chaine = input(msgErreur)

    return chaine


def saisieStr(listValidChaine: list[str], message: str, msgErreur: str) -> str:
    """
    Demande à l'utilisateur de saisir une chaîne de caractères parmi une liste de choix valides.
    """
    chaine: str = input(message)
    chaine = _verifStrInL(chaine, listValidChaine, msgErreur)

    return chaine


def saisieChaineCaractereInterdit(
    message: str,
    msgErreur: str,
    caracteresInterdit: list[str] | None = None
) -> str:
    """
    Demande une chaîne de caractères ne contenant aucun des caractères interdits fournis.
    """
    chaine: str = input(message).strip()
    estValide: bool = False
    caracInterdit: str
    listeInterdits: list[str] = caracteresInterdit if caracteresInterdit is not None else []

    while not estValide:
        estValide = True
        for caracInterdit in listeInterdits:
            if caracInterdit in chaine:
                estValide = False
        if not estValide:
            chaine = input(msgErreur).strip()

    return chaine


def saisieYesOrNO(message: str) -> bool:
    """
    Demande une confirmation (oui/non ou yes/no) à l'utilisateur.
    Retourne True pour une réponse positive, False pour une réponse négative.
    """
    enAccord: bool = False
    aRepondu: bool = False
    reponse: str
    reponsesVrai: list[str] = ["oui", "o", "yes", "y"]
    reponsesFaux: list[str] = ["non", "n", "no"]

    reponse = input(message).strip().lower()
    while not aRepondu:
        if reponse in reponsesVrai:
            enAccord = True
            aRepondu = True
        elif reponse in reponsesFaux:
            enAccord = False
            aRepondu = True
        else:
            print(f"Saisie incorrecte, choix acceptés : {reponsesVrai} ou {reponsesFaux}")
            reponse = input(message).strip().lower()

    return enAccord
