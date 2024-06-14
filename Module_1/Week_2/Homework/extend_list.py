def extend_list(x, y):
    # Your code here
    # Su dung extend de noi y vao x
    x.extend(y)  # inplace
    return x


if __name__ == '__main__':
    num_list_1 = ["a", 2, 5]
    num_list_2 = [1, 1]
    num_list_3 = [0, 0]

    assert extend_list(num_list_1,
                       extend_list(num_list_2, num_list_3)) == ['a', 2, 5, 1, 1, 0, 0]

    num_list_1 = [1, 2]
    num_list_2 = [3, 4]
    num_list_3 = [0, 0]

    # [1, 2, 3, 4, 0, 0]
    print(extend_list(num_list_1, extend_list(num_list_2, num_list_3)))
