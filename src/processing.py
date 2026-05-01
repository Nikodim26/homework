def filter_by_state(list_dict: list[dict], state='EXECUTED') -> list[dict]:
    """Функция возвращает новый список словарей, содержащий только те словари, у которых ключ
        'state' соответствует указанному значению."""

    return list(dict_ for dict_ in list_dict if dict_['state'] == state)