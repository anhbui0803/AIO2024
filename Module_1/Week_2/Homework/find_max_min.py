def find_min(num_list):
    # Your code here
    return min(num_list)


def find_max(num_list):
    # Your code here
    return max(num_list)


if __name__ == '__main__':
    assert find_min([1, 22, 93, -100]) == -100
    print(find_min([1, 2, 3, -1]))

    assert find_max([1001, 9, 100, 0]) == 1001
    print(find_max([1, 9, 9, 0]))
