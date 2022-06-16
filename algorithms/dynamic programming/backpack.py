import numpy as np


def fill_backpack(volume, weights, n):
    d = np.zeros(shape=(n + 1, volume + 1), dtype=int)
    for i in range(n + 1):
        for w in range(volume + 1):
            if i == 0 or w == 0:
                d[i][w] = 0
            elif weights[i - 1] <= w:
                d[i][w] = max(weights[i - 1] + d[i - 1][w - weights[i - 1]],
                              d[i - 1][w])
            else:
                d[i][w] = d[i - 1][w]
    print(d)
    return d[n][volume]

volume, n = map(int, input().split())
weights = list(map(int, input().split()))
print(fill_backpack(volume, weights, n))