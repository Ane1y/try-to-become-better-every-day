from math import floor

def read_arrays():
    a = list(map(int, input().split()))
    assert a[0] == len(a) - 1
    return a[1:]
def binary_search(a, k):
    l = 0
    r = len(a) - 1
    while l <= r:
        m = floor((l + r) / 2)
        if a[m] == k:
            return m + 1
        elif a[m] > k:
            r = m - 1
        else:
            l = m + 1
    return -1
a = read_arrays()
b = read_arrays()
answer = []
for i in b:
    answer.append(binary_search(a, i))
print(*answer, sep = ' ')
