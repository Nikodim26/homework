from src.masks import get_mask_card_number, get_mask_account


def test_get_mask_card_number():
    assert get_mask_card_number('1234567891011121') == '1234 56** **** 1121'


def test_get_mask_account():
    assert get_mask_account('40817810400210001236') == '**1236'