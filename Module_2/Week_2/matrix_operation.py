import numpy as np
from icecream import ic


# 1.1. Length of vector
def compute_vector_length(vector):
    vector_norm2 = np.linalg.norm(vector, ord=2)
    return vector_norm2

# 1.2. Dot product
def compute_dot_product(vector1, vector2):
    result1 = np.dot(vector1, vector2)
    result2 = vector1 @ vector2
    result3 = vector1.dot(vector2)
    return result1, result2, result3


# 1.3. Multiplying a vector by a matrix
def matrix_multi_vector(matrix, vector):
    result1 = np.matmul(matrix, vector)
    result2 = matrix @ vector
    result3 = matrix.dot(vector)
    return result1, result2, result3


# 1.4. Multiplying a matrix by a matrix
def matrix_multi_matrix(matrix1, matrix2):
    result1 = np.matmul(matrix1, matrix2)
    result2 = matrix1 @ matrix2
    result3 = matrix1.dot(matrix2)
    return result1, result2, result3


# 1.5. Matrix inverse (include markdown)
def inverse_matrix(matrix):
    result = np.linalg.inv(matrix)
    return result


if __name__ == '__main__':
    # Cau 1 -> D
    print("------------------- Cau 1 ---------------------")
    vector = np.array([-2, 4, 9, 21])
    ic(round(compute_vector_length(vector), 2))

    # Cau 2 -> B
    print("------------------- Cau 2 ---------------------")
    v1 = np.array([0, 1, -1, 2])
    v2 = np.array([2, 5, 1, 0])
    res1, res2, res3 = compute_dot_product(v1, v2)
    ic(res1, res2, res3)

    # Cau 3 -> A
    print("------------------- Cau 3 ---------------------")
    m = np.array([[1, 2],
                  [3, 4]])
    v = np.array([1, 2])
    ic(m.dot(v))
    ic(matrix_multi_vector(m, v))

    # Cau 4 -> B
    print("------------------- Cau 4 ---------------------")
    m = np.array([[-1, 2],
                  [3, -4]])
    v = np.array([1, 2])
    ic(m @ v)
    ic(matrix_multi_vector(m, v))

    # Cau 5 -> A
    print("------------------- Cau 5 ---------------------")
    m = np.array([[-1, 1, 1],
                  [0, -4, 9]])
    v = np.array([0, 2, 1])
    ic(matrix_multi_vector(m, v))

    # Cau 6 -> C
    print("------------------- Cau 6 ---------------------")
    m1 = np.array(([[0, 1, 2],
                    [2, -3, 1]]))
    m2 = np.array([[1, -3],
                   [6, 1],
                   [0, -1]])
    ic(matrix_multi_matrix(m1, m2))

    # Cau 7 -> A
    print("------------------- Cau 7 ---------------------")
    m1 = np.eye(3)
    m2 = np.array([[1, 1, 1],
                   [2, 2, 2],
                   [3, 3, 3]])
    ic(m1 @ m2)
    ic(matrix_multi_matrix(m1, m2))

    # Cau 8 -> D
    print("------------------- Cau 8 ---------------------")
    m1 = np.eye(2)
    m1 = np.reshape(m1, newshape=(-1, 4))[0]  # Flatten (1, 4)
    m2 = np.array([[1, 1, 1, 1],
                   [2, 2, 2, 2],
                   [3, 3, 3, 3],
                   [4, 4, 4, 4]])
    ic(m1)
    ic(m1 @ m2)
    ic(matrix_multi_matrix(m1, m2))

    # Cau 9 -> B
    print("------------------- Cau 9 ---------------------")
    m1 = np.array([[1, 2],
                   [3, 4]])
    m1 = np.reshape(m1, newshape=(-1, 4), order="F")  # Fortran-like reshape
    m2 = np.array([[1, 1, 1, 1],
                   [2, 2, 2, 2],
                   [3, 3, 3, 3],
                   [4, 4, 4, 4]])
    ic(m1)
    ic(m1 @ m2)
    ic(matrix_multi_matrix(m1, m2))

    # Cau 10 -> A
    print("------------------- Cau 10 ---------------------")
    m = np.array([[-2, 6],
                 [8, -4]])
    ic(inverse_matrix(m))
