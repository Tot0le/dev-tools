import os
from typing import Any, TypeVar
from devtools_py.cli.saisie import saisieYesOrNO
from devtools_py.files.binaire_simple import chargerFichierBin, sauvegarderFichierBin

genericClasse = TypeVar("genericClasse")


def concatenerClasseEnListe(monObjet: object) -> list[Any]:
    """
    Retourne une liste des valeurs des attributs de l'objet en entrée.
    """
    valeurs: list[Any] = list(monObjet.__dict__.values())
    return valeurs


def trouverElementFichierBin(
    listeDeType: list[genericClasse],
    monElementComparatif: str
) -> genericClasse | None:
    """
    Parcourt la liste pour trouver l'objet possédant la valeur monElementComparatif dans ses attributs.
    """
    objet: genericClasse
    objetTrouve: genericClasse | None = None

    for objet in listeDeType:
        if objetTrouve is None and monElementComparatif in objet.__dict__.values():
            objetTrouve = objet

    return objetTrouve


def elementEstDansFichierBin(
    listeDeType: list[genericClasse],
    monElementComparatif: str
) -> bool:
    """
    Vérifie si un objet possédant la valeur monElementComparatif est présent dans la liste.
    """
    element: genericClasse | None = trouverElementFichierBin(listeDeType, monElementComparatif)
    result: bool = element is not None
    return result


def trouverElementFichierBinAvecNom(
    listeDeType: list[genericClasse],
    monElementComparatif: str,
    nomAttribut: str
) -> genericClasse | None:
    """
    Parcourt la liste pour trouver l'objet dont l'attribut 'nomAttribut' vaut 'monElementComparatif'.
    """
    objet: genericClasse
    objetTrouve: genericClasse | None = None

    for objet in listeDeType:
        if objetTrouve is None and getattr(objet, nomAttribut, None) == monElementComparatif:
            objetTrouve = objet

    return objetTrouve


def elementEstDansFichierBinAvecNom(
    listeDeType: list[genericClasse],
    monElementComparatif: str,
    nomAttribut: str
) -> bool:
    """
    Vérifie si un objet dont l'attribut 'nomAttribut' vaut 'monElementComparatif' est dans la liste.
    """
    element: genericClasse | None = trouverElementFichierBinAvecNom(
        listeDeType, monElementComparatif, nomAttribut
    )
    result: bool = element is not None
    return result


def rajouterElementFichierBin(
    cheminFichier: str,
    elementComparatif: str,
    listeDonnees: list[object],
    modifierSiDedans: bool | None = None
) -> None:
    """
    Rajoute un objet dans un fichier binaire s'il n'est pas dedans, ou propose de le modifier.
    """
    objet: object | None
    iterateur: int
    listeAttributs: list[str]
    listeGlobale: list[object]
    nouvelObjet: object
    valeursAMettre: list[Any]

    listeGlobale = chargerFichierBin(cheminFichier)
    objet = trouverElementFichierBin(listeGlobale, elementComparatif)

    if objet is not None:
        if modifierSiDedans is None:
            modifierSiDedans = saisieYesOrNO(
                "L'élement est déjà présent dans le fichier, voulez vous le modifier avec vos valeurs saisies ? "
                "\n(si non : ne rien faire) : "
            )

        if modifierSiDedans:
            listeAttributs = list(objet.__dict__.keys())
            nouvelObjet = listeDonnees[0]
            valeursAMettre = list(nouvelObjet.__dict__.values())

            for iterateur in range(len(listeAttributs)):
                setattr(objet, listeAttributs[iterateur], valeursAMettre[iterateur])
    else:
        listeGlobale = listeGlobale + listeDonnees

    sauvegarderFichierBin(cheminFichier, listeGlobale)


def supprimerLigneFichierBinaire(cheminFichier: str, identifiant: str) -> None:
    """
    Supprime un objet du fichier binaire correspondant à l'identifiant donné.
    """
    listeGlobale: list[object] = chargerFichierBin(cheminFichier)
    objetASupprimer: object | None = trouverElementFichierBin(listeGlobale, identifiant)

    if objetASupprimer is not None:
        listeGlobale.remove(objetASupprimer)
        sauvegarderFichierBin(cheminFichier, listeGlobale)
        print(f"Ligne avec identifiant '{identifiant}' supprimée du fichier '{cheminFichier}'.")
    else:
        print(f"Aucune ligne avec identifiant '{identifiant}' trouvée dans le fichier '{cheminFichier}'.")


def donneLigneFichierBin(monElementComparatif: str, cheminDuFichier: str) -> list[Any]:
    """
    Cherche l'objet correspondant à monElementComparatif dans le fichier et retourne ses valeurs en liste.
    """
    ligne: list[Any] = []
    listeDeType: list[object] = chargerFichierBin(cheminDuFichier)
    objetTrouve: object | None = trouverElementFichierBin(listeDeType, monElementComparatif)

    if objetTrouve is not None:
        ligne = concatenerClasseEnListe(objetTrouve)

    return ligne


def donneToutFichierBin(cheminFichierBin: str) -> list[list[Any]]:
    """
    Donne tout le contenu du fichier binaire sous forme d'une liste de listes des valeurs d'objets.
    """
    listeFichier: list[list[Any]] = []
    listeGeneral: list[object]
    classe: object

    if not os.path.exists(cheminFichierBin):
        print(f"Erreur : Le fichier {cheminFichierBin} est introuvable.")
    else:
        listeGeneral = chargerFichierBin(cheminFichierBin)

        if listeGeneral == []:
            print("Le fichier est vide ou n'a pas pu être lu.")
        else:
            for classe in listeGeneral:
                listeFichier.append(concatenerClasseEnListe(classe))

    return listeFichier


def afficherFichierBin(cheminDuFichier: str) -> None:
    """
    Affiche tout le contenu d'un fichier binaire contenant des objets de classe.
    """
    listeGeneral: list[object]
    classe: object

    if not os.path.exists(cheminDuFichier):
        print(f"Erreur : Le fichier {cheminDuFichier} est introuvable.")
    else:
        listeGeneral = chargerFichierBin(cheminDuFichier)

        if listeGeneral == []:
            print("Le fichier est vide ou n'a pas pu être lu.")
        else:
            for classe in listeGeneral:
                print(concatenerClasseEnListe(classe))


def afficherLigneFichierBin(monElementComparatif: str, cheminDuFichier: str) -> None:
    """
    Cherche l'objet correspondant à monElementComparatif et affiche ses valeurs sous forme de liste.
    """
    print(str(donneLigneFichierBin(monElementComparatif, cheminDuFichier)))
