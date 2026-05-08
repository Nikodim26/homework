import pytest

from src.widget import get_date
from src.widget import mask_account_card


@pytest.mark.parametrize(
    "x, y, expected_x, expected_y ",
    [
        ("1234567891011121", "40817810400210001236", "1234 56** **** 1121", "**1236"),
        ("2200255555555555", "22002555555555552222", "2200 25** **** 5555", "**2222"),
    ],
)
def test_mask_account_card(x: str, y: str, expected_x: str, expected_y: str) -> None:
    assert mask_account_card(x) == expected_x
    assert mask_account_card(y) == expected_y


@pytest.mark.parametrize(
    "x, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2025-06-11T02:26:18.671407", "11.06.2025"),
    ],
)
def test_get_date(x: str, expected: str) -> None:
    assert get_date(x) == expected
