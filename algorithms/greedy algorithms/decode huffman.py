# По данной непустой строке s длины не более 10^4, состоящей из строчных букв латинского алфавита,
# постройте оптимальный беспрефиксный код. В первой строке выведите количество различных букв k, встречающихся в строке,
# и размер получившейся закодированной строки. В следующих k строках запишите коды букв в формате "letter: code".
# В последней строке выведите закодированную строку.
# class Node():
#     def __init__(self, root, symbol):
#         self.root = root
#         self.symbol = symbol
#         self.left = None
#         self.right = None
#
# def build_tree():
#     tree = Node()
#     dict = {}
#     if len(res_sorted) == 1:
#         return (res_sorted[0][0], 0)
#     tree.append([0, res_sorted[0][0]])
#     tree.append([1, res_sorted[1][1]])
#     tree.append([2, res_sorted[0][1] + res_sorted[1][1]])
#     for i in range(2, len(res_sorted)):
#         tree.append([i + 1, tree[i - 2][1] + res_sorted[i][1]])
#         tree.append()
#     print(dict)
#     return tree
# s = input()
# print(s)
# unique_symbols = 0
# encoded_string_size = 0
# res = {}
# for symbol in s:
#     res[symbol] = res.get(symbol, 0) + 1
#
# res_sorted = sorted(res.items(), key=lambda x: x[1])
# print(res_sorted)
# print(build_tree())

# декодировать строку по хаффману
# закодировать у меня не получилось, а вот декодировать пожалуйста!
unique_symbols, size_of_string = map(int, input().split())
dict = {}
for i in range(unique_symbols):
    str = input().split(': ')
    dict[str[1]]= str[0]
str = input()
decoded_str = ''
code = ''
for i in str:
    code += i
    if code in dict:
        decoded_str += dict[code]
        code = ''
print(decoded_str)
# 4 14
# a: 0
# b: 10
# c: 110
# d: 111
