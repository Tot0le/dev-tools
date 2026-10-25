from typing import cast
from devtools_py import constante


def _convertirType(type_voulu: str, valeur: str, monMessageTypeErreur: str) -> int | float | str | None:
    """
    Fonction interne qui convertit la 'valeur' (str) en le 'type_voulu' (str: "int", "float", "str")
    et gère les erreurs de conversion.

    Retourne la valeur convertie, ou None si la conversion a échoué.
    """
    resultat: int | float | str | None = None

    match type_voulu:
        case "float":
            try:
                resultat = float(valeur)
            except ValueError:
                print(f"Erreur : Impossible de convertir la valeur '{valeur}' en float.")
                print(monMessageTypeErreur)
                resultat = None

        case "int":
            try:
                resultat = int(valeur)
            except ValueError:
                print(f"Erreur : Impossible de convertir la valeur '{valeur}' en int.")
                print(monMessageTypeErreur)
                resultat = None

        case "str":
            print("Utiliser la fonction saisieStr est mieux.")
            resultat = valeur

        case _:
            print(f"Erreur : Le type '{type_voulu}' n'est pas géré. (Choix : float, int, str)")
            resultat = None

    return resultat


def _verifFloat(
    valeur: float,
    msgErreur: str,
    borneMin: float,
    borneMax: float,
    MinInclus: bool,
    MaxInclus: bool
) -> float:
    """
    Verifie si un reel est bien dans un intervalle donne.
    """
    maValeurStr: str = str(valeur)
    messageTypeErreur: str = "Veuillez saisir un nombre réel, pas une chaine de caractère."

    if MinInclus and MaxInclus:
        while float(maValeurStr) < borneMin or float(maValeurStr) > borneMax:
            maValeurStr = str(input(msgErreur))
            valeur = cast(float, _convertirType("float", maValeurStr, messageTypeErreur))

    elif not MinInclus and MaxInclus:
        while float(maValeurStr) <= borneMin or float(maValeurStr) > borneMax:
            maValeurStr = str(input(msgErreur))
            valeur = cast(float, _convertirType("float", maValeurStr, messageTypeErreur))

    elif MinInclus and not MaxInclus:
        while float(maValeurStr) < borneMin or float(maValeurStr) >= borneMax:
            maValeurStr = str(input(msgErreur))
            valeur = cast(float, _convertirType("float", maValeurStr, messageTypeErreur))

    else:
        while float(maValeurStr) <= borneMin or float(maValeurStr) >= borneMax:
            maValeurStr = str(input(msgErreur))
            valeur = cast(float, _convertirType("float", maValeurStr, messageTypeErreur))

    return valeur


def saisieFloat(
    message: str = "Veuillez saisir une valeur réel : ",
    msgErreur: str = "Erreur de saisie, veuillez saisir une valeur réel : ",
    borneMin: float = constante.MINFLOAT,
    borneMax: float = constante.MAXFLOAT,
    MinInclus: bool = True,
    MaxInclus: bool = True
) -> float:
    """
    Demande à l'utilisateur de saisir une valeur réel.
    """
    valeur: float
    valeurStr: str

    valeurStr = str(input(message))
    valeur = cast(float, _convertirType("float", valeurStr, "Veuillez saisir un nombre réel, pas une chaine de caractère."))
    valeur = _verifFloat(valeur, msgErreur, borneMin, borneMax, MinInclus, MaxInclus)

    return valeur


def _verifEntier(
    valeur: int,
    msgErreur: str,
    borneMin: int,
    borneMax: int,
    MinInclus: bool,
    MaxInclus: bool
) -> int:
    """
    Verifie si un entier est bien dans un intervalle donne.
    """
    maValeurStr: str = str(valeur)
    msgErreurType: str = "Veuillez saisir un nombre entier, pas une chaine de caractère ni un nombre réel."

    if MinInclus and MaxInclus:
        while int(maValeurStr) < borneMin or int(maValeurStr) > borneMax:
            maValeurStr = str(input(msgErreur))
            valeur = cast(int, _convertirType("int", maValeurStr, msgErreurType))

    elif not MinInclus and MaxInclus:
        while int(maValeurStr) <= borneMin or int(maValeurStr) > borneMax:
            maValeurStr = str(input(msgErreur))
            valeur = cast(int, _convertirType("int", maValeurStr, msgErreurType))

    elif MinInclus and not MaxInclus:
        while int(maValeurStr) < borneMin or int(maValeurStr) >= borneMax:
            maValeurStr = str(input(msgErreur))
            valeur = cast(int, _convertirType("int", maValeurStr, msgErreurType))

    else:
        while int(maValeurStr) <= borneMin or int(maValeurStr) >= borneMax:
            maValeurStr = str(input(msgErreur))
            valeur = cast(int, _convertirType("int", maValeurStr, msgErreurType))

    return valeur


def saisieEntier(
    message: str,
    msgErreur: str,
    borneMin: int = constante.MININT,
    borneMax: int = constante.MAXINT,
    MinInclus: bool = True,
    MaxInclus: bool = True
) -> int:
    """
    Demande à l'utilisateur de saisir une valeur entière.
    """
    valeur: int
    valeurStr: str

    valeurStr = str(input(message))
    valeur = cast(int, _convertirType("int", valeurStr, "Veuillez saisir un nombre entier, pas une chaine de caractère ni un nombre réel."))
    valeur = _verifEntier(valeur, msgErreur, borneMin, borneMax, MinInclus, MaxInclus)

    return valeur


def _verifStrInL(chaine: str, listValidChaine: list[str], msgErreur: str) -> str:
    """
    Verifie si la chaine de caractere saisie est dans les choix possibles.
    """
    while chaine not in listValidChaine:
        chaine = str(input(msgErreur))
    return chaine


def saisieStr(listValidChaine: list[str], message: str, msgErreur: str) -> str:
    """
    Demande à l'utilisateur de saisir une chaine de caractere parmi une liste valide.
    """
    chaine: str

    chaine = str(input(message))
    chaine = _verifStrInL(chaine, listValidChaine, msgErreur)
    return chaine


def saisieChaineCaractereInterdit(
    message: str,
    msgErreur: str,
    caracteresInterdit: list[str] | None = None
) -> str:
    """
    Demande une chaîne de caractères ne contenant aucun des caractères interdits.
    """
    chaine: str = str(input(message)).strip()
    valid: bool = False
    caracInterdit: str
    listeInterdits: list[str] = caracteresInterdit if caracteresInterdit is not None else []

    while not valid:
        valid = True
        for caracInterdit in listeInterdits:
            if caracInterdit in chaine:
                valid = False
                chaine = str(input(msgErreur)).strip()

    return chaine


def saisieYesOrNO(message: str) -> bool:
    """
    Fonction demandant oui ou non à l'utilisateur, renvoie True si oui/yes/y, False si non/no/n.
    """
    enAccord: bool = False
    aRepondu: bool = False
    reponse: str
    listReponseVrai: list[str] = ["oui", "Oui", "OUI", "yes", "Yes", "y", "Y"]
    listReponseFaux: list[str] = ["non", "Non", "NON", "no", "No", "n", "N"]

    reponse = input(message)
    while not aRepondu:
        if reponse in listReponseVrai:
            enAccord = True
            aRepondu = True
        elif reponse in listReponseFaux:
            enAccord = False
            aRepondu = True
        else:
            print(f"Saisie incorrect, choix accepté : \n {listReponseVrai} \n {listReponseFaux}")
            reponse = input(message)

    return enAccord
