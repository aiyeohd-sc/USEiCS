# 25363 
# num = 0
# data = []
# with open('26_25363.txt', 'r') as f:
#     n = int(f.readline())
#     for i in f.readlines():
#         el1,el2 = i.split()
#         data.append((num, int(el1), 1))
#         data.append((num, int(el2), 2))
#         num += 1

# set_answ = set()
# answ = [0]*n
# data.sort(key = lambda x:x[1])
# start = 0
# end = n-1

# for i in data:
#     if i[0] not in set_answ:
#         if i[2] == 1:
#             answ[start] = i[0]
#             start += 1
#         else:
#             answ[end] = i[0]
#             end -= 1
#         set_answ.add(i[0])
#         last_n = i[0]

# top_k = 0

# for i in answ:
#     if i == last_n:
#         print(last_n + 1)
#         print(n - top_k - 1)
#         break
#     top_k += 1


# -----------------------------------------------------------------------------------


home = []
with open('26_24897.txt', 'r') as f:
    n = int(f.readline())
    for i in f.readlines():
        el1,el2,el3 = i.split()
        home.append((int(el2), int(el3), int(el1)))

home.sort()

max_seq = 0
seq = 0
min_num_req = float('inf')
answ_home = 0
num_p_m = 0
num_p = home[0][1]
num_req = home[0][2]

for i in range(n-1):
    if home[i][0] == home[i+1][0] and home[i][1]+1 == home[i+1][1]:
        seq += 1
    elif home[i][0] == home[i+1][0] and home[i][1] == home[i+1][1]:
        continue
    else:
        if seq > max_seq:
            max_seq = seq
            answ_home = home[i][0]
            min_num_req = num_req
            num_p_m = num_p
        if seq == max_seq:
            if num_req < min_num_req:
                answ_home = home[i][0]
                min_num_req = num_req
                num_p_m = num_p
        
        num_p = home[i+1][1]
        num_req = home[i+1][2]
        seq = 0

if seq > max_seq:
    max_seq = seq
    answ_home = home[i-1][0]
    num_p_m = num_p
elif seq == max_seq:
    if num_req < answ_req:
        answ_home = home[i-1][0]
        num_p_m = num_p

print(answ_home, num_p_m)
