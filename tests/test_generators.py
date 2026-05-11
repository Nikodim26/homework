from src.generators import transaction_descriptions, card_number_generator, filter_by_currency


def test_filter_by_currency(fixture_for_generators:list[dict]) -> None:
    descriptions = filter_by_currency(fixture_for_generators, "USD")
    assert next(descriptions) == {
        'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572',
        'operationAmount': {'amount': '9824.07', 'currency': {'name': 'USD', 'code': 'USD'}},
        'description': 'Перевод организации', 'from': 'Счет 75106830613657916952',
        'to': 'Счет 11776614605963066702'}

    descriptions = filter_by_currency(fixture_for_generators, "RUB")
    assert next(descriptions) == {
        'id': 873106923, 'state': 'EXECUTED', 'date': '2019-03-23T01:09:46.296404',
        'operationAmount': {'amount': '43318.34', 'currency': {'name': 'руб.', 'code': 'RUB'}},
        'description': 'Перевод со счета на счет', 'from': 'Счет 44812258784861134719',
        'to': 'Счет 74489636417521191160'}


def test_transaction_descriptions(fixture_for_generators: list[dict]) -> None:
    descriptions = transaction_descriptions(fixture_for_generators)
    assert next(descriptions) == 'Перевод организации'
    assert next(descriptions) == 'Перевод со счета на счет'


def test_card_number_generator() -> None:
    descriptions = card_number_generator(3, 15)
    assert next(descriptions) == '0000 0000 0000 0003'
    assert next(descriptions) == '0000 0000 0000 0004'
    assert next(descriptions) == '0000 0000 0000 0005'
