import numpy as np

def editDistBU(a, b):
    n = len(a) + 1
    m = len(b) + 1
    d = np.zeros(shape=(n, m), dtype=int)
    for i in range(n):
        d[i, 0] = i
    for j in range(m):
        d[0, j] = j
    for i in range(1, n):
        for j in range(1, m):
            c = 0 if a[i - 1] == b[j - 1] else 1
            d[i, j] = min(d[i - 1, j] + 1, d[i, j - 1] + 1, d[i - 1, j - 1] + c)
        print(d)
    return d[n-1, m-1]
def main():
    a = input()
    b = input()
    print(editDistBU(a, b))

if __name__ == '__main__':
    main()