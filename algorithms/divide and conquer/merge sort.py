# #Сортировки
# Сортировка слияением
def insertion_sort(a):
    for i in range(2, len(a)):
        j = i
        while j > 1 and a[j] < a[j - 1]:
            a[j], a[j - 1] = a[j - 1], a[j]
            print(a)
            j -= 1
    return a

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

a = [1, 5, 9, 4, 7, 6, 2, 1]

print(merge_sort(a))