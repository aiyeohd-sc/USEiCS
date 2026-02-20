# 77 ans = 4
# Для приведенного фрагмента таблицы истинности выражения 
# F=(x∨(y∧¬z))∧¬wF=(x∨(y∧¬z))∧¬w определите количество возможных последовательностей
# имён столбцов.
# ? ? ? ?   F
# 1 0 0 0   1
# 0 0 1 0   1
# 0 1 0 1   0

# В ответе укажите количество таких комбинаций.

# from itertools import *

# rows = [
#     ([1,0,0,0],1),
#     ([0,0,1,0],1),
#     ([0,1,0,1],0)
# ]

# def F(x, y, z, w):
#     return ((x or (y and not z)) and not w)

# count = 0
# for v in permutations("xyzw"):
#     flag = True
#     for vals, res in rows:
#         vars_dict = {var: val for var, val in zip(v, vals)}
#         x = vars_dict['x']
#         y = vars_dict['y']
#         z = vars_dict['z']
#         w = vars_dict['w']
#         if F(x, y, z, w) != res:
#             flag = False
#             break
#     if flag:
#         count += 1
# print(count)


# -----------------------------------------------------------------------------------

# 12911
# print("z y x F")
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             F = ((not z) and x or x and y)
#             print(z, y, x, F)


# -----------------------------------------------------------------------------------


# 332
# from itertools import *

# rows = [
#     ([1, 0, 1, 0], 1),
#     ([1, 1, 1, 0], 1),
#     ([0, 1, 0, 1], 0)
# ]

# def F(x, y, z, w):
#     return ((x or y and not z) and not w)

# count = 0
# for perm in permutations("xyzw"):
#     flag = True
#     for val, key in rows:
#         val_map = {vl: ky for vl, ky in zip(perm, val)}
#         x = val_map['x']
#         y = val_map['y']
#         z = val_map['z']
#         w = val_map['w']
#         if F(x, y, z, w) != key:
#             flag = False
#             break
#     if flag:
#         count += 1
# print(count)


# -----------------------------------------------------------------------------------


# from itertools import *

# rows = [
#     ([1, 0, 1, 1],0),
#     ([1, 0, 0, 0], 0),
#     ([1, 0, 1, 0], 0)
# ]

# def F(a, b, c, d):
#     return ((not(not a or b) or c) or not d)

# for perm in permutations("abcd"):
#     flag = True
#     for vals, exp in rows:
#         val_dict = {val: var for val, var in zip(perm, vals)}
#         print(zip(perm, vals))
#         a = val_dict["a"]
#         b = val_dict["b"]
#         c = val_dict["c"]
#         d = val_dict["d"]
#         if F(a, b, c, d) != exp:
#             flag = False
#             break
#     if flag:
#         print(perm)
