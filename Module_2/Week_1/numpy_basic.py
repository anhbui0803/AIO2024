import numpy as np
from icecream import ic


# Cau 1 -> A
print("------------------- Cau 1 ---------------------")
arr = np.arange(0, 10, 1)
ic(arr)

# Cau 2 -> D
print("------------------- Cau 2 ---------------------")
arr1 = np.ones((3, 3)) > 0
arr2 = np.ones((3, 3), dtype=bool)
arr3 = np.full((3, 3), fill_value=True, dtype=bool)
ic(arr1)
ic(arr2)
ic(arr3)

# Cau 3 -> A
print("------------------- Cau 3 ---------------------")
arr = np.arange(0, 10)
ic(arr[arr % 2 == 1])

# Cau 4 -> B
print("------------------- Cau 4 ---------------------")
arr = np.arange(0, 10)
arr[arr % 2 == 1] = -1
ic(arr)

# Cau 5 -> B
print("------------------- Cau 5 ---------------------")
arr = np.arange(10)
arr_2d = arr.reshape(2, -1)
ic(arr_2d)

# Cau 6 -> A
print("------------------- Cau 6 ---------------------")
arr1 = np.arange(10).reshape(2, -1)
arr2 = np.repeat(1, 10).reshape(2, -1)
c = np.concatenate([arr1, arr2], axis=0)
ic(c)

# Cau 7 -> C
print("------------------- Cau 7 ---------------------")
arr1 = np.arange(10).reshape(2, -1)
arr2 = np.repeat(1, 10).reshape(2, -1)
c = np.concatenate([arr1, arr2], axis=1)
ic(c)

# Cau 8 -> A
print("------------------- Cau 8 ---------------------")
arr = np.array([1, 2, 3])
ic(np.repeat(arr, 3))  # Repeat each element of array
ic(np.tile(arr, 3))  # Repeat array

# Cau 9 -> C
print("------------------- Cau 9 ---------------------")
arr = np.array([2, 6, 1, 9, 10, 3, 27])
index = np.nonzero((arr >= 5) & (arr <= 10))
ic(arr[index])

# Cau 10 -> D
print("------------------- Cau 10 ---------------------")
def maxz(x, y):
    if x >= y:
        return x
    return y


a = np.array([5, 7, 9, 8, 6, 4, 5])
b = np.array([6, 3, 4, 8, 9, 7, 1])
pair_max = np.vectorize(pyfunc=maxz, otypes=[float])
ic(pair_max(a, b))

# Cau 11 -> A
print("------------------- Cau 11 ---------------------")
a = np.array([5, 7, 9, 8, 6, 4, 5])
b = np.array([6, 3, 4, 8, 9, 7, 1])
ic(np.where(a < b, b, a))  # Intuition: Output max by compare each pair of elements
