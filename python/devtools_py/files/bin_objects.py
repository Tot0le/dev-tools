import os
from typing import Any, TypeVar
from devtools_py.cli.inputs import prompt_yes_or_no
from devtools_py.files.bin_simple import load_binary_file, save_binary_file

T = TypeVar("T")


def object_to_value_list(obj: object) -> list[Any]:
    """
    Return a list containing all attribute values of a class instance.
    """
    values: list[Any] = list(obj.__dict__.values())
    return values


def find_object_in_list(
    objects: list[T],
    target_value: Any,
    attr_name: str | None = None
) -> T | None:
    """
    Search and return the first object in 'objects' matching 'target_value'.
    If 'attr_name' is provided, check only that attribute; otherwise check all attributes.
    """
    obj: T
    found_obj: T | None = None

    for obj in objects:
        if found_obj is None:
            if attr_name is not None:
                if getattr(obj, attr_name, None) == target_value:
                    found_obj = obj
            else:
                if target_value in obj.__dict__.values():
                    found_obj = obj

    return found_obj


def is_object_in_list(
    objects: list[T],
    target_value: Any,
    attr_name: str | None = None
) -> bool:
    """
    Return True if an object matching 'target_value' exists in the list, False otherwise.
    """
    found_obj: T | None = find_object_in_list(objects, target_value, attr_name)
    exists: bool = found_obj is not None
    return exists


def upsert_object_in_binary_file(
    file_path: str,
    target_value: Any,
    new_obj: object,
    overwrite_if_exists: bool | None = None,
    attr_name: str | None = None
) -> None:
    """
    Insert an object into a binary file if no matching object is found.
    If a matching object exists, update its attributes based on 'overwrite_if_exists'
    (prompts the user via CLI if 'overwrite_if_exists' is None).
    """
    objects: list[object] = load_binary_file(file_path)
    existing_obj: object | None = find_object_in_list(objects, target_value, attr_name)
    key: str
    val: Any

    if existing_obj is not None:
        if overwrite_if_exists is None:
            overwrite_if_exists = prompt_yes_or_no(
                "This element already exists in the file. Overwrite it with the new values? (yes/no): "
            )

        if overwrite_if_exists:
            for key, val in new_obj.__dict__.items():
                setattr(existing_obj, key, val)
    else:
        objects.append(new_obj)

    save_binary_file(file_path, objects)


def delete_object_from_binary_file(
    file_path: str,
    target_value: Any,
    attr_name: str | None = None
) -> None:
    """
    Delete the first object matching 'target_value' from the binary file.
    """
    objects: list[object] = load_binary_file(file_path)
    obj_to_delete: object | None = find_object_in_list(objects, target_value, attr_name)

    if obj_to_delete is not None:
        objects.remove(obj_to_delete)
        save_binary_file(file_path, objects)
        print(f"Object matching '{target_value}' deleted from '{file_path}'.")
    else:
        print(f"No object matching '{target_value}' found in '{file_path}'.")


def get_object_values_from_binary_file(
    target_value: Any,
    file_path: str,
    attr_name: str | None = None
) -> list[Any]:
    """
    Find the object matching 'target_value' in the binary file and return its attribute values as a list.
    """
    values: list[Any] = []
    objects: list[object] = load_binary_file(file_path)
    found_obj: object | None = find_object_in_list(objects, target_value, attr_name)

    if found_obj is not None:
        values = object_to_value_list(found_obj)

    return values


def get_all_objects_values_from_binary_file(file_path: str) -> list[list[Any]]:
    """
    Return all objects stored in the binary file as a list of attribute-value lists.
    """
    all_values: list[list[Any]] = []
    objects: list[object]
    obj: object

    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found.")
    else:
        objects = load_binary_file(file_path)

        if not objects:
            print("The file is empty or could not be read.")
        else:
            for obj in objects:
                all_values.append(object_to_value_list(obj))

    return all_values


def print_objects_from_binary_file(file_path: str) -> None:
    """
    Print each object stored in the binary file as a list of its attribute values.
    """
    objects: list[object]
    obj: object

    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found.")
    else:
        objects = load_binary_file(file_path)

        if not objects:
            print("The file is empty or could not be read.")
        else:
            for obj in objects:
                print(object_to_value_list(obj))


def print_single_object_from_binary_file(
    target_value: Any,
    file_path: str,
    attr_name: str | None = None
) -> None:
    """
    Find the object matching 'target_value' in the binary file and print its attribute values.
    """
    print(str(get_object_values_from_binary_file(target_value, file_path, attr_name)))
