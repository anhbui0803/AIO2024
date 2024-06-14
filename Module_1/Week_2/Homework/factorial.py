def factorial(x):
    res = 1
    while (x > 1):
        res *= x
        x -= 1

    return res


if __name__ == '__main__':
    assert factorial(8) == 40320
    print(factorial(4))  # 24
