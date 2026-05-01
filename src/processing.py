from datetime import datetime


def filter_by_state(list_dict: list[dict], state='EXECUTED') -> list[dict]:
    """Функция возвращает новый список словарей, содержащий только те словари, у которых ключ
        'state' соответствует указанному значению."""

    return list(dict_ for dict_ in list_dict if dict_['state'] == state)


def sort_by_date(list_dicts: list[dict], ascending=True) -> list[dict]:
    """Функция принимает список словарей и необязательный параметр, задающий порядок сортировки
    (по умолчанию — убывание). Функция должна возвращать новый список, отсортированный по дате"""

    return sorted(list_dicts, key=lambda x: datetime.fromisoformat(x['date']), reverse=ascending)
