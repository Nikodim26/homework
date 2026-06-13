import json
import re
from collections import Counter


def process_bank_search(list_data: list[dict], search_string: str) -> list[dict]:
    """Ищет в данных нужные, обусловленные определенными критериями"""

    pattern = re.compile(rf"{search_string.lower()}")
    return [data for data in list_data if pattern.search(json.dumps(data['description'], ensure_ascii=False).lower())]


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """Собирает статистику об операциях - их количестве"""
    types_of_categories = []
    for categori in categories:
        category_matching_dictionary = process_bank_search(data, categori)
        types_of_categories.extend([categori] * len(category_matching_dictionary))

    return dict(Counter(types_of_categories))