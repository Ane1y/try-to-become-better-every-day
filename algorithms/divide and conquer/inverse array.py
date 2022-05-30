#Первая строка содержит число 1≤n≤10^5, вторая — массив A[1…n], содержащий натуральные числа, не превосходящие
# 109 10^9 109. Необходимо посчитать число пар индексов 1≤i<j≤n, для которых A[i]>A[j] . (Такая пара элементов
# называется инверсией массива. Количество инверсий в массиве является в некотором смысле его мерой неупорядоченности: например, в упорядоченном по неубыванию массиве
# инверсий нет вообще, а в массиве, упорядоченном по убыванию, инверсию образуют каждые два элемента.)
#занимаюсь дублированием кода

def countInversions(array):
    alen = len(array)
    if alen == 1:
        return array, 0
    mid = int(alen / 2)
    left, inversions1 = countInversions(array[:mid])
    right, inversions2 = countInversions(array[mid:])
    sorted_array = []
    i, j = 0, 0
    inversions = 0
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            sorted_array.append(right[j])
            inversions += mid - i
            j += 1
        else:
            sorted_array.append(left[i])
            i += 1
    while i < len(left):
        sorted_array.append(left[i])
        i += 1
    while j < len(right):
        sorted_array.append(right[j])
        j += 1
    return sorted_array, inversions1 + inversions2 + inversions

n = int(input())
array = list(map(int, input().split()))
_, inversions = countInversions(array)
print(inversions)