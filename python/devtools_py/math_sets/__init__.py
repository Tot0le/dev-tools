from devtools_py.math_sets.math_utils import (
    is_prime,
    fibonacci_iterative,
    fibonacci_recursive,
    factorial,
)
from devtools_py.math_sets.sets_lists import (
    generate_random_int_list,
    count_duplicate_values,
    count_distinct_values,
    is_set,
    add_to_set,
    union,
    intersection,
    difference,
    are_disjoint,
)

# French aliases
est_premier = is_prime
factorielle = factorial
generer_liste_entiers_aleatoires = generate_random_int_list
compter_valeurs_en_doublon = count_duplicate_values
compter_valeurs_distinctes = count_distinct_values
est_un_ensemble = is_set
ajouter_si_absent = add_to_set
sont_disjointes = are_disjoint

__all__: list[str] = [
    # English & Bilingual API
    "is_prime",
    "fibonacci_iterative",
    "fibonacci_recursive",
    "factorial",
    "generate_random_int_list",
    "count_duplicate_values",
    "count_distinct_values",
    "is_set",
    "add_to_set",
    "union",
    "intersection",
    "difference",
    "are_disjoint",
    # French API
    "est_premier",
    "factorielle",
    "generer_liste_entiers_aleatoires",
    "compter_valeurs_en_doublon",
    "compter_valeurs_distinctes",
    "est_un_ensemble",
    "ajouter_si_absent",
    "sont_disjointes",
]