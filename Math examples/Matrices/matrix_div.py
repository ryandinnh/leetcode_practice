import numpy as np

A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

#Inverting matrix B
B_inv = np.linalg.inv(B)

#Multiplying A by the inverse of B
result = np.dot(A, B_inv)
print(result)
