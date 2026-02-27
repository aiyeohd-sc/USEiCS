# 25363 
# with open("26_25363.txt", "r") as f:
#     n = int(f.readline())
#     j = 1
#     data_1 = []
#     for i in f.readlines():
#         data = i.split()
#         data_1.append((int(data[0]), 1, j))
#         data_1.append((int(data[1]), 2, j))
#         j += 1

# data_1.sort(key=lambda x:x[0])

# answ = [0]*n

# start = 0
# end = n-1
# set_ = set()
# last_el = 0

# for i in data_1:
#     if i[2] not in set_:
#         set_.add(i[2])
#         if i[1] == 1:
#             answ[start] = i[2]
#             start += 1
#         else:
#             answ[end] = i[2]
#             end -= 1
#         last_el = i[2]

# for i in range(len(answ)):
#     if answ[i] == last_el:
#         print(last_el)
#         print(n-i-1)


# -----------------------------------------------------------------------------------


