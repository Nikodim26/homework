from src.processing import filter_by_state
from src.processing import sort_by_date


def test_filter_by_state(fixture_for_processing: list[dict], fixture_end_for_filter_by_state: list[dict]) -> None:
    assert filter_by_state(fixture_for_processing) == fixture_end_for_filter_by_state


def test_sort_by_date(fixture_for_processing: list[dict], fixture_end_sort_by_date: list[dict]) -> None:
    assert sort_by_date(fixture_for_processing) == fixture_end_sort_by_date
