from devtools_py.files.text_io import (
    count_file_lines,
    clear_file_content,
)
from devtools_py.files.bin_simple import (
    load_binary_file,
    save_binary_file,
    append_to_binary_file,
    print_binary_file,
)
from devtools_py.files.bin_objects import (
    object_to_value_list,
    find_object_in_list,
    is_object_in_list,
    upsert_object_in_binary_file,
    delete_object_from_binary_file,
    get_object_values_from_binary_file,
    get_all_objects_values_from_binary_file,
    print_objects_from_binary_file,
    print_single_object_from_binary_file,
)

# French aliases
compter_lignes_fichier = count_file_lines
effacer_contenu_fichier = clear_file_content
charger_fichier_bin = load_binary_file
sauvegarder_fichier_bin = save_binary_file
ajouter_dans_fichier_bin = append_to_binary_file
afficher_fichier_bin = print_binary_file
objet_vers_liste = object_to_value_list
trouver_objet_dans_liste = find_object_in_list
objet_est_dans_liste = is_object_in_list
ajouter_ou_modifier_objet_bin = upsert_object_in_binary_file
supprimer_objet_fichier_bin = delete_object_from_binary_file
obtenir_valeurs_objet_bin = get_object_values_from_binary_file
obtenir_toutes_valeurs_objets_bin = get_all_objects_values_from_binary_file
afficher_objets_fichier_bin = print_objects_from_binary_file
afficher_objet_fichier_bin = print_single_object_from_binary_file

__all__: list[str] = [
    # English API
    "count_file_lines",
    "clear_file_content",
    "load_binary_file",
    "save_binary_file",
    "append_to_binary_file",
    "print_binary_file",
    "object_to_value_list",
    "find_object_in_list",
    "is_object_in_list",
    "upsert_object_in_binary_file",
    "delete_object_from_binary_file",
    "get_object_values_from_binary_file",
    "get_all_objects_values_from_binary_file",
    "print_objects_from_binary_file",
    "print_single_object_from_binary_file",
    # French API
    "compter_lignes_fichier",
    "effacer_contenu_fichier",
    "charger_fichier_bin",
    "sauvegarder_fichier_bin",
    "ajouter_dans_fichier_bin",
    "afficher_fichier_bin",
    "objet_vers_liste",
    "trouver_objet_dans_liste",
    "objet_est_dans_liste",
    "ajouter_ou_modifier_objet_bin",
    "supprimer_objet_fichier_bin",
    "obtenir_valeurs_objet_bin",
    "obtenir_toutes_valeurs_objets_bin",
    "afficher_objets_fichier_bin",
    "afficher_objet_fichier_bin",
]
