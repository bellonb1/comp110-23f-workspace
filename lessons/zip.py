"""Combining two lists into a dictionary."""

__author__: str = "730656976"


def zip(first_list: list[str], second_list: list[int]) -> dict[str, int]:
    """Combines two lists to create a dictionary."""
    return_dict: dict[str, int] = dict()
    if len(first_list) != len(second_list):
        return return_dict

    for i in range(len(first_list)):
        return_dict[first_list[i]] = second_list[i]
    return return_dict