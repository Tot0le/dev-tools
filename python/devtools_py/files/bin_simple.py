import os
import pickle
from typing import Any, BinaryIO


def load_binary_file(file_path: str) -> list[Any]:
    """
    Read a binary file and return the list of elements it contains.
    Return an empty list [] if the file does not exist, is empty, or is corrupted.
    """
    content: list[Any] = []
    file: BinaryIO

    if os.path.exists(file_path):
        try:
            with open(file_path, "rb") as file:
                content = pickle.load(file)
        except (EOFError, pickle.UnpicklingError):
            content = []

    return content


def save_binary_file(file_path: str, data: list[Any]) -> None:
    """
    Serialize and save a list of elements to a binary file (overwrites existing content).
    """
    file: BinaryIO

    with open(file_path, "wb") as file:
        pickle.dump(data, file)


def append_to_binary_file(file_path: str, item: Any) -> None:
    """
    Append a single element (str, int, list, etc.) to the list stored in a binary file.
    """
    items: list[Any] = load_binary_file(file_path)
    items.append(item)
    save_binary_file(file_path, items)


def print_binary_file(file_path: str) -> None:
    """
    Print the raw list content of a binary file to the console.
    """
    items: list[Any]

    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found.")
    else:
        items = load_binary_file(file_path)

        if not items:
            print("The file is empty or could not be read.")
        else:
            print(items)
