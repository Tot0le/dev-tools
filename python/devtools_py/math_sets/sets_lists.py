from random import randint


def generate_random_int_list(count: int, min_val: int, max_val: int) -> list[int]:
    """
    Generate a list of 'count' random integers between 'min_val' and 'max_val' (inclusive).
    """
    random_list: list[int] = []

    for _ in range(count):
        random_list.append(randint(min_val, max_val))

    return random_list


def count_duplicate_values(items: list[int]) -> int:
    """
    Return the number of distinct values that appear more than once in the list.
    """
    duplicates: list[int] = []
    i: int
    j: int
    duplicate_count: int = 0

    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if items[i] == items[j] and items[i] not in duplicates:
                duplicates.append(items[i])
                duplicate_count += 1

    return duplicate_count


def count_distinct_values(items: list[int]) -> int:
    """
    Return the total number of distinct values present in the list.
    """
    seen: list[int] = []
    item: int

    for item in items:
        if item not in seen:
            seen.append(item)

    distinct_count: int = len(seen)
    return distinct_count


def is_set(items: list[int]) -> bool:
    """
    Return True if the list contains no duplicate elements, False otherwise.
    """
    result: bool = count_duplicate_values(items) == 0
    return result


def add_to_set(value: int, items: list[int]) -> list[int]:
    """
    Return a new list with 'value' appended if it is not already present.
    Raise a ValueError if 'items' is not a valid set (contains duplicates).
    """
    result_set: list[int] = items.copy()

    if not is_set(result_set):
        raise ValueError("Error: The provided list is not a set (it contains duplicates).")

    if value not in result_set:
        result_set.append(value)

    return result_set


def union(set_a: list[int], set_b: list[int]) -> list[int]:
    """
    Return the union of two set-like lists.
    Raise a ValueError if either list contains duplicates.
    """
    if not is_set(set_a) or not is_set(set_b):
        raise ValueError("Error: Both input lists must be valid sets without duplicates.")

    union_set: list[int] = set_a.copy()
    item: int

    for item in set_b:
        union_set = add_to_set(item, union_set)

    return union_set


def intersection(set_a: list[int], set_b: list[int]) -> list[int]:
    """
    Return the intersection (common elements) of two set-like lists.
    Raise a ValueError if either list contains duplicates.
    """
    if not is_set(set_a) or not is_set(set_b):
        raise ValueError("Error: Both input lists must be valid sets without duplicates.")

    intersection_set: list[int] = []
    item: int

    for item in set_a:
        if item in set_b:
            intersection_set.append(item)

    return intersection_set


def difference(set_a: list[int], set_b: list[int]) -> tuple[list[int], list[int]]:
    """
    Return a tuple containing both relative complements: (set_a \\ set_b, set_b \\ set_a).
    Raise a ValueError if either list contains duplicates.
    """
    if not is_set(set_a) or not is_set(set_b):
        raise ValueError("Error: Both input lists must be valid sets without duplicates.")

    diff_a_b: list[int] = set_a.copy()
    diff_b_a: list[int] = set_b.copy()
    item: int

    for item in set_b:
        if item in diff_a_b:
            diff_a_b.remove(item)

    for item in set_a:
        if item in diff_b_a:
            diff_b_a.remove(item)

    return diff_a_b, diff_b_a


def are_disjoint(set_a: list[int], set_b: list[int]) -> bool:
    """
    Return True if the two sets have no elements in common, False otherwise.
    Raise a ValueError if either list contains duplicates.
    """
    if not is_set(set_a) or not is_set(set_b):
        raise ValueError("Error: Both input lists must be valid sets without duplicates.")

    disjoint: bool = True
    idx: int = 0

    while disjoint and idx < len(set_a):
        if set_a[idx] in set_b:
            disjoint = False
        idx += 1

    return disjoint
