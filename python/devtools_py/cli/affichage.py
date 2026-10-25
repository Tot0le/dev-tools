import os

def ALaLigne(monNombreDeFois: int) -> None:
    i: int

    for i in range(monNombreDeFois):
        print()


def pressEnterToContinue(langue: str = "en") -> None:
    """
    Fonction qui fait qu'on doit appuyer sur entrée pour continuer
    """
    langue = langue.lower()
    match langue:
        case "fr":
            input("Appuyez sur Entrée pour continuer...")
        case _:
            input("Press Enter to continue.")


def clearConsole() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')
    
