from typing import Any, Generator


def filter_by_currency(transactions: list[dict], currency: str) -> Generator[dict, Any, None]:
    """Принимает на вход список словарей, представляющих транзакции.
    Функция возвращает итератор, который поочередно выдает транзакции, где валюта операции соответствует
    заданной (например, USD)."""

    return (i for i in transactions if i["operationAmount"]["currency"]["code"] == currency)


def transaction_descriptions(transactions: list[dict]) -> Generator[dict, Any, None]:
    """Принимает список словарей с транзакциями и возвращает описание каждой операции по очереди."""

    return (i["description"] for i in transactions)


def card_number_generator(start_of_range: int, end_of_range: int) -> Generator[str]:
    """Выдает номера банковских карт в формате "XXXX XXXX XXXX XXXX", где X — цифра номера карты.
    Может сгенерировать номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999"""

    for i in range(start_of_range, end_of_range + 1):
        card_number = ''
        for j in range(17 - len(str(end_of_range))):
            card_number += '0'

        card_number += str(i)

        yield card_number[:4] + " " + card_number[4:8] + " " + card_number[8:12] + " " + card_number[-4:]
