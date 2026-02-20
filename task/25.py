# from fnmatch import fnmatch
# for i in range(317, 10**10+1, 4173):
#     if fnmatch(str(i), '1?7246*1'):
#         print(i, int(i//4173))


# --------------------------------------------------------------------------------------------------------------------


# 27851
# for i in range(110203, 110246):
#     d=[]
#     for g in range(2,i):
#         if i%g==0:
#             d.append(g)
#     if len(d)==4:
#         print(sorted(d))


# --------------------------------------------------------------------------------------------------------------------


# max_count = (0, 0)
# for i in range(84052, 84131):
#     mass = []
#     for g in range(1, i+1):
#         if i%g == 0:
#             mass.append(g)
#     if len(mass) > max_count[0]:
#         max_count = (len(mass), i)
# print(max_count)


# --------------------------------------------------------------------------------------------------------------------


# for i in range(110203, 110246):
#     d=[]
#     for g in range(2,int(i**0.5)+1):
#         if i%g==0 and g%2==0:
#             d.append(g)
#     if len(d)==4:
#         print(sorted(d))


# --------------------------------------------------------------------------------------------------------------------


# # Unnamed function
# def f(x):
#     delitel = set()
#     for d in range(2, int(x**0.5)+1):
#         if len(delitel) > 2:
#             break
#         if x % d == 0:
#             if d % 2 == 0:
#                 delitel.add(d)
#             if (x/d) % 2 == 0:
#                 delitel.add(x//d)
#     return sorted(delitel)
# # print(f(16))

# for i in range(101000000, 102000001, 2):
#     if len(f(i)) == 2:
#         print(i)


# --------------------------------------------------------------------------------------------------------------------


# 40741
# def maxDel(x):
#     delit = set()
#     for d in range(2, int(x**0.5)+1):
#         if x % d == 0:
#             delit.add(d)
#             delit.add(x//d)
#     if len(delit) >= 2:
#         max_int = max(delit)
#         delit.remove(max(delit))
#         max_int_2 = max(delit)
#         summ = max_int + max_int_2
#         if summ < 10000:
#             return (summ)
#     return 0
# count = 0
# for i in range(10000000, 10001000):
#     v = maxDel(i)
#     if v != 0:
#         print(v)
#         count += 1
#     if count == 5:
#         break


# --------------------------------------------------------------------------------------------------------------------


# 37130
# count = 0
# for x in range(600000, 601001):
#     for d in range(8, (x**0.5)+1):
#         if x % d == 0 and d % 10 == 7:
#             print(x, d)
#             count += 1
#         if count == 5:
#             break