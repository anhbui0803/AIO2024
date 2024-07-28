import numpy as np
from icecream import ic


def compute_mean(x: list[int]):
    size = len(x)
    mean = 0.0

    for num in x:
        mean += num

    return mean / size


def compute_median(x: list[int]):
    size = len(x)
    x = np.sort(x)

    if size % 2 == 0:
        return (x[size // 2 - 1] + x[size // 2]) / 2

    return x[(size + 1) // 2 - 1]


def compute_std(x: list[int]):
    size = len(x)
    mean = compute_mean(x)
    variance = 0.0

    for num in x:
        variance += (num - mean) ** 2

    variance = variance / size

    return np.sqrt(variance)


def compute_correlation_coefficient(x: np.ndarray, y: np.ndarray):
    N = len(x)
    numerator = N * (x @ y) - np.sum(x) * np.sum(y)
    denominator = (np.sqrt(N * np.sum(x ** 2) - np.sum(x) ** 2)
                   * np.sqrt(N * np.sum(y ** 2) - np.sum(y) ** 2))
    return numerator / denominator


def compute_mean_numpy(x: np.ndarray):
    if not isinstance(x, np.ndarray):
        x = np.array(x)

    return np.mean(x)


def compute_median_numpy(x: np.ndarray):
    if not isinstance(x, np.ndarray):
        x = np.array(x)

    return np.median(x)


def compute_std_numpy(x: np.ndarray):
    if not isinstance(x, np.ndarray):
        x = np.array(x)

    return np.std(x)


def compute_correlation_coefficient_numpy(x: np.ndarray, y: np.ndarray):
    if not isinstance(x, np.ndarray):
        x = np.array(x)

    if not isinstance(y, np.ndarray):
        y = np.array(y)

    return np.corrcoef(x, y)


if __name__ == '__main__':
    # Cau 1 -> A
    print("------------------- Cau 1 ---------------------")
    X1 = [2, 0, 2, 2, 7, 4, -2, 5, -1, -1]
    ic("Mean:", compute_mean(X1))
    ic("Mean (numpy):", compute_mean_numpy(X1))

    # Cau 2 -> B
    print("------------------- Cau 2 ---------------------")
    X2 = [1, 5, 4, 4, 9, 13]
    ic("Median:", compute_median(X2))
    ic("Median (numpy):", compute_median_numpy(X2))

    # Cau 3 -> C
    print("------------------- Cau 3 ---------------------")
    X3 = [171, 176, 155, 167, 169, 182]
    ic("STD:", compute_std(X3))
    ic("STD (numpy):", compute_std_numpy(X3))

    # Cau 4 -> D
    print("------------------- Cau 4 ---------------------")
    X = np.array([-2, -5, -11, 6, 4, 15, 9])
    Y = np.array([4, 25, 121, 36, 16, 225, 81])
    ic("Correlation:", np.round(compute_correlation_coefficient(X, Y), 2))
    ic("Correlation (numpy):", compute_correlation_coefficient_numpy(X, Y))
