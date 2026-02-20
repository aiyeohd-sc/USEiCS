# 10473
# alph = "1234"
# count = 0
# for s1 in alph:
#     for s2 in alph:
#         for s3 in alph:
#             for s4 in alph:
#                 for s5 in alph:
#                     pswd = s1 + s2 + s3 + s4 + s5
#                     if pswd.count("1") == 2:
#                         count += 1
# print(count)


# --------------------------------------------------------------------------------------------------------------------


# 58235
# alph = '0123'
# count = 0
# for s1 in '123':
#     for s2 in alph:
#         for s3 in alph:
#             pswd = s1 + s2 + s3
#             if (int(s1)+ int(s3)) > int(s2):
#                 count += 1
# print(count)


# --------------------------------------------------------------------------------------------------------------------


# 58237
# alph = '0123456'
# count = 0
# for s1 in '123456':
#     for s2 in alph:
#         for s3 in alph:
#             for s4 in alph:
#                 pswd = s1 + s2 + s3 + s4
#                 if int(s1) > int(s2) and int(s2) > int(s3) and int(s3) > int(s4):
#                     count += 1
# print(count)


# --------------------------------------------------------------------------------------------------------------------


# 59713
# alph = 'ПЯТНИЦА'
# count = 0
# for s1 in alph:
#     if s1 == 'Н':
#         continue
#     for s2 in alph:
#         for s3 in alph:
#             for s4 in alph:
#                 for s5 in alph:
#                     psw = s1 + s2 + s3 + s4 + s5
#                     if psw.count('Я') == 1:
#                         count += 1
# print(count)


# --------------------------------------------------------------------------------------------------------------------


# 59713
# count = 0
# mn = set()
# for n in range(8**4, 8**5):
#     n_o = oct(n)[2:]
#     # print(n_o)
#     if n_o.count('1') == 0:
#         mn.add(n_o[0])
#         k = True 
#         for idx in range(1, len(n_o)-1):
#             if int(n_o[idx-1]) % 2 == 0 and int(n_o[idx]) % 2 == 0:
#                 k = False
#                 break
#             if int(n_o[idx-1]) % 2 != 0 and int(n_o[idx]) % 2 != 0:
#                 k = False
#                 break
#             mn.add(n_o[idx])
#         if len(mn) == len(n_o) and k == True:
#             count += 1
#         mn == set()
# print(count)