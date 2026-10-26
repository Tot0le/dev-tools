# 🛠️ dev-tools

**[🇬🇧 English](README.md) | [🇫🇷 Français](README.fr.md)**

Dépôt centralisé multi-langages regroupant des utilitaires de développement réutilisables, des fonctions d'aide (saisie sécurisée, fichiers binaires, affichage) et des algorithmes classiques. Conçu avec un typage strict pour être facilement importable dans des projets personnels comme académiques.

---

## 🌍 Langages supportés & Feuille de route

Ce dépôt est structuré comme un *monorepo* multi-langages évolutif :

| Langage | Dossier | Nom du package | Statut |
| :--- | :--- | :--- | :--- |
| **Python** (>= 3.10) | [`python/`](./python) | `devtools-py` | ✅ Disponible (`v0.1.0`) |
| **C / C++** | `cpp/` | — | 🚧 Prévu |

---

## 📂 Architecture du dépôt

```text
dev-tools/
├── README.md                  # Documentation en anglais
├── README.fr.md               # Documentation en français
├── docs/                      # Documentation et notes complémentaires
└── python/                    # Package d'utilitaires Python
    ├── pyproject.toml         # Configuration du package
    └── devtools_py/
        ├── __init__.py        # API publique (Anglais + Alias Français)
        ├── constants.py       # Bornes numériques (MIN_INT, MAX_INT, etc.)
        ├── cli/               # Affichage console & saisies utilisateur vérifiées
        │   ├── display.py
        │   └── inputs.py
        ├── files/             # Gestion de fichiers texte, binaires simples et binaires d'objets
        │   ├── text_io.py
        │   ├── bin_simple.py
        │   └── bin_objects.py
        ├── math_sets/         # Algorithmes mathématiques & opérations sur les ensembles
        │   ├── math_utils.py
        │   └── sets_lists.py
        └── strings/           # Comptage d'occurrences et gestion de stock de caractères
            └── occurrences.py
```

---

## 🐍 Package Python (`devtools-py`)

### 📦 Installation & Utilisation dans un projet

Cloner simplement le dépôt dans un projet ne suffit pas pour que Python trouve le sous-dossier `devtools_py`. Voici les **3 façons** d'utiliser la librairie selon votre besoin :

#### Option 1 : Copie directe du dossier (Sans `pip` — Idéal pour les TPs et rendus scolaires)
Si votre projet doit tourner sur la machine d'un correcteur sans rien installer avec `pip`, copiez uniquement le sous-dossier `devtools_py` directement à la racine de votre projet (à côté de votre `main.py`) :

```bash
git clone https://github.com/Tot0le/dev-tools.git
cp -r dev-tools/python/devtools_py ./
rm -rf dev-tools
```

#### Option 2 : Installation directe depuis GitHub avec `pip`
Dans un environnement virtuel (`venv`), installez le package directement depuis GitHub en ciblant le sous-dossier `python` :

```bash
pip install "git+https://github.com/Tot0le/dev-tools.git#subdirectory=python"
```

#### Option 3 : Installation locale en mode éditable (Sur votre machine personnelle)
Clonez ce dépôt une seule fois sur votre machine et installez-le en **mode éditable** (`-e`). Toute modification dans `dev-tools` sera immédiatement disponible partout :

```bash
git clone https://github.com/Tot0le/dev-tools.git
cd dev-tools
pip install -e ./python
```

---

### 🌐 API Bilingue (Anglais & Français)

Le cœur du code respecte les standards internationaux (anglais, PEP 8, `snake_case`), mais des **alias en français** sont exposés à la racine du package pour garantir une utilisation naturelle dans les projets et TPs en français.

```python
# Utilisation en Français (via les alias)
from devtools_py import saisir_entier, saisir_oui_ou_non, clear_console

clear_console()
age: int = saisir_entier("Entrez votre âge : ", min_val=0, max_val=120)
if saisir_oui_ou_non("Confirmer ? (o/n) : "):
    print(f"Âge enregistré : {age}")
```

