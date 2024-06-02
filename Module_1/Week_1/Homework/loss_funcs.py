import random
import math


def calc_ae(y, y_hat):
    return abs(y - y_hat)


def calc_se(y, y_hat):
    return (y - y_hat) ** 2


def mae(num_samples, loss_name):
    loss = 0.0
    for i in range(num_samples):
        y_hat = random.uniform(0, 10)
        y = random.uniform(0, 10)
        loss += calc_ae(y, y_hat)
        loss /= num_samples
        print(f"loss name: {loss_name}, \
            sample: {i}, \
            pred: {y_hat}, \
            target: {y}, \
            loss: {loss}")


def mse(num_samples, loss_name):
    loss = 0.0
    for i in range(num_samples):
        y_hat = random.uniform(0, 10)
        y = random.uniform(0, 10)
        loss += calc_se(y, y_hat)
        loss /= num_samples
        print(f"loss name: {loss_name}, \
            sample: {i}, \
            pred: {y_hat}, \
            target: {y}, \
            loss: {loss}")


def rmse(num_samples, loss_name):
    loss = 0.0
    for i in range(num_samples):
        y_hat = random.uniform(0, 10)
        y = random.uniform(0, 10)
        loss += calc_se(y, y_hat)
        loss = math.sqrt(loss / num_samples)
        print(f"loss name: {loss_name}, \
            sample: {i}, \
            pred: {y_hat}, \
            target: {y}, \
            loss: {loss}")


def calc_loss():
    LOSS_NAME = {
        "mae": mae,
        "mse": mse,
        "rmse": rmse,
    }
    num_samples = input("Input number of samples (integer number): ")
    if num_samples.isnumeric():
        loss_name = input("Input loss name: ")
        num_samples = int(num_samples)
        LOSS_NAME[loss_name](num_samples, loss_name)
    else:
        print("number of samples must be an integer number")


if __name__ == "__main__":
    # calc_loss()

    assert calc_ae(y=1, y_hat=6) == 5
    print(calc_ae(y=2, y_hat=9))  # 7

    assert calc_se(y=4, y_hat=2) == 4
    print(calc_se(y=2, y_hat=1))  # 1
