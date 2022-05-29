import random

def test(gcd, n_iter=100):
    for i in range(n_iter):
        c = random.randint(0, 1024)
        a = c * random.randint(0, 128)
        b = c * random.randint(0, 128)
        assert gcd(a, a) == gcd(a, 0) == a
        assert gcd(b, b) == gcd(b, 0) == b
        assert gcd(a, 1) == gcd(b, 1) == 1
        d = gcd(a, b)
        if d != 0:
            assert a % d == b % d == 0

def gcd1(a, b):
    assert a >= 0 and b >= 0
    for d in reversed(range(max(a, b) + 1)):
        if d == 0 or a % d == b % d == 0:
            return d

print(gcd1(8, 3))
print(gcd1(0, 0))
test(gcd1)

def gcd2(a, b):
    while a and b:
        if a >= b:
            a %= b
        else:
            b %= a
    return max(a, b)

print(gcd2(8, 3))
print(gcd2(100000000000, 1000000000000000000))
test(gcd2)

def gcd3(a, b):
    assert a >= 0 or b >= 0
    if a == 0 or b == 0:
        return max(a, b)
    elif(a >= b):
        return gcd3(a % b, b)
    else:
        return gcd3(a, b % a)

test(gcd3)

def gcd4(a, b):
    assert a >= 0 or b >= 0
    if a == 0 or b == 0:
        return max(a, b)
    return gcd4(b % a, a)
test(gcd4)

from timing import compare

compare([gcd1, gcd2, gcd3, gcd4], [(2003879, 4054159) for _ in range(100)])