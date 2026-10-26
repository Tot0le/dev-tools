from typing import TextIO


def count_file_lines(file_path: str) -> int:
    """
    Count and return the total number of lines in a text file.
    """
    file: TextIO
    line_count: int = 0

    with open(file_path, "r", encoding="utf-8") as file:
        for _ in file:
            line_count += 1

    return line_count


def clear_file_content(file_path: str) -> None:
    """
    Erase all content from the specified file without deleting the file itself.
    """
    file: TextIO

    with open(file_path, "r+", encoding="utf-8") as file:
        file.truncate(0)
