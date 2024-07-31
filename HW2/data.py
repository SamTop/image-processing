files = [
    '145-11',
    '146-11',
    '147-11',
    '148-11',
    '149-11',
    '150-11',
    '151-11',
    '152-11',
]

import numpy as np

# Example 2D array
array = np.array([[1, 2, 3], [4, 5, 6]])

# Append the array to itself row-wise
appended_array_row = np.concatenate((array, array), axis=0)

print("Original Array:")
print(array)
print("Appended Array (Row-wise):")
print(appended_array_row)

# Append the array to itself column-wise
appended_array_col = np.concatenate((array, array), axis=1)

print("Original Array:")
print(array)
print("Appended Array (Column-wise):")
print(appended_array_col)
