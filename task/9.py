# count = 0
# for line in open('ege/lesson/9.txt'):
#     a = [int(x) for x in line.split()]
#     two_in = [x for x in a if a.count(x) == 2]
#     one_in = [x for x in a if a.count(x) == 1]
#     if len(one_in) == 4:
#         if sum(two_in) >= sum(one_in)/len(one_in):
#             count += 1
# print(count)


# --------------------------------------------------------------------------------------------------------------------


# row_num = 0
# max_row = 0
# for line in open('ege/lesson/9.txt'):
#     row_num += 1
#     a = [int(x) for x in line.split()]
#     two_in = [x for x in a if a.count(x) == 2]
#     one_in = [x for x in a if a.count(x) == 1]
#     if len(two_in) == 6 and len(one_in) == 2:
#         if (max(two_in) - min(two_in))**2 > 2*(one_in[0]**2+one_in[1]**2):
#             max_row = row_num
# print(max_row)


# --------------------------------------------------------------------------------------------------------------------


# sum_list = [100000]
# for line in open('ege/lesson/9.txt'):
#     a = [int(x) for x in line.split()]
#     two_in = [x for x in a if a.count(x) == 2]
#     degree = min(a)**2
#     if len(two_in) == 6 or degree in a:
#        summ = sum(a)
#        if summ < min(sum_list):
#            sum_list.append(summ)
# print(sum_list)


# --------------------------------------------------------------------------------------------------------------------


# m = []
# for s in open('ege/lesson/9.txt'):
#     a = sorted([int(x) for x in s.split()])
#     k = 0
#     for x in set(a):
#         k += a.count(x)//2
#     if (a[0]**2 in a)+(k>=3)==1:
#         m.append(sum(a))
# print(min(m))

# count = 0
# for line in open('ege/lesson/9.txt'):
#     a = [int(x) for x in line.split()]
#     two_in = [x for x in a if a.count(x) == 2]
#     one_in = [x for x in a if a.count(x) == 1]
#     if len(one_in) == 4:
#         if sum(two_in) >= sum(one_in)/len(one_in):
#             count += 1
# print(count)


# --------------------------------------------------------------------------------------------------------------------


# row_num = 0
# max_row = 0
# for line in open('ege/lesson/9.txt'):
#     row_num += 1
#     a = [int(x) for x in line.split()]
#     two_in = [x for x in a if a.count(x) == 2]
#     one_in = [x for x in a if a.count(x) == 1]
#     if len(two_in) == 6 and len(one_in) == 2:
#         if (max(two_in) - min(two_in))**2 > 2*(one_in[0]**2+one_in[1]**2):
#             max_row = row_num
# print(max_row)


# --------------------------------------------------------------------------------------------------------------------


# sum_list = [100000]
# for line in open('ege/lesson/9.txt'):
#     a = [int(x) for x in line.split()]
#     two_in = [x for x in a if a.count(x) == 2]
#     degree = min(a)**2
#     if len(two_in) == 6 or degree in a:
#        summ = sum(a)
#        if summ < min(sum_list):
#            sum_list.append(summ)
# print(sum_list)


# --------------------------------------------------------------------------------------------------------------------


# curr_row = 0
# for line in open('ege/lesson/9.txt'):
#     curr_row += 1
#     a = [int(x) for x in line.split()]
#     flag = True
#     if_2 = False
#     for i in range(1, len(a)):
#         if a[i] < a[i-1]:
#             flag = False
#             break
#         if a.count(a[i]) > 1:
#             c = str(a[i])
#             summ = 0
#             for x in range(len(c)):
#                 summ += int(x)
#             if summ%2 == 0:
#                 if_2 = True
#     if flag and if_2:
#         max_row = curr_row
# print(max_row)

# count = 0
# for line in open('ege/lesson/9.txt'):
#     a = [int(x) for x in line.split()]
#     two_in = [x for x in a if a.count(x) == 2]
#     one_in = [x for x in a if a.count(x) == 1]
#     if len(one_in) == 4:
#         if sum(two_in) >= sum(one_in)/len(one_in):
#             count += 1
# print(count)


# --------------------------------------------------------------------------------------------------------------------


# row_num = 0
# max_row = 0
# for line in open('ege/lesson/9.txt'):
#     row_num += 1
#     a = [int(x) for x in line.split()]
#     two_in = [x for x in a if a.count(x) == 2]
#     one_in = [x for x in a if a.count(x) == 1]
#     if len(two_in) == 6 and len(one_in) == 2:
#         if (max(two_in) - min(two_in))**2 > 2*(one_in[0]**2+one_in[1]**2):
#             max_row = row_num
# print(max_row)


# --------------------------------------------------------------------------------------------------------------------


