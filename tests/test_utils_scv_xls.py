from unittest.mock import patch

from src.utils_scv_xls import about_financial_transactions_csv
from src.utils_scv_xls import about_financial_transactions_xlsx


@patch("csv.DictReader")
def test_about_financial_transactions_csv_(mock_get) -> None:
    mock_get.return_value[0] = {"id", "650703", "state", "EXECUTED"}
    assert about_financial_transactions_csv("") == []


def test_about_financial_transactions_csv() -> None:
    assert about_financial_transactions_csv("") == []


def test_about_financial_transactions_xlsx() -> None:
    assert about_financial_transactions_xlsx("") == []
