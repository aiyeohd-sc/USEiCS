# 24_20968 
# s = open('24_20968.txt').readline().strip().replace('*', '+')
# j = res = n_st = 0
# for i in range(len(s)):
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
# print(res)


s = open('24_20968.txt').readline().strip().replace('*', '+')
i = j = res = n_st = 0
while i < len(s):
    if s[i] == '+':
        if i == j or s[i-1] == '+' or s[i-1] in '13579':
            j = i + 1
        n_st = i + 1
    else:
        if i > n_st and s[n_st] == '0':
            j = i
            n_st = i
        if s[i] in '02468':
            res = max(res, i-j+1)
    i += 1
print(res)
