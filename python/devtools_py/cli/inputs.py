from typing import cast
from devtools_py import constants


def _convert_type(target_type: str, value: str, type_error_msg: str) -> int | float | str | None:
    """
    Convert a string value to the specified target type ('int', 'float', 'str').
    Print an error message and return None if conversion fails.
    """
    result: int | float | str | None = None

    match target_type:
        case "float":
            try:
                result = float(value)
            except ValueError:
                print(f"Error: Unable to convert '{value}' to float.")
                print(type_error_msg)
                result = None

        case "int":
            try:
                result = int(value)
            except ValueError:
                print(f"Error: Unable to convert '{value}' to int.")
                print(type_error_msg)
                result = None

        case "str":
            result = value

        case _:
            print(f"Error: Unsupported type '{target_type}'. (Expected: float, int, str)")
            result = None

    return result


def _is_within_bounds(
    value: int | float,
    min_val: int | float,
    max_val: int | float,
    min_inclusive: bool,
    max_inclusive: bool
) -> bool:
    """
    Check whether a numeric value falls within the specified minimum and maximum bounds.
    """
    meets_min: bool = (value >= min_val) if min_inclusive else (value > min_val)
    meets_max: bool = (value <= max_val) if max_inclusive else (value < max_val)
    is_valid: bool = meets_min and meets_max

    return is_valid


def prompt_float(
    prompt: str = "Enter a float value: ",
    error_msg: str = "Invalid input. Please enter a valid float value: ",
    min_val: float = constants.MIN_FLOAT,
    max_val: float = constants.MAX_FLOAT,
    min_inclusive: bool = True,
    max_inclusive: bool = True
) -> float:
    """
    Prompt the user for a floating-point number within the specified bounds.
    Reprompt until a valid float meeting all constraints is provided.
    """
    type_error_msg: str = "Please enter a valid floating-point number, not text."
    raw_value: str = input(prompt)
    converted_val: int | float | str | None = _convert_type("float", raw_value, type_error_msg)
    float_val: float
    is_valid: bool = False
    result: float = 0.0

    while not is_valid:
        if converted_val is not None:
            float_val = cast(float, converted_val)
            if _is_within_bounds(float_val, min_val, max_val, min_inclusive, max_inclusive):
                result = float_val
                is_valid = True

        if not is_valid:
            raw_value = input(error_msg)
            converted_val = _convert_type("float", raw_value, type_error_msg)

    return result


def prompt_int(
    prompt: str = "Enter an integer value: ",
    error_msg: str = "Invalid input. Please enter a valid integer value: ",
    min_val: int = constants.MIN_INT,
    max_val: int = constants.MAX_INT,
    min_inclusive: bool = True,
    max_inclusive: bool = True
) -> int:
    """
    Prompt the user for an integer within the specified bounds.
    Reprompt until a valid integer meeting all constraints is provided.
    """
    type_error_msg: str = "Please enter a valid integer, not text or a decimal number."
    raw_value: str = input(prompt)
    converted_val: int | float | str | None = _convert_type("int", raw_value, type_error_msg)
    int_val: int
    is_valid: bool = False
    result: int = 0

    while not is_valid:
        if converted_val is not None:
            int_val = cast(int, converted_val)
            if _is_within_bounds(int_val, min_val, max_val, min_inclusive, max_inclusive):
                result = int_val
                is_valid = True

        if not is_valid:
            raw_value = input(error_msg)
            converted_val = _convert_type("int", raw_value, type_error_msg)

    return result


def _verify_choice(text: str, valid_choices: list[str], error_msg: str) -> str:
    """
    Reprompt the user until the input string matches one of the valid choices.
    """
    while text not in valid_choices:
        text = input(error_msg)

    return text


def prompt_choice(valid_choices: list[str], prompt: str, error_msg: str) -> str:
    """
    Prompt the user to enter a string belonging to a predefined list of valid choices.
    """
    text: str = input(prompt)
    text = _verify_choice(text, valid_choices, error_msg)

    return text


def prompt_filtered_str(
    prompt: str,
    error_msg: str,
    forbidden_chars: list[str] | None = None
) -> str:
    """
    Prompt the user for a string that does not contain any of the specified forbidden characters.
    """
    text: str = input(prompt).strip()
    is_valid: bool = False
    char: str
    forbidden_list: list[str] = forbidden_chars if forbidden_chars is not None else []

    while not is_valid:
        is_valid = True
        for char in forbidden_list:
            if char in text:
                is_valid = False
        if not is_valid:
            text = input(error_msg).strip()

    return text


def prompt_yes_or_no(prompt: str) -> bool:
    """
    Prompt the user for a yes/no (or oui/non) confirmation.
    Return True for affirmative answers and False for negative answers.
    """
    agreed: bool = False
    answered: bool = False
    response: str
    true_choices: list[str] = ["yes", "y", "oui", "o"]
    false_choices: list[str] = ["no", "n", "non"]

    response = input(prompt).strip().lower()
    while not answered:
        if response in true_choices:
            agreed = True
            answered = True
        elif response in false_choices:
            agreed = False
            answered = True
        else:
            print(f"Invalid input. Accepted choices: {true_choices} or {false_choices}")
            response = input(prompt).strip().lower()

    return agreed
