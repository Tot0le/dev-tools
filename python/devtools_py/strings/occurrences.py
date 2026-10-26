from typing import cast


def count_char_occurrences(
    text: str,
    target_chars: list[str] | None = None
) -> list[list[str | int]]:
    """
    Count the occurrences of each character in 'text'.
    If 'target_chars' is provided, only count characters present in that list.
    Return a list of pairs [character, count], e.g., [['A', 2], ['B', 1]].
    """
    occurrences: list[list[str | int]] = []
    chars_to_count: list[str] = []
    char: str
    text_char: str
    count: int

    if target_chars is not None:
        chars_to_count = target_chars
    else:
        for char in text:
            if char not in chars_to_count:
                chars_to_count.append(char)

    for char in chars_to_count:
        count = 0
        for text_char in text:
            if text_char == char:
                count += 1
        occurrences.append([char, count])

    return occurrences


def decrement_char_occurrence(
    occurrences: list[list[str | int]],
    char: str
) -> list[list[str | int]]:
    """
    Decrement the occurrence count of 'char' by 1 in the 'occurrences' list.
    """
    pair: list[str | int]
    current_count: int

    for pair in occurrences:
        if pair[0] == char:
            current_count = cast(int, pair[1])
            pair[1] = current_count - 1

    return occurrences


def increment_char_occurrence(
    occurrences: list[list[str | int]],
    char: str
) -> list[list[str | int]]:
    """
    Increment the occurrence count of 'char' by 1 in the 'occurrences' list.
    """
    pair: list[str | int]
    current_count: int

    for pair in occurrences:
        if pair[0] == char:
            current_count = cast(int, pair[1])
            pair[1] = current_count + 1

    return occurrences


def has_remaining_count(
    occurrences: list[list[str | int]],
    char: str
) -> bool:
    """
    Return True if 'char' is present in 'occurrences' with a count strictly greater than 0.
    """
    is_available: bool = False
    pair: list[str | int]
    remaining_count: int

    for pair in occurrences:
        if pair[0] == char:
            remaining_count = cast(int, pair[1])
            if remaining_count > 0:
                is_available = True

    return is_available
