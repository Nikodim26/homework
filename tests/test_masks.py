import pytest

from src.masks import get_mask_account
from src.masks import get_mask_card_number


@pytest.mark.parametrize(
    "x, expected",
    [
        ("1234567891011121", "1234 56** **** 1121"),
        ("2200255555555555", "2200 25** **** 5555"),
    ],
)
def test_get_mask_card_number(x: str, expected: str) -> None:
    assert get_mask_card_number(x) == expected


@pytest.mark.parametrize(
    "x, expected",
    [
        ("40817810400210001236", "**1236"),
        ("22002555555555551111", "**1111"),
    ],
)
def test_get_mask_account(x: str, expected: str) -> None:
    assert get_mask_account(x) == expected
