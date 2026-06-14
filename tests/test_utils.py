from unittest.mock import patch

from src.utils import about_financial_transactions_csv
from src.utils import about_financial_transactions_json
from src.utils import about_financial_transactions_xlsx


def test_about_financial_transactions() -> None:
    assert about_financial_transactions_json("") == []
    assert type(about_financial_transactions_json("operations.json")) == list
    assert type(about_financial_transactions_json("operations.json")[0]) == dict


@patch("csv.DictReader")
def test_about_financial_transactions_csv_(mock_get) -> None:
    mock_get.return_value[0] = {"id", "650703", "state", "EXECUTED"}
    assert about_financial_transactions_csv("") == []


def test_about_financial_transactions_csv() -> None:
    assert about_financial_transactions_csv("") == []


def test_about_financial_transactions_xlsx() -> None:
    assert about_financial_transactions_xlsx("") == []
