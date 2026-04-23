from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(account_or_number:"str")->str:
    """Обрабатывает информацию как о картах, так и о счетах"""

    number=""
    premeditation = ""
    for ch in account_or_number:
        if ch.isdigit():
            number+=ch
        else:
            premeditation+=ch
    if len(number) == 16:
        return premeditation + get_mask_card_number(number)
    else:
        return premeditation + get_mask_account(number)


print(mask_account_card('Visa Platinum 7000792289606361'))
print(mask_account_card('Maestro 7000792289606361'))
print(mask_account_card('Счет 73654108430135874305'))