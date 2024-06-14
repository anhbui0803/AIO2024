def avg(num_list=[0, 1, 2]):
    avg = 0
    for num in num_list:
        avg += num

    return avg / len(num_list)


if __name__ == '__main__':
    assert avg([4, 6, 8]) == 6
    print(avg())  # 1.0
