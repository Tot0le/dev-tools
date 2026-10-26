from devtools_py.cli.display import (
    print_newlines,
    wait_for_enter,
    clear_console,
)
from devtools_py.cli.inputs import (
    prompt_float,
    prompt_int,
    prompt_choice,
    prompt_filtered_str,
    prompt_yes_or_no,
)

# French aliases
aller_a_la_ligne = print_newlines
attendre_entree = wait_for_enter
saisir_float = prompt_float
saisir_entier = prompt_int
saisir_choix = prompt_choice
saisir_chaine_filtree = prompt_filtered_str
saisir_oui_ou_non = prompt_yes_or_no

__all__: list[str] = [
    # English API
    "print_newlines",
    "wait_for_enter",
    "clear_console",
    "prompt_float",
    "prompt_int",
    "prompt_choice",
    "prompt_filtered_str",
    "prompt_yes_or_no",
    # French API
    "aller_a_la_ligne",
    "attendre_entree",
    "saisir_float",
    "saisir_entier",
    "saisir_choix",
    "saisir_chaine_filtree",
    "saisir_oui_ou_non",
]