import os
import subprocess


def ALaLigne(monNombreDeFois: int = 1) -> None:
    """
    Affiche un nombre donné de sauts de ligne dans la console (1 par défaut).
    """
    for _ in range(monNombreDeFois):
        print()


def pressEnterToContinue(langue: str = "en") -> None:
    """
    Met le programme en pause jusqu'à ce que l'utilisateur appuie sur Entrée.
    Langues supportées : 'fr' ou 'en' (par défaut).
    """
    langueNormalisee: str = langue.strip().lower()

    match langueNormalisee:
        case "fr":
            input("Appuyez sur Entrée pour continuer...")
        case _:
            input("Press Enter to continue...")


def clearConsole() -> None:
    """
    Efface le contenu du terminal (compatible Windows et Unix/Linux/macOS).
    """
    if os.name == "nt":
        subprocess.run("cls", shell=True, check=False)
    else:
        subprocess.run(["clear"], check=False)
