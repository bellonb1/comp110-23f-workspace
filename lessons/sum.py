"""Summing the elements of a list using different loops.""" 

__author__: str = "730656976"


def w_sum(vals: list[float]) -> float:
    """Sums elements of a list using while loop."""
    index: int = 0
    sum: float = 0
    while index < len(vals):
        sum += vals[index]
        index += 1
    return sum


def f_sum(vals: list[float]) -> float:
    """Sums elements of a list using for loop."""
    sum: float = 0
    for v in vals:
        sum += v
    return sum


def f_range_sum(vals: list[float]) -> float:
    """Sums elements of a list using for loop (range)."""
    sum: float = 0
    for i in range(len(vals)):
        sum += vals[i]
    return sum
