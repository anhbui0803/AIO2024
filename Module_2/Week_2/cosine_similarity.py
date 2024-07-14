import numpy as np
from icecream import ic


# 3.1. Cosine similarity (include markdown)
def compute_cosine(vector1, vector2):
    result = np.dot(vector1, vector2) / \
        (np.linalg.norm(vector1, ord=2) * np.linalg.norm(vector2, ord=2))
    return result


if __name__ == '__main__':
    # Cau 12 -> C
    print("------------------- Cau 12 ---------------------")
    m1 = np.array([1, 2, 3, 4])
    m2 = np.array([1, 0, 3, 0])
    ic(round(compute_cosine(m1, m2), 3))
