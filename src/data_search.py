import json
import re
from collections import Counter


def process_bank_search(data: list[dict], search_string: str) -> list[dict]:
    """Ищет в данных нужные, обусловленные определенными критериями"""
    res = []
    for i in data:
        data_json = re.sub(r"[\"()\[\]{}]", "", json.dumps(i, ensure_ascii=False))
        if search_string.lower() in data_json.lower():
            res.append(i)
    return res


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """Собирает статистику об операциях - их количестве"""
    types_of_categories = []
    for categori in categories:
        category_matching_dictionary = process_bank_search(data, categori)
        for category_matching in category_matching_dictionary:
            types_of_categories.append(categori)

    return dict(Counter(types_of_categories))
