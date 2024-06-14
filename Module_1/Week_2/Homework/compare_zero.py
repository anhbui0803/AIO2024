def function_helper(x):
    # Your code here
    # Neu x > 0 return "T", else return "N"
    if x > 0:
        return "T"
    return "N"


def compare_zero(num_list):
    res = [function_helper(num) for num in num_list]
    return res


if __name__ == '__main__':
    assert compare_zero([10, 0, -10, -1]) == ["T", "N", "N", "N"]
    print(compare_zero([2, 3, 5, -1]))
