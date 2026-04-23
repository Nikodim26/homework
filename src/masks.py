def get_mask_card_number(number: str) -> str:
    """Принимает на вход номер карты в виде строки и возвращает маску номера по правилу
    "XXX XX** **** XXXX" """

    number = number.replace(" ", "")  # На случай, если ввод с пробелами
    number = number[:6] + "******" + number[-4:]
    number = number[:4] + " " + number[4:8] + " " + number[8:12] + " " + number[-4:]

    return number


def get_mask_account(account: str) -> str:
    """принимает на вход номер счета в виде строки и возвращает маску номера по правилу
    "*XXXX" """

    return "**" + account[-4:]


# print(get_mask_card_number("1234 5678 9101 1213"))
# print(get_mask_card_number("1234567891011213"))
# print(get_mask_account("73654108430135874305"))
