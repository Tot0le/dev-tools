from devtools_py.strings.occurrences import (
    count_char_occurrences,
    decrement_char_occurrence,
    increment_char_occurrence,
    has_remaining_count,
)

# French aliases
compter_occurrences = count_char_occurrences
decrementer_occurrence = decrement_char_occurrence
incrementer_occurrence = increment_char_occurrence
a_quantite_restante = has_remaining_count

__all__: list[str] = [
    # English API
    "count_char_occurrences",
    "decrement_char_occurrence",
    "increment_char_occurrence",
    "has_remaining_count",
    # French API
    "compter_occurrences",
    "decrementer_occurrence",
    "incrementer_occurrence",
    "a_quantite_restante",
]
