# По данному числу 1≤n≤10^9 найдите максимальное число k, для которого n можно представить как сумму k различных натуральных слагаемых.
# Выведите в первой строке число k, во второй — k слагаемых.

def sum_of_natural_numbers(n):
    sum = 0
    i = 1
    k = 0
    terms = []
    while n > sum:
        sum += i
        terms.append(i)
        i += 1
        k += 1
        if sum > n:
            k -= 1
            terms.remove(sum - n)
            return k, terms
    return k, terms

n = int(input())
k, terms = sum_of_natural_numbers(n)
print(k)
print(*terms, sep=" ")
