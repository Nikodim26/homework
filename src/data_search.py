import json
import re


def process_bank_search(data: list[dict], search_string: str) -> list[dict]:
    """Ищет в данных нужные, обусловленные определенными критериями"""
    res=[]
    for i in data:
        data_json = re.sub(r"[\"()\[\]{}]", "", json.dumps(i, ensure_ascii=False))
        if search_string.lower() in data_json.lower():
            res.append(i)
    return res


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """Собирает статистику об операциях - их количестве"""
    descriptions = set(dict_data.get("description") for dict_data in data if dict_data.get("description"))
    result = {}
    for description in descriptions:
        if description in categories:
            result[description] = len(process_bank_search(data, description))

    return result