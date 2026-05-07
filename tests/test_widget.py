from src.widget import mask_account_card, get_date


def test_mask_account_card():
    assert mask_account_card('1234567891011121') == '1234 56** **** 1121'
    assert mask_account_card('40817810400210001236') == '**1236'


def test_get_date():
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"
