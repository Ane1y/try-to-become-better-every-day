# implementation of how to pack backpack by lecturer
# and look how is his solution more elegant
import heapq
def fractional_knapsack_heap(capacity, values_and_weights):
    order = [(-v / w, w) for v, w in values_and_weights]
    heapq.heapify(order)
    acc = 0
    while order and capacity:
        v_per_w, w = heapq.heappop(order)
        can_take = min(w, capacity)
        acc -= v_per_w * can_take
        capacity -= can_take

    return acc
def fractional_knapsack(capacity, values_and_weights):
    order = [(v / w, w) for v, w in values_and_weights]
    order.sort(reverse=True)

    acc = 0
    for v_per_w, w in order:
        if w < capacity:
            acc += v_per_w * w
            capacity -= w
        else:
            acc += v_per_w * capacity
            break
    return acc
# можно читать поток ввода
import sys
def main():
    reader = (map(int, line.split()) for line in sys.stdin)
    n, capacity = next(reader)
    values_and_weights = list(reader)
    assert len(values_and_weights) == n
    opt_value = fractional_knapsack(capacity, values_and_weights)
    print("{:.3f}".format(opt_value))

def test():
    assert  fractional_knapsack_heap(0, [(60, 20)]) == 0.0
    assert fractional_knapsack_heap(25, [(60, 20)]) == 60.0
    assert fractional_knapsack_heap(25, [(60, 20), (0, 100)]) == 60.0
    assert fractional_knapsack_heap(25, [(60, 20), (50, 50)]) == 60.0 + 5.0

    from random import randint
    from timing import timed

    for attempt in range(100):
        n = randint(1, 1000)
        capacity = randint(0, 2 * 10 ** 6)
        values_and_weights = []
        for i in range(n):
            values_and_weights.append((randint(0, 2 * 10 ** 6), randint(1, 2 * 10 ** 6)))
        t = timed(fractional_knapsack_heap, capacity, values_and_weights)
        print('hey')
        assert t < 5
if __name__ == '__main__':
    test()