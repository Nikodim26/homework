from src.processing import filter_by_state, sort_by_date


def test_filter_by_state(fixture_for_filter_by_state, fixture_end_for_filter_by_state):
    assert filter_by_state(fixture_for_filter_by_state) == fixture_end_for_filter_by_state

def test_sort_by_date(fixture_for_sort_by_date,fixture_end_sort_by_date):
    assert sort_by_date(fixture_for_sort_by_date) == fixture_end_sort_by_date