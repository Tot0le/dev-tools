import platform
import subprocess


def print_newlines(count: int = 1) -> None:
    """
    Print a specified number of blank lines to the console.
    """
    for _ in range(count):
        print()


def wait_for_enter(lang: str = "en") -> None:
    """
    Pause execution until the user presses the Enter key.
    Supported languages: 'en' (default) and 'fr'.
    """
    normalized_lang: str = lang.strip().lower()

    match normalized_lang:
        case "fr":
            input("Appuyez sur Entrée pour continuer...")
        case _:
            input("Press Enter to continue...")


def clear_console() -> None:
    """
    Clear the terminal screen on Windows and Unix-like systems.
    """
    if platform.system() == "Windows":
        subprocess.run(["cmd", "/c", "cls"], check=False)
    else:
        subprocess.run(["clear"], check=False)
