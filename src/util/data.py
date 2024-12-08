import copy

CAT = {
    "VERB": [],
    "NOUN": [],
    "ADJ": [],
    "ADV": [],
    "PRON": [],
    "DET": [],
    "ADP": [],
    "AUX": [],
    "CONJ": [],
    "NUM": [],
    "PUNCT": [],
    "OTHER": []
}
CAT_NUMS = {
    "VERB": 0,
    "NOUN": 0,
    "ADJ": 0,
    "ADV": 0,
    "PRON": 0,
    "DET": 0,
    "ADP": 0,
    "AUX": 0,
    "CONJ": 0,
    "NUM": 0,
    "PUNCT": 0,
    "OTHER": 0
}


def get_cat_copy():
    return copy.deepcopy(CAT)


def get_cat_num_copy():
    return copy.deepcopy(CAT_NUMS)


def read_file(filename='text.txt'):
    content = ""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return "File was not found"
    except Exception as e:
        return f"Something went wrong: {e}"