```python
# Utilisation en Anglais
from devtools_py import prompt_int, prompt_yes_or_no, clear_console

clear_console()
age: int = prompt_int("Enter your age: ", min_val=0, max_val=120)
if prompt_yes_or_no("Confirm? (y/n): "):
    print(f"Recorded age: {age}")
```

---

### 📖 Référence de l'API (`devtools_py`)

#### 1. Console & Saisies Utilisateur (`devtools_py.cli`)
Outils d'affichage terminal et de saisie sécurisée avec boucles de validation (type et bornes).

| Fonction Anglaise | Alias Français | Description |
| :--- | :--- | :--- |
| `print_newlines(count=1)` | `aller_a_la_ligne` | Affiche `count` sauts de ligne dans le terminal. |
| `wait_for_enter(lang="en")` | `attendre_entree` | Met en pause jusqu'à l'appui sur Entrée (`"en"` ou `"fr"`). |
| `clear_console()` | *(Aucun)* | Efface le contenu du terminal (Windows / Linux / macOS). |
| `prompt_int(...)` | `saisir_entier` | Demande un entier compris dans `[min_val, max_val]` (inclus/exclus). |
| `prompt_float(...)` | `saisir_float` | Demande un réel compris dans `[min_val, max_val]` (inclus/exclus). |
| `prompt_choice(...)` | `saisir_choix` | Demande une chaîne appartenant à une liste de choix autorisés (`valid_choices`). |
| `prompt_filtered_str(...)` | `saisir_chaine_filtree` | Demande une chaîne ne contenant aucun des caractères interdits (`forbidden_chars`). |
| `prompt_yes_or_no(prompt)` | `saisir_oui_ou_non` | Demande une confirmation oui/non ou yes/no (`bool`). |

#### 2. Gestion de Fichiers (`devtools_py.files`)
Séparation claire entre les fichiers texte, les fichiers binaires (`pickle`) stockant des types simples et ceux manipulant des instances de classes.

* **Fichiers Texte (`text_io.py`)**

| Fonction Anglaise | Alias Français | Description |
| :--- | :--- | :--- |
| `count_file_lines(file_path)` | `compter_lignes_fichier` | Compte et retourne le nombre de lignes d'un fichier texte UTF-8. |
| `clear_file_content(file_path)` | `effacer_contenu_fichier` | Vide intégralement le contenu d'un fichier sans le supprimer. |

* **Fichiers Binaires Simples (`bin_simple.py`)**

| Fonction Anglaise | Alias Français | Description |
| :--- | :--- | :--- |
| `load_binary_file(file_path)` | `charger_fichier_bin` | Charge la liste stockée dans un fichier binaire (retourne `[]` si absent/corrompu). |
| `save_binary_file(file_path, data)` | `sauvegarder_fichier_bin` | Sauvegarde une liste dans un fichier binaire. |
| `append_to_binary_file(file_path, item)` | `ajouter_dans_fichier_bin` | Ajoute un élément simple à la fin de la liste d'un fichier binaire. |
| `print_binary_file(file_path)` | `afficher_fichier_bin` | Affiche le contenu brut d'un fichier binaire simple. |

* **Fichiers Binaires d'Instances de Classes (`bin_objects.py`)**