# sum_list = [100000]
# for line in open('ege/lesson/9.txt'):
#     a = [int(x) for x in line.split()]
#     two_in = [x for x in a if a.count(x) == 2]
#     degree = min(a)**2
#     if len(two_in) == 6 or degree in a:
#        summ = sum(a)
#        if summ < min(sum_list):
#            sum_list.append(summ)
# print(sum_list)


# --------------------------------------------------------------------------------------------------------------------


# curr_row = 0
# max_row = 0
# summ_a = 0
# for f in open('ege/lesson/9.txt'):
#     curr_row += 1
#     a = [int(x) for x in f.split()]
#     k = 0
#     z = 0
#     summ = 0
#     orig_sum = 0
#     if len(set(a)) != 5:
#         continue
#     for x in set(a):
#         if a.count(x) == 3:
#             k += 1
#             summ += x
#         if a.count(x) == 1:
#             orig_sum += x
#         if k > 1 or a.count(x) == 2:
#             break
#     if (k == 1) and (summ >= orig_sum/4) and len(set(a)) == 5:
#         if max_row < curr_row:
#             summ_a = sum(a)
# print(summ_a)

# count = 0
# for line in open('ege/lesson/9.txt'):
#     a = [int(x) for x in line.split()]
#     two_in = [x for x in a if a.count(x) == 2]
#     one_in = [x for x in a if a.count(x) == 1]
#     if len(one_in) == 4:
#         if sum(two_in) >= sum(one_in)/len(one_in):
#             count += 1
# print(count)


# --------------------------------------------------------------------------------------------------------------------


# row_num = 0
# max_row = 0
# for line in open('ege/lesson/9.txt'):
#     row_num += 1
#     a = [int(x) for x in line.split()]
#     two_in = [x for x in a if a.count(x) == 2]
#     one_in = [x for x in a if a.count(x) == 1]
#     if len(two_in) == 6 and len(one_in) == 2:
#         if (max(two_in) - min(two_in))**2 > 2*(one_in[0]**2+one_in[1]**2):
#             max_row = row_num
# print(max_row)


# --------------------------------------------------------------------------------------------------------------------


# sum_list = [100000]
# for line in open('ege/lesson/9.txt'):
#     a = [int(x) for x in line.split()]
#     two_in = [x for x in a if a.count(x) == 2]
#     degree = min(a)**2
#     if len(two_in) == 6 or degree in a:
#        summ = sum(a)
#        if summ < min(sum_list):
#            sum_list.append(summ)
# print(sum_list)


# --------------------------------------------------------------------------------------------------------------------


# count = 0
# for line in open('ege/lesson/9.txt'):
#     a = [int(x) for x in line.split()]
#     if len(set(a)) != 4:
#         continue
#     triple = 0
#     double = 0
#     max_thr = 0
#     max_one = 0
#     for x in set(a):
#         if a.count(x) == 3:
#             triple += 1
#             if max_thr < x:
#                 max_thr = x
#         elif a.count(x) == 2:
#             double += 1
#             if max_thr < x:
#                 max_thr = x
#         elif a.count(x) == 1 and x > max_one:
#             max_one = x
#     if (triple != 1) or (double != 1):
#             continue
#     if (max_thr > max_one):
#         count += 1
# print(count)

# count = 0
# for line in open('ege/lesson/9.txt'):
#     a = [int(x) for x in line.split()]
#     two_in = [x for x in a if a.count(x) == 2]
#     one_in = [x for x in a if a.count(x) == 1]
#     if len(one_in) == 4:
#         if sum(two_in) >= sum(one_in)/len(one_in):
#             count += 1
# print(count)


# --------------------------------------------------------------------------------------------------------------------


# row_num = 0
# max_row = 0
# for line in open('ege/lesson/9.txt'):
#     row_num += 1
#     a = [int(x) for x in line.split()]
#     two_in = [x for x in a if a.count(x) == 2]
#     one_in = [x for x in a if a.count(x) == 1]
#     if len(two_in) == 6 and len(one_in) == 2:
#         if (max(two_in) - min(two_in))**2 > 2*(one_in[0]**2+one_in[1]**2):
#             max_row = row_num
# print(max_row)


# --------------------------------------------------------------------------------------------------------------------


# sum_list = [100000]
# for line in open('ege/lesson/9.txt'):
#     a = [int(x) for x in line.split()]
#     two_in = [x for x in a if a.count(x) == 2]
#     degree = min(a)**2
#     if len(two_in) == 6 or degree in a:
#        summ = sum(a)
#        if summ < min(sum_list):
#            sum_list.append(summ)
# print(sum_list)


# --------------------------------------------------------------------------------------------------------------------


# curr = 0
# max_r = 0
# for line in open('ege/lesson/9.txt'):
#     curr += 1
#     a = sorted([int(x) for x in line.split()])
#     summ = (a[0] + a[-1])*2
#     summ_2 = (sum(a[1:len(a)-1]))*3
#     if len(set(a)) == len(a) and summ == summ_2:
#         if curr > max_r:
#             max_r = curr
# print(max_r)

