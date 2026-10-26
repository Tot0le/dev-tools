# 🛠️ dev-tools

**[🇬🇧 English](README.md) | [🇫🇷 Français](README.fr.md)**

A centralized, multi-language repository of reusable development utilities, helper functions, and standard algorithms. Designed to be clean, strictly typed, and easily importable across personal and academic projects.

---

## 🌍 Supported Languages & Roadmap

This repository is structured as a multi-language monorepo:

| Language | Directory | Package Name | Status |
| :--- | :--- | :--- | :--- |
| **Python** (>= 3.10) | [`python/`](./python) | `devtools-py` | ✅ Available (`v0.1.0`) |
| **C / C++** | `cpp/` | — | 🚧 Planned |

---

## 📂 Repository Structure

```text
dev-tools/
├── README.md                  # English documentation
├── README.fr.md               # French documentation
├── docs/                      # Additional documentation & notes
└── python/                    # Python utilities package
    ├── pyproject.toml         # Package configuration
    └── devtools_py/
        ├── __init__.py        # Public API & French aliases
        ├── constants.py       # Numeric bounds (MIN_INT, MAX_INT, etc.)
        ├── cli/               # Terminal display & validated user prompts
        │   ├── display.py
        │   └── inputs.py
        ├── files/             # Text, simple binary, and object binary I/O
        │   ├── text_io.py
        │   ├── bin_simple.py
        │   └── bin_objects.py
        ├── math_sets/         # Academic math & set operations on lists
        │   ├── math_utils.py
        │   └── sets_lists.py
        └── strings/           # Character frequency & stock management
            └── occurrences.py
```

---

## 🐍 Python Package (`devtools-py`)

### 📦 Installation & Setup

Simply cloning the repository inside a project folder is not enough for Python to locate `devtools_py` automatically. Choose one of the following **3 methods** depending on your needs:

#### Option 1: Standalone Copy (No `pip` required — Best for school/university assignments)
If you need your project to run on another machine (e.g., a teacher's computer) without installing external packages, copy the `devtools_py` folder directly next to your `main.py`:

```bash
git clone https://github.com/Tot0le/dev-tools.git
cp -r dev-tools/python/devtools_py ./
rm -rf dev-tools
```

#### Option 2: Install directly from GitHub via `pip`
Inside a virtual environment (`venv`), install the package directly from the `python` subdirectory on GitHub:

```bash
pip install "git+https://github.com/Tot0le/dev-tools.git#subdirectory=python"
```

#### Option 3: Local Editable Install (For personal development on your machine)
Clone this repository once on your computer and install it in **editable mode** (`-e`). Any changes pulled or made in `dev-tools` will immediately apply everywhere:

```bash
git clone https://github.com/Tot0le/dev-tools.git
cd dev-tools
pip install -e ./python
```

---

### 🌐 Bilingual API (English & French)

While the core codebase is written in strict PEP 8 English, full **French aliases** are exposed at the package level to maintain seamless compatibility with French-language academic projects.

```python
# English API usage
from devtools_py import prompt_int, prompt_yes_or_no, clear_console

clear_console()
age: int = prompt_int("Enter your age: ", min_val=0, max_val=120)
if prompt_yes_or_no("Confirm? (y/n): "):
    print(f"Recorded age: {age}")
```

```python
# French API usage (Aliases pointing to the exact same functions)
from devtools_py import saisir_entier, saisir_oui_ou_non, clear_console

clear_console()
age: int = saisir_entier("Entrez votre âge : ", min_val=0, max_val=120)
if saisir_oui_ou_non("Confirmer ? (o/n) : "):
    print(f"Âge enregistré : {age}")
```

---

### 📖 API Reference (`devtools_py`)

#### 1. CLI & Validated User Inputs (`devtools_py.cli`)
Utilities for terminal display and safe, loop-validated user input.

| English Function | French Alias | Description |
| :--- | :--- | :--- |
| `print_newlines(count=1)` | `aller_a_la_ligne` | Print `count` blank lines to the console. |
| `wait_for_enter(lang="en")` | `attendre_entree` | Pause execution until the user presses Enter (`"en"` or `"fr"`). |
| `clear_console()` | *(None)* | Clear the terminal screen (cross-platform). |
| `prompt_int(...)` | `saisir_entier` | Prompt for an integer within `[min_val, max_val]` (inclusive/exclusive). |
| `prompt_float(...)` | `saisir_float` | Prompt for a float within `[min_val, max_val]` (inclusive/exclusive). |
| `prompt_choice(...)` | `saisir_choix` | Prompt for a string among a list of `valid_choices`. |
| `prompt_filtered_str(...)` | `saisir_chaine_filtree` | Prompt for a string containing none of the `forbidden_chars`. |
| `prompt_yes_or_no(prompt)` | `saisir_oui_ou_non` | Prompt for a yes/no or oui/non confirmation (`bool`). |

#### 2. File Handling (`devtools_py.files`)
Separated into plain text utilities, simple `pickle` binary lists, and structured `pickle` binary files storing class instances.

* **Text Files (`text_io.py`)**

| English Function | French Alias | Description |
| :--- | :--- | :--- |
| `count_file_lines(file_path)` | `compter_lignes_fichier` | Count total lines in a UTF-8 text file. |
| `clear_file_content(file_path)` | `effacer_contenu_fichier` | Truncate a file to 0 bytes without deleting it. |

* **Simple Binary Files (`bin_simple.py`)**

| English Function | French Alias | Description |
| :--- | :--- | :--- |
| `load_binary_file(file_path)` | `charger_fichier_bin` | Load a list from a binary file (returns `[]` if missing/corrupted). |
| `save_binary_file(file_path, data)` | `sauvegarder_fichier_bin` | Save a list to a binary file. |
| `append_to_binary_file(file_path, item)` | `ajouter_dans_fichier_bin` | Append a single item to a binary file's list. |
| `print_binary_file(file_path)` | `afficher_fichier_bin` | Print the raw content of a binary file. |

* **Class Instance Binary Files (`bin_objects.py`)**

| English Function | French Alias | Description |
| :--- | :--- | :--- |
| `object_to_value_list(obj)` | `objet_vers_liste` | Extract an object's attribute values as a `list`. |
| `find_object_in_list(objects, target_value, attr_name=None)` | `trouver_objet_dans_liste` | Find the first object matching `target_value` (in `attr_name` or any attribute). |
| `is_object_in_list(objects, target_value, attr_name=None)` | `objet_est_dans_liste` | Return `True` if a matching object exists in the list. |
| `upsert_object_in_binary_file(...)` | `ajouter_ou_modifier_objet_bin` | Insert a new object or update an existing matching object in a binary file. |
| `delete_object_from_binary_file(...)` | `supprimer_objet_fichier_bin` | Remove the first object matching `target_value` from a binary file. |
| `get_object_values_from_binary_file(...)` | `obtenir_valeurs_objet_bin` | Return the attribute values list of a matching object from a binary file. |
| `get_all_objects_values_from_binary_file(file_path)` | `obtenir_toutes_valeurs_objets_bin` | Return all stored objects as a list of attribute-value lists. |
| `print_objects_from_binary_file(file_path)` | `afficher_objets_fichier_bin` | Print each stored object's attribute values. |
| `print_single_object_from_binary_file(...)` | `afficher_objet_fichier_bin` | Print the attribute values of a single matching object. |

#### 3. Character Occurrences (`devtools_py.strings`)
Mutable frequency counters `[char, count]` useful for word games, parsers, and inventory checks.

| English Function | French Alias | Description |
| :--- | :--- | :--- |
| `count_char_occurrences(text, target_chars=None)` | `compter_occurrences` | Return a list of `[char, count]` pairs for characters in `text`. |
| `decrement_char_occurrence(occurrences, char)` | `decrementer_occurrence` | Decrement the counter for `char` by 1. |
| `increment_char_occurrence(occurrences, char)` | `incrementer_occurrence` | Increment the counter for `char` by 1. |
| `has_remaining_count(occurrences, char)` | `a_quantite_restante` | Return `True` if `char` has a remaining count strictly greater than 0. |

#### 4. Mathematics & Set Operations (`devtools_py.math_sets`)
> **Note:** Several functions in this module (`factorial`, `is_prime`, `fibonacci_*`, list-based set operations) were originally implemented for algorithmic coursework. For production performance, prefer Python's native `math.factorial` and built-in `set` type.

| English Function | French Alias | Description |
| :--- | :--- | :--- |
| `is_prime(number)` | `est_premier` | Check whether an integer is prime. |
| `fibonacci_iterative(k)` | *(None)* | Compute the *k*-th Fibonacci term iteratively. |
| `fibonacci_recursive(k)` | *(None)* | Compute the *k*-th Fibonacci term recursively. |
| `factorial(number)` | `factorielle` | Compute `number!` recursively. |
| `generate_random_int_list(count, min_val, max_val)` | `generer_liste_entiers_aleatoires` | Generate a list of `count` random integers. |
| `count_duplicate_values(items)` | `compter_valeurs_en_doublon` | Count how many values appear more than once in `items`. |
| `count_distinct_values(items)` | `compter_valeurs_distinctes` | Count the number of unique values in `items`. |
| `is_set(items)` | `est_un_ensemble` | Return `True` if `items` contains no duplicates. |
| `add_to_set(value, items)` | `ajouter_si_absent` | Return a copy of `items` with `value` added (raises `ValueError` if `items` has duplicates). |
| `union(set_a, set_b)` | *(None)* | Return the union of two duplicate-free lists. |
| `intersection(set_a, set_b)` | *(None)* | Return the intersection of two duplicate-free lists. |
| `difference(set_a, set_b)` | *(None)* | Return `(set_a \ set_b, set_b \ set_a)`. |
| `are_disjoint(set_a, set_b)` | `sont_disjointes` | Return `True` if `set_a` and `set_b` share no common elements. |
