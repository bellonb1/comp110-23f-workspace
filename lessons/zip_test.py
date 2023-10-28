"""Test my zip function."""

__author__: str = "730656976"

from zip import zip


def test_empty_zip() -> None:
    """Testing edge case of an empty list should be zero."""
    assert zip([],[]) == 0


def test_zip_fourlist() -> None:
    """Tests zip function with a list of fours."""
    assert zip(["1","2","3","4"],[1,2,3,4]) == {"1":1, "2":2, "3":3, "4":4}


def test_zip_threelist() -> None:
    """Tests zip fuinction with a list of threes."""
    assert zip(["1","2","3"],[1,2,3]) == {"1":1, "2":2, "3":3}