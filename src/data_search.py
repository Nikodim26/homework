def process_bank_search(data: list[dict], search_string: str) -> list[dict]:
    """Ищет в данных нужные, обусловленные определенными критериями"""

    return [dict_data for dict_data in data if search_string in str(dict_data)]
