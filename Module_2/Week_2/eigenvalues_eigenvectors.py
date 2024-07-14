import numpy as np
from icecream import ic


# 2.1. Eigenvector and eigenvalue (include markdown)
def compute_eigenvectors_eigenvalues(matrix):
    eigenvalues1, eigenvectors1 = np.linalg.eig(matrix)
    eigenvalues2, eigenvectors2 = np.linalg.eigh(matrix)  # Hermitian
    return eigenvalues1, eigenvectors1, eigenvalues2, eigenvectors2


if __name__ == '__main__':
    # Cau 11 -> A
    print("------------------- Cau 11 ---------------------")
    m = np.array([[0.9, 0.2], [0.1, 0.8]])
    eigenvalues1, eigenvectors1, eigenvalues2, eigenvectors2 = compute_eigenvectors_eigenvalues(m)
    ic(eigenvalues1)
    ic(eigenvectors1)

    ic(eigenvalues2)  # Hermitian
    ic(eigenvectors2)  # Hermitian
