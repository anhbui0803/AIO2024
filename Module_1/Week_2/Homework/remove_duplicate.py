def function_helper(x, num_list):
    for num in num_list:
        # Your code here
        # Neu x == num thi return False
        if x == num:
            return False
    return True


def remove_duplicate(num_list):
    res = []
    for num in num_list:
        if function_helper(num, res):
            res.append(num)

    return res


if __name__ == '__main__':
    assert remove_duplicate([10, 10, 9, 7, 7]) == [10, 9, 7]
    print(remove_duplicate([9, 9, 8, 1, 1]))  # [9, 8, 1]
