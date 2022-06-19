import numpy as np

def matrixMultTD(m):
    n = len(m)
    d = np.zeros(shape=(n, n))#, fill_value=-1.0)
    for i in range(1, n):
        d[i, i] = 0
        # d[i, 0] = 0
        # d[0, i] = 0
    for s in range(2, n):
        for i in range(1, n - s + 1):
            j = i + s - 1
            d[i][j] = np.inf
            for k in range(i, j):
                d[i, j] = min(d[i, j], d[i, k] + d[k + 1, j] + m[i - 1] * m[k] * m[j])
                print(m[i - 1] * m[k] * m[j])
        print(d)
    return d[1, n - 1]


print(matrixMultTD([50,20,1,10,100]))