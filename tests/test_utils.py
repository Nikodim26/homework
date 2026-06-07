from src.utils import about_financial_transactions


def test_about_financial_transactions():
    assert about_financial_transactions('') == []
    assert type(about_financial_transactions('operations.json')) == list
    assert type(about_financial_transactions('operations.json')[0]) == dict
