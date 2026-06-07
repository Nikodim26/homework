from src.external_api import currency_conversion


def test_currency_conversion(fixture_for_test_currency_conversion):
    assert currency_conversion({}) is None
    assert currency_conversion(fixture_for_test_currency_conversion) == '31957.58'
