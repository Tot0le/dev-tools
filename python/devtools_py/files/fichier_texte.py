from typing import TextIO


def nombreLigneFichier(nomFichier: str) -> int:
    """
    Compte le nombre de lignes dans un fichier et le retourne.
    """
    f: TextIO
    nombreLigne: int = 0

    with open(nomFichier, "r", encoding="utf-8") as f:
        for _ in f:
            nombreLigne += 1

    return nombreLigne


def effacerContenuFichier(cheminFichier: str) -> None:
    """
    Efface le contenu du fichier en entrée.
    """
    f: TextIO

    with open(cheminFichier, "r+", encoding="utf-8") as f:
        f.truncate(0)
