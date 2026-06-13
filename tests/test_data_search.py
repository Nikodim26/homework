from src.data_search import process_bank_operations
from src.data_search import process_bank_search


def test_process_bank_search(fixture_for_generators) -> None:
    assert process_bank_search(fixture_for_generators, "Перевод с карты на карту") == [
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
    ]
    assert process_bank_search(fixture_for_generators, "ERR") == []


def test_process_bank_operations(fixture_for_generators) -> None:
    assert process_bank_operations(fixture_for_generators, ["Перевод с карты на карту"]) == {
        "Перевод с карты на карту": 1
    }
    assert process_bank_operations(fixture_for_generators, ["Перевод со счета на счет"]) == {
        "Перевод со счета на счет": 2
    }
