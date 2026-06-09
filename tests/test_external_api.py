from unittest.mock import patch

from src.external_api import currency_conversion


def test_currency_conversion(fixture_for_test_currency_conversion) -> None:
    assert currency_conversion({}) is None
    assert currency_conversion(fixture_for_test_currency_conversion) == 31957.58


@patch("requests.get")
def test_currency_conversion2(mock_get, fixture_for_test_currency_conversion_val) -> None:
    mock_get.return_value.json.return_value = {"Valute": {"USD": {"Value": 52.3172}}}
    assert currency_conversion(fixture_for_test_currency_conversion_val) is None
    mock_get.assert_called_once_with("https://www.cbr-xml-daily.ru/daily_json.js")
