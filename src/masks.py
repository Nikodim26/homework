def get_mask_card_number(number: str) -> str:
    """Принимает на вход номер карты в виде строки и возвращает маску номера по правилу
    "XXX XX** **** XXXX" """

    number = number[:6] + "******" + number[-4:]
    number = number[:4] + " " + number[4:8] + " " + number[8:12] + " " + number[-4:]

    return number


def get_mask_account(account: str) -> str:
    """принимает на вход номер счета в виде строки и возвращает маску номера по правилу
    "*XXXX" """

    return "**" + account[-4:]
