"""Collection of functions which involve dictionaries."""

__author__: str = "730656976"


def invert(invert: dict[str, str]) -> dict[str, str]:
    """Inverts the contents of a string dictionary."""
    new_invert: dict[str, str] = dict()
    for key in invert:
        new_invert[invert[key]] = key
    if(len(invert) != len(new_invert)):
        raise KeyError("Multiple keys correspond to one value.")
    print(new_invert)


def favorite_color(color: dict[str, str]) -> str:
    """Returns the most frequent value of a dictionary."""
    counter_dict: dict[str, int] = dict()
    highest: int = 0
    return_str: str = ""
    #Creates a new dict and assigns its key as the value of the original dictionary. The Value is an integer that counts up for each key and value.
    for key in color:
        if color[key] in counter_dict:
            counter_dict[color[key]] += 1
        else:
            counter_dict[color[key]] = 1
    #Everytime a new highest value is found the return value is changed to its key
    for key in counter_dict:
        if counter_dict[key] > highest:
            highest = counter_dict[key]
            return_str = key
    return return_str


def count(count_list: list[str]) -> dict[str,int]:
    """Returns the count of values present in list."""
    return_dict: dict[str, int] = dict()
    for i in range(len(count_list)):
        if count_list[i] in return_dict:
            return_dict[count_list[i]] = return_dict[count_list[i]] + 1
        else:
            return_dict[count_list[i]] = 1
    return return_dict

def alphabetizer(i_list: list[str]) -> dict[str, list[str]]:
    """Sorts list into a dictionary of lists where the key is their first letter."""
    return_dict: dict[str, list[str]] = dict()
    for i in range(len(i_list)):
        if i_list[i][0] not in return_dict:
            return_dict[i_list[i][0].lower()] = [i_list[i]]
        else:
            return_dict[i_list[i][0].lower()].append(i_list[i])
    return return_dict


def update_attendance(initial_dict: dict[str, list[str]], day: str, name: str) -> dict[str, list[str]]:
    """Will update attendence with the given name and date. Initial D."""
    if day in initial_dict:
        if name not in initial_dict:
            initial_dict[day].append(name)
    else:
        initial_dict[day] = [name]
    return initial_dict