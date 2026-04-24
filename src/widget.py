from datetime import datetime

from src.masks import get_mask_account
from src.masks import get_mask_card_number


def mask_account_card(account_or_number: "str") -> str:
    """Обрабатывает информацию как о картах, так и о счетах"""

    number = ""
    premeditation = ""
    for ch in account_or_number:
        if ch.isdigit():
            number += ch
        else:
            premeditation += ch

    if len(number) == 16:
        return premeditation + get_mask_card_number(number)
    else:
        return premeditation + get_mask_account(number)


def get_date(data_time: str) -> str:
    """принимает на вход строку с датой в формате "2024-03-11T02:26:18.671407"
    и возвращает строку с датой в формате "ДД.ММ.ГГГГ  ("11.03.2024")"""

    dt_naive = datetime.fromisoformat(data_time).strftime("%d-%m-%Y")

    return dt_naive.replace('-','.')

