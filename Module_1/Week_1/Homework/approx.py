def factorial(x):
    res = 1
    for j in range(2, x + 1):
        res *= j
    return res


def approx_sin(x, n):
    res = 0.0
    for i in range(n + 1):
        res += ((-1) ** i) * (x ** (2 * i + 1)) / factorial(2 * i + 1)
    return res


def approx_cos(x, n):
    res = 0.0
    for i in range(n + 1):
        res += ((-1) ** i) * (x ** (2 * i)) / factorial(2 * i)
    return res


def approx_sinh(x, n):
    res = 0.0
    for i in range(n + 1):
        res += (x ** (2 * i + 1)) / factorial(2 * i + 1)
    return res


def approx_cosh(x, n):
    res = 0.0
    for i in range(n + 1):
        res += (x ** (2 * i)) / factorial(2 * i)
    return res


if __name__ == "__main__":
    # n > 0 and x must be radian scale
    assert round(approx_cos(x=1, n=10), 2) == 0.54
    print(round(approx_cos(x=3.14, n=10), 2))  # -1.0

    assert round(approx_sin(x=1, n=10), 4) == 0.8415
    print(round(approx_sin(x=3.14, n=10), 4))  # 0.0016

    assert round(approx_sinh(x=1, n=10), 2) == 1.18
    print(round(approx_sinh(x=3.14, n=10), 2))  # 11.53

    assert round(approx_cosh(x=1, n=10), 2) == 1.54
    print(round(approx_cosh(x=3.14, n=10), 2))  # 11.57
