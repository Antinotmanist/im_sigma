# def rec(lst, level=1):
#     print(*lst, 'level =', level)
#     for el in lst:
#         if isinstance(el, list):
#             rec(el, level + 1)


# rec([1, 2, [3, [4, [1, [[[[[[3]]]]]]]]], [3, 4, [3, [[[[2]]]]]]])

# fa = lambda x: x if x == 1 else fa(x - 1) * x
a = 'Python TopF'
print(a.lower())