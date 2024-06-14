from icecream import ic
from collections import Counter


def count_char(string):
    # Use built in function
    # counter = Counter(string)

    # Implement from scratch
    counter = {}
    for char in string:
        if char in counter:
            counter[char] += 1
        else:
            counter[char] = 1

    return counter


if __name__ == "__main__":
    assert count_char("Baby") == {"B": 1, "a": 1, "b": 1, "y": 1}
    print(count_char("smiles"))  # {'s': 2, 'm': 1, 'i': 1, 'l': 1, 'e': 1}
