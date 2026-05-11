from typing import Any, Generator


def filter_by_currency(transactions: list[dict], currency: str) -> Generator[dict, Any, None]:
    """Принимает на вход список словарей, представляющих транзакции.
    Функция возвращает итератор, который поочередно выдает транзакции, где валюта операции соответствует
    заданной (например, USD)."""


    return (i for i in transactions if i["operationAmount"]["currency"]["code"] == currency)
