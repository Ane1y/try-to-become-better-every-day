#Первая строка содержит число 1≤n≤10^5, вторая — массив A[1…n], содержащий натуральные числа, не превосходящие
# 109 10^9 109. Необходимо посчитать число пар индексов 1≤i<j≤n, для которых A[i]>A[j] . (Такая пара элементов
# называется инверсией массива. Количество инверсий в массиве является в некотором смысле его мерой неупорядоченности: например, в упорядоченном по неубыванию массиве
# инверсий нет вообще, а в массиве, упорядоченном по убыванию, инверсию образуют каждые два элемента.)
#занимаюсь дублированием кода
def merge(a, b):
    result = []
    ai, bi = 0, 0
    while ai < len(a) and bi < len(b):
        if a[ai] < b[bi]:
            result.append(a[ai])
            ai += 1
        else:
            result.append(b[bi])
            bi += 1
    while ai < len(a):
        result.append(a[ai])
        ai += 1
    while bi < len(b):
        result.append(b[bi])
        bi += 1
    return result

def merge_sort(a):
    if len(a) < 2:
        return a
    else:
        m = int(len(a) / 2)
        left = merge_sort(a[:m])
        right = merge_sort(a[m:])
        return merge(left, right)
n = int(input())
array = list(map(int, input().split()))
print(inversion_array(array))