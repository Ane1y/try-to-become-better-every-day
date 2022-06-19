def broken_calculator(n):
    a = [0] * (n + 1)
    b = [n]
    for i in range(2, n + 1):
        v_min = a[i - 1] + 1
        if i % 2 == 0:
            v_min = min(v_min, a[int(i / 2)] + 1)
        if i % 3 == 0:
            v_min = min(v_min, a[int(i / 3)] + 1)
        a[i] = v_min
    # print(a)
    i = n
    while i > 1:
        if a[i] == a[i - 1] + 1:
            i -= 1
        elif i % 2 == 0 and a[i] == a[int(i / 2)] + 1:
            i = int(i / 2)
        else:
            i = int(i / 3)
        b.append(i)
    b.reverse()
    print(*b, sep=' ')


n = int(input())
broken_calculator(n)