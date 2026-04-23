from src.masks import get_mask_card_number, get_mask_account


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


aaa = ['Maestro 1596837868705199',
       'Счет 64686473678894779589',
       'MasterCard 7158300734726758',
       'Счет 35383033474447895560',
       'Visa Classic 6831982476737658',
       'Visa Platinum 8990922113665229',
       'Visa Gold 5999414228426353',
       'Счет 73654108430135874305']
for i in aaa:
    print(mask_account_card(i))