| Fonction Anglaise | Alias Français | Description |
| :--- | :--- | :--- |
| `object_to_value_list(obj)` | `objet_vers_liste` | Extrait les valeurs des attributs d'un objet sous forme de liste. |
| `find_object_in_list(objects, target_value, attr_name=None)` | `trouver_objet_dans_liste` | Cherche le premier objet correspondant à `target_value` (sur `attr_name` ou tous les attributs). |
| `is_object_in_list(objects, target_value, attr_name=None)` | `objet_est_dans_liste` | Retourne `True` si l'objet recherché est présent dans la liste. |
| `upsert_object_in_binary_file(...)` | `ajouter_ou_modifier_objet_bin` | Ajoute un objet dans le fichier binaire, ou met à jour ses attributs s'il existe déjà. |
| `delete_object_from_binary_file(...)` | `supprimer_objet_fichier_bin` | Supprime du fichier binaire le premier objet correspondant à `target_value`. |
| `get_object_values_from_binary_file(...)` | `obtenir_valeurs_objet_bin` | Retourne la liste des valeurs d'attributs d'un objet précis du fichier binaire. |
| `get_all_objects_values_from_binary_file(file_path)` | `obtenir_toutes_valeurs_objets_bin` | Retourne tous les objets du fichier sous forme de liste de listes de valeurs. |
| `print_objects_from_binary_file(file_path)` | `afficher_objets_fichier_bin` | Affiche les valeurs d'attributs de chaque objet du fichier binaire. |
| `print_single_object_from_binary_file(...)` | `afficher_objet_fichier_bin` | Affiche les valeurs d'attributs d'un objet précis du fichier binaire. |

#### 3. Occurrences de Caractères (`devtools_py.strings`)
Gestion de compteurs mutables `[caractere, quantite]`, utile pour les jeux de lettres, l'analyse de texte ou la vérification de stock d'éléments.

| Fonction Anglaise | Alias Français | Description |
| :--- | :--- | :--- |
| `count_char_occurrences(text, target_chars=None)` | `compter_occurrences` | Génère la liste des paires `[caractere, quantite]` présentes dans `text`. |
| `decrement_char_occurrence(occurrences, char)` | `decrementer_occurrence` | Décrémente de 1 le compteur associé à `char`. |
| `increment_char_occurrence(occurrences, char)` | `incrementer_occurrence` | Incrémente de 1 le compteur associé à `char`. |
| `has_remaining_count(occurrences, char)` | `a_quantite_restante` | Retourne `True` si le compteur de `char` est strictement supérieur à 0. |

#### 4. Mathématiques & Ensembles (`devtools_py.math_sets`)
> **Note :** Plusieurs fonctions de ce module (`factorial`, `is_prime`, `fibonacci_*`, opérations ensemblistes sur des `list`) sont issues de travaux pratiques d'algorithmique. En production, privilégiez `math.factorial` et le type natif `set` de Python.

| Fonction Anglaise | Alias Français | Description |
| :--- | :--- | :--- |
| `is_prime(number)` | `est_premier` | Vérifie si un entier est un nombre premier. |
| `fibonacci_iterative(k)` | *(Aucun)* | Calcule le *k*-ième terme de Fibonacci de manière itérative. |
| `fibonacci_recursive(k)` | *(Aucun)* | Calcule le *k*-ième terme de Fibonacci de manière récursive. |
| `factorial(number)` | `factorielle` | Calcule `number!` de manière récursive. |
| `generate_random_int_list(count, min_val, max_val)` | `generer_liste_entiers_aleatoires` | Génère une liste de `count` entiers aléatoires. |
| `count_duplicate_values(items)` | `compter_valeurs_en_doublon` | Compte combien de valeurs apparaissent plusieurs fois dans la liste. |
| `count_distinct_values(items)` | `compter_valeurs_distinctes` | Compte le nombre total de valeurs distinctes dans la liste. |
| `is_set(items)` | `est_un_ensemble` | Retourne `True` si la liste ne contient aucun doublon. |
| `add_to_set(value, items)` | `ajouter_si_absent` | Retourne une copie de `items` avec `value` ajouté (lève `ValueError` si `items` contient des doublons). |
| `union(set_a, set_b)` | *(Aucun)* | Retourne l'union de deux listes sans doublons. |
| `intersection(set_a, set_b)` | *(Aucun)* | Retourne l'intersection de deux listes sans doublons. |
| `difference(set_a, set_b)` | *(Aucun)* | Retourne le tuple `(set_a \ set_b, set_b \ set_a)`. |
| `are_disjoint(set_a, set_b)` | `sont_disjointes` | Retourne `True` si les deux listes n'ont aucun élément en commun. |
