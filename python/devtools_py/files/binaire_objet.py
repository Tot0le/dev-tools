import os
from typing import Any, TypeVar
from devtools_py.cli.saisie import saisieYesOrNO
from devtools_py.files.binaire_simple import chargerFichierBin, sauvegarderFichierBin

genericClasse = TypeVar("genericClasse")


def concatenerClasseEnListe(monObjet: object) -> list[Any]:
    """
    Retourne la liste des valeurs de tous les attributs d'une instance de classe.
    """
    valeurs: list[Any] = list(monObjet.__dict__.values())
    return valeurs


def trouverElementFichierBin(
    listeDeType: list[genericClasse],
    monElementComparatif: Any,
    nomAttribut: str | None = None
) -> genericClasse | None:
    """
    Cherche et retourne le premier objet de la liste correspondant à 'monElementComparatif'.
    Si 'nomAttribut' est précisé, vérifie uniquement cet attribut ; sinon vérifie tous les attributs.
    """
    objet: genericClasse
    objetTrouve: genericClasse | None = None

    for objet in listeDeType:
        if objetTrouve is None:
            if nomAttribut is not None:
                if getattr(objet, nomAttribut, None) == monElementComparatif:
                    objetTrouve = objet
            else:
                if monElementComparatif in objet.__dict__.values():
                    objetTrouve = objet

    return objetTrouve


def elementEstDansFichierBin(
    listeDeType: list[genericClasse],
    monElementComparatif: Any,
    nomAttribut: str | None = None
) -> bool:
    """
    Retourne True si un objet correspondant à 'monElementComparatif' existe dans la liste, False sinon.
    """
    element: genericClasse | None = trouverElementFichierBin(
        listeDeType, monElementComparatif, nomAttribut
    )
    estPresent: bool = element is not None
    return estPresent


def rajouterElementFichierBin(
    cheminFichier: str,
    elementComparatif: Any,
    nouvelObjet: object,
    modifierSiDedans: bool | None = None,
    nomAttribut: str | None = None
) -> None:
    """
    Ajoute un objet dans un fichier binaire s'il n'est pas déjà présent.
    S'il est présent, met à jour ses attributs selon 'modifierSiDedans' (ou demande à l'utilisateur si None).
    """
    listeGlobale: list[object] = chargerFichierBin(cheminFichier)
    objetExistant: object | None = trouverElementFichierBin(
        listeGlobale, elementComparatif, nomAttribut
    )
    nomAttr: str
    valeurAttr: Any

    if objetExistant is not None:
        if modifierSiDedans is None:
            modifierSiDedans = saisieYesOrNO(
                "L'élément est déjà présent dans le fichier, voulez-vous le modifier avec vos nouvelles valeurs ? "
                "\n(si non : ne rien faire) : "
            )

        if modifierSiDedans:
            for nomAttr, valeurAttr in nouvelObjet.__dict__.items():
                setattr(objetExistant, nomAttr, valeurAttr)
    else:
        listeGlobale.append(nouvelObjet)

    sauvegarderFichierBin(cheminFichier, listeGlobale)


def supprimerLigneFichierBinaire(
    cheminFichier: str,
    identifiant: Any,
    nomAttribut: str | None = None
) -> None:
    """
    Supprime l'objet correspondant à l'identifiant donné dans le fichier binaire.
    """
    listeGlobale: list[object] = chargerFichierBin(cheminFichier)
    objetASupprimer: object | None = trouverElementFichierBin(
        listeGlobale, identifiant, nomAttribut
    )

    if objetASupprimer is not None:
        listeGlobale.remove(objetASupprimer)
        sauvegarderFichierBin(cheminFichier, listeGlobale)
        print(f"Ligne avec identifiant '{identifiant}' supprimée du fichier '{cheminFichier}'.")
    else:
        print(f"Aucune ligne avec identifiant '{identifiant}' trouvée dans le fichier '{cheminFichier}'.")


def donneLigneFichierBin(
    monElementComparatif: Any,
    cheminDuFichier: str,
    nomAttribut: str | None = None
) -> list[Any]:
    """
    Cherche l'objet correspondant à 'monElementComparatif' dans le fichier et retourne ses attributs en liste.
    """
    ligne: list[Any] = []
    listeDeType: list[object] = chargerFichierBin(cheminDuFichier)
    objetTrouve: object | None = trouverElementFichierBin(
        listeDeType, monElementComparatif, nomAttribut
    )

    if objetTrouve is not None:
        ligne = concatenerClasseEnListe(objetTrouve)

    return ligne


def donneToutFichierBin(cheminFichierBin: str) -> list[list[Any]]:
    """
    Retourne tout le contenu du fichier binaire sous forme d'une liste de listes des valeurs d'attributs.
    """
    listeFichier: list[list[Any]] = []
    listeGeneral: list[object]
    instanceObjet: object

    if not os.path.exists(cheminFichierBin):
        print(f"Erreur : Le fichier '{cheminFichierBin}' est introuvable.")
    else:
        listeGeneral = chargerFichierBin(cheminFichierBin)

        if not listeGeneral:
            print("Le fichier est vide ou n'a pas pu être lu.")
        else:
            for instanceObjet in listeGeneral:
                listeFichier.append(concatenerClasseEnListe(instanceObjet))

    return listeFichier


def afficherFichierBin(cheminDuFichier: str) -> None:
    """
    Affiche chaque objet du fichier binaire sous forme de liste de ses valeurs d'attributs.
    """
    listeGeneral: list[object]
    instanceObjet: object

    if not os.path.exists(cheminDuFichier):
        print(f"Erreur : Le fichier '{cheminDuFichier}' est introuvable.")
    else:
        listeGeneral = chargerFichierBin(cheminDuFichier)

        if not listeGeneral:
            print("Le fichier est vide ou n'a pas pu être lu.")
        else:
            for instanceObjet in listeGeneral:
                print(concatenerClasseEnListe(instanceObjet))


def afficherLigneFichierBin(
    monElementComparatif: Any,
    cheminDuFichier: str,
    nomAttribut: str | None = None
) -> None:
    """
    Cherche l'objet correspondant à 'monElementComparatif' et affiche la liste de ses attributs.
    """
    print(str(donneLigneFichierBin(monElementComparatif, cheminDuFichier, nomAttribut)))
