from unittest.mock import patch

from src.external_api import currency_conversion

transaction = {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {"amount": "100", "currency": {"name": "USD", "code": "USD"}
                        }
}


def test_currency_conversion(fixture_for_test_currency_conversion):
    assert currency_conversion({}) is None
    assert currency_conversion(fixture_for_test_currency_conversion) == '31957.58'


@patch('requests.get')
def test_currency_conversion2(mock_get):
    mock_get.return_value.json.return_value = {"Valute": {"USD": {"Value": 52.3172}}}
    assert currency_conversion(transaction) is None
    mock_get.assert_called_once_with('https://www.cbr-xml-daily.ru/daily_json.js')
