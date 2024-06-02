import math


def is_number(x):
    try:
        float(x)
    except ValueError:
        return False
    return True


def sigmoid(x):
    return 1 / (1 + math.e ** (-x))


def relu(x):
    return max(x, 0)


def elu(x, alpha=0.01):
    return x if x > 0 \
        else alpha * (math.e ** x - 1)


def calc_act_func(x, act_func_name):
    ACT_FUNC = {
        "sigmoid": sigmoid,
        "relu": relu,
        "elu": elu
    }

    if not is_number(x):
        print("x must be a number")
        return

    if act_func_name not in ACT_FUNC.keys():
        print(f"{act_func_name} is not supported")
        return

    x = float(x)
    result = ACT_FUNC[act_func_name](x)
    print(f"{act_func_name}: f({x}) = {result}")
    return result


if __name__ == "__main__":
    assert is_number(3) == 1.0
    assert is_number("-2a") == 0.0
    print(is_number(1))  # True
    print(is_number("n"))  # False

    assert round(sigmoid(3), 2) == 0.95
    print(round(sigmoid(2), 2))  # 0.88

    assert round(elu(1)) == 1
    print(round(elu(-1), 2))  # -0.01

    assert calc_act_func(x=1, act_func_name="relu") == 1
    print(round(calc_act_func(x=3, act_func_name="sigmoid"), 2))  # 0.95
