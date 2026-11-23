import pytest

from test_ai_bug import find_max


def test_find_max_returns_largest_score():
	assert find_max([70, 85, 60, 95]) == 95


def test_find_max_when_largest_is_in_middle():
	assert find_max([70, 95, 60, 85]) == 95


def test_find_max_with_one_score():
	assert find_max([42]) == 42


def test_find_max_with_two_scores():
	assert find_max([42, 75]) == 75


def test_find_max_with_duplicate_largest_scores():
	assert find_max([95, 70, 95]) == 95


def test_find_max_with_empty_list_raises_index_error():
	with pytest.raises(IndexError):
		find_max([])