# count = 0
# for line in open('ege/lesson/9.txt'):
#     a = [int(x) for x in line.split()]
#     two_in = [x for x in a if a.count(x) == 2]
#     one_in = [x for x in a if a.count(x) == 1]
#     if len(one_in) == 4:
#         if sum(two_in) >= sum(one_in)/len(one_in):
#             count += 1
# print(count)


# --------------------------------------------------------------------------------------------------------------------


# row_num = 0
# max_row = 0
# for line in open('ege/lesson/9.txt'):
#     row_num += 1
#     a = [int(x) for x in line.split()]
#     two_in = [x for x in a if a.count(x) == 2]
#     one_in = [x for x in a if a.count(x) == 1]
#     if len(two_in) == 6 and len(one_in) == 2:
#         if (max(two_in) - min(two_in))**2 > 2*(one_in[0]**2+one_in[1]**2):
#             max_row = row_num
# print(max_row)


# --------------------------------------------------------------------------------------------------------------------


# sum_list = [100000]
# for line in open('ege/lesson/9.txt'):
#     a = [int(x) for x in line.split()]
#     two_in = [x for x in a if a.count(x) == 2]
#     degree = min(a)**2
#     if len(two_in) == 6 or degree in a:
#        summ = sum(a)
#        if summ < min(sum_list):
#            sum_list.append(summ)
# print(sum_list)


# --------------------------------------------------------------------------------------------------------------------


# curr_row = 0
# for line in open('ege/lesson/9.txt'):
#     curr_row += 1
#     a = [int(x) for x in line.split()]
#     double = 0
#     summ_org = []
#     summ_double = 0
#     if len(set(a)) != 5:
#         continue
#     for x in set(a):
#         if a.count(x) == 2:
#             double += 1
#             summ_double += x/2
#         elif a.count(x) == 1:
#             summ_org.append(x)
#     if double == 2 and summ_double < max(summ_org):
#         print(curr_row)
#         break

# count = 0
# for line in open('ege/lesson/9.txt'):
#     a = [int(x) for x in line.split()]
#     two_in = [x for x in a if a.count(x) == 2]
#     one_in = [x for x in a if a.count(x) == 1]
#     if len(one_in) == 4:
#         if sum(two_in) >= sum(one_in)/len(one_in):
#             count += 1
# print(count)


# --------------------------------------------------------------------------------------------------------------------


# row_num = 0
# max_row = 0
# for line in open('ege/lesson/9.txt'):
#     row_num += 1
#     a = [int(x) for x in line.split()]
#     two_in = [x for x in a if a.count(x) == 2]
#     one_in = [x for x in a if a.count(x) == 1]
#     if len(two_in) == 6 and len(one_in) == 2:
#         if (max(two_in) - min(two_in))**2 > 2*(one_in[0]**2+one_in[1]**2):
#             max_row = row_num
# print(max_row)


# --------------------------------------------------------------------------------------------------------------------


# sum_list = [100000]
# for line in open('ege/lesson/9.txt'):
#     a = [int(x) for x in line.split()]
#     two_in = [x for x in a if a.count(x) == 2]
#     degree = min(a)**2
#     if len(two_in) == 6 or degree in a:
#        summ = sum(a)
#        if summ < min(sum_list):
#            sum_list.append(summ)
# print(sum_list)


# --------------------------------------------------------------------------------------------------------------------

# curr_row = 0
# max_row = 0
# for line in open('ege/lesson/9.txt'):
#     curr_row += 1
#     a = [int(x) for x in line.split()]
#     if len(set(a)) != 4:
#         continue
#     k = False
#     val = 0
#     summ = []
#     for x in set(a):
#         if a.count(x) == 3:
#             val = x
#             k = True
#         elif a.count(x) == 1:
#             summ.append(x)
#     if (k == True) and (sum(summ)/len(summ) < val):
#         max_row = curr_row
# print(max_row)


# count = 0
# for line in open('ege/lesson/9.txt'):
#     a = [int(x) for x in line.split()]
#     two_in = [x for x in a if a.count(x) == 2]
#     one_in = [x for x in a if a.count(x) == 1]
#     if len(one_in) == 4:
#         if sum(two_in) >= sum(one_in)/len(one_in):
#             count += 1
# print(count)


# --------------------------------------------------------------------------------------------------------------------


# row_num = 0
# max_row = 0
# for line in open('ege/lesson/9.txt'):
#     row_num += 1
#     a = [int(x) for x in line.split()]
#     two_in = [x for x in a if a.count(x) == 2]
#     one_in = [x for x in a if a.count(x) == 1]
#     if len(two_in) == 6 and len(one_in) == 2:
#         if (max(two_in) - min(two_in))**2 > 2*(one_in[0]**2+one_in[1]**2):
#             max_row = row_num
# print(max_row)


