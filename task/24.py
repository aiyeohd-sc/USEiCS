# # 26551
# with open("ege/task/24_26551.txt", "r") as f:
#     data = f.read()

# set_ = set(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D"])
# set_chet = set(["2", "4", "6", "8", "0", "A", "C"])

# max_seq = ""
# max_seq_len = 0

# j = 0

# for i in range(len(data)):
#     if data[i] not in set_:
#         j = i + 1
#         continue
#     if data[i] in set_chet and max_seq<data[j:i+1]:
#         if len(data[j:i+1]) > max_seq_len:
#             max_seq = data[j:i+1]
#             max_seq_len = len(max_seq)
# i = 0
# while max_seq[i] == "0":
#     i += 1
# print(len(max_seq[i:]))

# -----------------------------------------------------------------------------------

# 26549
# with open("ege/task/24_26549.txt", "r") as f:
#     data = f.read()

# data = data.replace("2025", "|")
# chet_2025 = 0
# chet_Y = 0

# max_seq_len = 0
# j = 0

# for i in range(len(data)):
#     if data[i] == "|":
#         if chet_2025 == 50:
#             while data[j] != "|":
#                 if data[j] == "Y":
#                     chet_Y -= 1
#                 j += 1
#             j += 1
#             if max_seq_len<len(data[j:i+1]) and chet_Y >= 140:
#                 max_seq_len = len(data[j:i+1])
#         else:
#             chet_2025 += 1
#             if chet_2025 == 50:
#                 max_seq_len = len(data[j:i+1])
#     if data[i] == "Y":
#         chet_Y += 1
# print(max_seq_len + 50*3 + 3)

# -----------------------------------------------------------------------------------

# 25361
# with open("task/24_25361.txt", "r") as f:
#     data = f.read()
# set_ = set(["0", "2", "4", "6", "8"])
# max_len_seq = 0
# f_count = 0
# j = 0
# i = 0
# while i < len(data):
#     if data[i] in set_:
#         j = i + 1
#         f_count = 0
#         while j < len(data):
#             if data[j] in set_:
#                 break
#             if data[j] == "F":
#                 f_count += 1
#                 if f_count == 76:
#                     if j-i > max_len_seq:
#                         max_len_seq = j-i
#                     i = j
#                     break
#             j += 1
#     i = max(i+1, j)
# print(max_len_seq+1)

# -----------------------------------------------------------------------------------

# 22359
# with open("task/24_22359.txt", "r") as f:
#     data = f.read()
# alph = set(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E"])
# multpl_five = set(["0", "5", "A"])
# max_digit = 0
# last_index = 0
# curr_digit = 0
# i = 0
# j = 0
# while i < len(data):
#     if data[i] in alph:
#         j = i + 1
#         while j < len(data):
#             if data[j] not in alph:
#                 break
#             if data[j] in multpl_five:
#                 curr_digit = int(data[i:j+1], 15)
#                 if curr_digit > max_digit:
#                     max_digit = curr_digit
#                     last_index = j
#             j += 1
#     i = max(i+1,j)
# print(last_index)


# -----------------------------------------------------------------------------------


# 21908
# with open("task/24_21908.txt", "r") as f:
#     data = f.read()
# alph = set(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D"])
# chet = set(["0", "2", "4", "6", "8", "A", "C"])
# max_digit = 0
# max_str = ""
# i = 0
# j = 0
# while i < len(data):
#     if data[i] in alph:
#         j = i + 1
#         while j < len(data):
#             if data[j] not in alph:
#                 break
#             if data[j] in chet:
#                 curr_digit = int(data[i:j+1], 14)
#                 if curr_digit > max_digit:
#                     max_digit = curr_digit
#                     max_str = data[i:j+1]
#             j += 1
#     i = max(i+1, j)
# n = 0
# while max_str[n] == "0":
#     n += 1
# print(len(max_str[n:j+1]))


# -----------------------------------------------------------------------------------


# 20968
# s = open('24_20968.txt').readline().strip().replace('*', '+')
# i = j = res = n_st = 0
# while i < len(s):
#     if s[i] == '+':
#         if i == j or s[i-1] == '+' or s[i-1] in '13579':
#             j = i + 1
#         n_st = i + 1
#     else:
#         if i > n_st and s[n_st] == '0':
#             j = i
#             n_st = i
#         if s[i] in '02468':
#             res = max(res, i-j+1)
#     i += 1
# print(res)