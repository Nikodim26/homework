import json


def process_bank_search(data: list[dict], search_string: str) -> list[dict]:
    """Ищет в данных нужные, обусловленные определенными критериями"""

    return [dict_data for dict_data in data if search_string in json.dumps(dict_data, ensure_ascii=False)]


def process_bank_operations(data: list[dict], categories: list) -> dict:
    descriptions = set(dict_data.get('description') for dict_data in data if dict_data.get('description'))
    result = {}
    for description in descriptions:
        if description in categories:
            result[description] = len(process_bank_search(data, description))

    return result
