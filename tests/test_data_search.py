from src.data_search import process_bank_search, process_bank_operations


def test_process_bank_search(fixture_end_sort_by_date) -> None:
    assert (process_bank_search(fixture_end_sort_by_date, '2018-06-30T02:08:58.425572') ==
            [{"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"}])
    assert process_bank_search(fixture_end_sort_by_date, 'ERR') == []


def test_process_bank_operations(fixture_for_generators) -> None:
    assert process_bank_operations(fixture_for_generators, 'Перевод с карты на карту') == {
        'Перевод с карты на карту': 1}
    assert process_bank_operations(fixture_for_generators, "Перевод со счета на счет") == {
        "Перевод со счета на счет": 2}
