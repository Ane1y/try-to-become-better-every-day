import bisect


def lisBottomUp2(a):
    n = len(a)
    d = [1] * n
    prev = [-1] * n
    for i in range(n):
        for j in range(i):
            if a[i] % a[j] == 0 and d[j] + 1 > d[i]:
                d[i] = d[j] + 1
                prev[i] = j
    ans = 0
    print(d)
    for i in d:
        ans = max(ans, i)

    return ans


def lis2(arr):
    if len(arr) == 0:
        return 0
    l = [arr[0]]
    for element in arr[1:]:
        pos = bisect.bisect(l, element)
        if pos == len(l):
            if element > l[pos - 1]:
                l.append(element)
        else:
            if element != l[pos - 1]:
                l[pos] = element
    return len(l)

def main():
    # a = [3, 6, 12, 7, 9, 24, 18, 3, 9, 24]
    # b = [5, 3, 4, 4, 2]
    _ = int(input())
    array = list(map(int, input().split()))
    print(lisBottomUp2(array))
    # print(lis2(b))
if __name__ == "__main__":
    main()