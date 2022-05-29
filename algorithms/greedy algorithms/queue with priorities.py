# Первая строка входа содержит число операций 1≤n≤10^5. Каждая из последующих n строк задают операцию одного из следующих двух типов:
#
#     Insert  x, где 0≤x≤10^9 — целое число;
#     ExtractMaxx.
#
# Первая операция добавляет число x в очередь с приоритетами, вторая — извлекает максимальное число и выводит его.
# Система кстати не приняла решение, потому что оно неоптимальное :((
class QueueWithPriorities():
    def __init__(self):
        self.tree = []
        self.size = 0

    def insert(self, element):
        i = self.size
        self.tree.append(element)
        self.size = self.size + 1
        while self.tree[i] > self.tree[(i - 1) // 2]: # i  0 — мы в корне
            self.tree[i], self.tree[(i - 1) // 2] = self.tree[(i - 1) // 2], self.tree[i]
            i = (i - 1) // 2
            if i == 0:
                break
        print(self.tree)

    def getMax(self):
        return self.tree[0]

    def extractMax(self):
        # self.tree[0] = self.tree[self.size - 1]
        # self.tree.pop()
        # self.size -= 1
        # i = 0
        # while 2 * i + 1 < self.size:
        #     left = self.getLeftNode(i)
        #     right = self.getRightNode(i)
        #     j = left
        #     if right > self.size and self.tree[right] > self.tree[left]:
        #         j = right
        #     if self.tree[i] >= self.tree[j]:
        #         break
        #     self.tree[i], self.tree[j] = self.tree[j], self.tree[i]
        #     i = j
        self.tree[0] = self.tree[self.size - 1]
        self.tree.pop(self.size - 1)
        self.size -= 1
        cur_index = 0
        right_node = self.getRightNode(cur_index)
        left_node = self.getLeftNode(cur_index)
        while not(left_node is None):
            max_index = 0
            if not(right_node is None) and self.tree[right_node] >= self.tree[left_node]:
                max_index = right_node
            elif self.tree[left_node] > self.tree[cur_index]:
                max_index = left_node
            else:
                break
            self.tree[cur_index], self.tree[max_index] = self.tree[max_index], self.tree[cur_index]
            cur_index = max_index
            right_node = self.getRightNode(cur_index)
            left_node = self.getLeftNode(cur_index)

        print(self.tree)

    def getLeftNode(self, parent_index):
        left_node = parent_index * 2 + 1
        if left_node < self.size and left_node > 0:
            return left_node
        return None

    def getRightNode(self, parent_index):
        right_node = parent_index * 2 + 2
        if right_node < self.size and right_node > 0:
            return right_node
        return None

    def getParent(self, child_index):
        if child_index > 0:
            return (child_index - 1)// 2

import sys
n = int(input())
queue = QueueWithPriorities()
for i in range(n):
    cmd = sys.stdin.readline().split(' ')
    if cmd[0] == 'Insert':
        queue.insert(int(cmd[1]))
    else:
        print(queue.getMax())
        queue.extractMax()