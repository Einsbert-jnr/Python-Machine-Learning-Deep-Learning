import numpy as np

a = np.array([[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]])
b = np.array([[1], [2], [3], [4]])

print(a.shape)
print(b.shape)

for i in range(3):
    for j in range(4):
        c[i][j] = a[i][j] + b[j]