# --------------------------------------------------------------------------------------------------------------------


# sum_list = [100000]
# for line in open('ege/lesson/9.txt'):
#     a = [int(x) for x in line.split()]
#     two_in = [x for x in a if a.count(x) == 2]
#     degree = min(a)**2
#     if len(two_in) == 6 or degree in a:
#        summ = sum(a)
#        if summ < min(sum_list):
#            sum_list.append(summ)
# print(sum_list)


# --------------------------------------------------------------------------------------------------------------------


# count = 0
# for line in open('ege/lesson/9.txt'):
#     a = sorted([int(x) for x in line.split()])
#     if len(set(a)) == len(a):
#         if a[0]*a[1] <= sum(a[2:len(a)]):
#             count += 1
# print(count)


# ====================================================================================================================

	
# № 24889 (Уровень: Средний)
# Откройте файл электронной таблицы, содержащей в каждой строке восемь натуральных чисел. Определите количество строк 
# таблицы, содержащих числа, для которых выполнены оба условия:
# – в строке максимальное число встречается три или четыре раза, остальные числа без повторений;
# – сумма минимального и максимального из неповторяющихся чисел не больше суммы других неповторяющихся.
# В ответе запишите только число.
# ответ 213

# count = 0
# for line in open('9_24889.txt'):
#     data = sorted([int(x) for x in line.split()])
#     four_or_tri = 0
#     one_enter = []
#     flag = True
#     for x in set(data):
#         if data.count(x) == 3 or data.count(x) == 4:
#             if x == data[-1]:
#                 four_or_tri += 1
#             else:
#                 flag = False
#                 break
#         elif data.count(x) == 1 and x != data[-1]:
#             one_enter.append(x)
#         else:
#             flag = False
#             break
#     if not flag:
#         continue
#     one_enter.sort()
#     m2_sum = one_enter[0] + one_enter[-1]
#     else_sum = sum(one_enter[1:-1])
#     if four_or_tri == 1 and m2_sum <= else_sum:
#         count += 1
# print(count)


# --------------------------------------------------------------------------------------------------------------------

	
# № 24360 (Уровень: Сложный)
# (А. Ходарин) Откройте файл электронной таблицы, содержащей в каждой строке восемь натуральных чисел. Определите 
# минимальную сумму чисел в строке таблицы, содержащей числа, для которой выполнено ровно одно условие:
# – квадрат минимального числа присутствует в строке;
# – из чисел строки можно получить три пары одинаковых чисел (например, строку с числами 8 9 6 4 8 9 6 2 можно 
# представить тремя парами одинаковых чисел: 8 8 9 9 6 6, а строку 8 2 7 8 8 2 2 2 можно представить, например, тремя 
# парами одинаковых чисел 2 2 2 2 8 8).
# В ответе запишите только число.
# ответ 98

# all_sums = []
# for line in open('9_24360.txt'):
#     a = [int(x) for x in line.split()]
#     sq_min = min(a)**2 in a
#     count = 0
#     flag = False
#     for x in set(a):
#         count += a.count(x)//2
#     if count == 3:
#         flag = True
#     if flag and not sq_min:
#         all_sums += [sum(a)]
#     elif not flag and sq_min:
#         all_sums += [sum(a)]
# print(min(all_sums))

# count = 0
# for line in open('ege/lesson/9.txt'):
#     a = [int(x) for x in line.split()]
#     two_in = [x for x in a if a.count(x) == 2]
#     one_in = [x for x in a if a.count(x) == 1]
#     if len(one_in) == 4:
#         if sum(two_in) >= sum(one_in)/len(one_in):
#             count += 1
# print(count)


# --------------------------------------------------------------------------------------------------------------------


# row_num = 0
# max_row = 0
# for line in open('ege/lesson/9.txt'):
#     row_num += 1
#     a = [int(x) for x in line.split()]
#     two_in = [x for x in a if a.count(x) == 2]
#     one_in = [x for x in a if a.count(x) == 1]
#     if len(two_in) == 6 and len(one_in) == 2:
#         if (max(two_in) - min(two_in))**2 > 2*(one_in[0]**2+one_in[1]**2):
#             max_row = row_num
# print(max_row)


# --------------------------------------------------------------------------------------------------------------------


# sum_list = [100000]
# for line in open('ege/lesson/9.txt'):
#     a = [int(x) for x in line.split()]
#     two_in = [x for x in a if a.count(x) == 2]
#     degree = min(a)**2
#     if len(two_in) == 6 or degree in a:
#        summ = sum(a)
#        if summ < min(sum_list):
#            sum_list.append(summ)
# print(sum_list)


# --------------------------------------------------------------------------------------------------------------------