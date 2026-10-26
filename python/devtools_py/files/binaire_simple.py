import os
import pickle
from typing import Any, BinaryIO


def chargerFichierBin(cheminFichier: str) -> list[Any]:
    """
    Lit un fichier binaire et retourne la liste d'éléments qu'il contient.
    Retourne une liste vide [] si le fichier n'existe pas, est vide ou est corrompu.
    """
    contenu: list[Any] = []
    f: BinaryIO

    if os.path.exists(cheminFichier):
        try:
            with open(cheminFichier, "rb") as f:
                contenu = pickle.load(f)
        except (EOFError, pickle.UnpicklingError):
            contenu = []

    return contenu


def sauvegarderFichierBin(cheminFichier: str, donnees: list[Any]) -> None:
    """
    Sauvegarde une liste d'éléments dans un fichier binaire (écrase le contenu existant).
    """
    f: BinaryIO

    with open(cheminFichier, "wb") as f:
        pickle.dump(donnees, f)


def rajouterTexteFichierBin(cheminFichier: str, donnee: Any) -> None:
    """
    Ajoute un élément simple (str, int, etc.) à la fin de la liste stockée dans un fichier binaire.
    """
    listeGlobale: list[Any] = chargerFichierBin(cheminFichier)
    listeGlobale.append(donnee)
    sauvegarderFichierBin(cheminFichier, listeGlobale)


def afficherFichierBinSimple(cheminDuFichier: str) -> None:
    """
    Affiche le contenu brut d'un fichier binaire simple dans la console.
    """
    listeGeneral: list[Any]

    if not os.path.exists(cheminDuFichier):
        print(f"Erreur : Le fichier '{cheminDuFichier}' est introuvable.")
    else:
        listeGeneral = chargerFichierBin(cheminDuFichier)

        if not listeGeneral:
            print("Le fichier est vide ou n'a pas pu être lu.")
        else:
            print(listeGeneral)
