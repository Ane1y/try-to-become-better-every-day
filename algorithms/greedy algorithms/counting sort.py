#not greedy algorithm
from itertools import repeat


def counting_sort(array):
    counter = {}
    for i in array:
        if i in counter:
            counter[i] += 1
        else:
            counter[i] = 1
    sorted_list = []
    for key in sorted(counter):
        sorted_list.extend(repeat(key, counter[key]))
    return sorted_list

n = int(input())
array = list(map(int, input().split()))
print(array)
print(*counting_sort(array), sep = ' ')
#на форуме решений такие красивые решения...

# 5
# 2 3 9 2 9