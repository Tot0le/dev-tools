import os
import pickle
from typing import Any, BinaryIO


def chargerFichierBin(cheminFichier: str) -> list[Any]:
    """
    Fonction générique qui lit n'importe quel fichier binaire et retourne son contenu (une liste).
    Renvoie une liste vide [] si le fichier n'existe pas ou est corrompu.
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
    Fonction générique qui sauvegarde n'importe quelle liste dans un fichier binaire.
    """
    f: BinaryIO

    with open(cheminFichier, "wb") as f:
        pickle.dump(donnees, f)


def rajouterTexteFichierBin(cheminFichier: str, donnee: str) -> None:
    """
    Rajoute une chaîne de caractères dans un fichier binaire contenant une liste.
    """
    listeGlobale: list[Any]

    listeGlobale = chargerFichierBin(cheminFichier)
    listeGlobale = listeGlobale + [donnee]
    sauvegarderFichierBin(cheminFichier, listeGlobale)


def afficherFichierBinSimple(cheminDuFichier: str) -> None:
    """
    Affiche tout le contenu d'un fichier binaire simple.
    """
    listeGeneral: list[Any]

    if not os.path.exists(cheminDuFichier):
        print(f"Erreur : Le fichier {cheminDuFichier} est introuvable.")
    else:
        listeGeneral = chargerFichierBin(cheminDuFichier)

        if listeGeneral == []:
            print("Le fichier est vide ou n'a pas pu être lu.")
        else:
            print(listeGeneral)
