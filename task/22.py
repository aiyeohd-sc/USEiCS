# with open("task/22_25359.csv", "r") as f:
#     data = f.read()

# lines = data.split()

# id_time = {}
# id_total_time = {}
# dependences = {}
# dependences_set = {}

# def countDeps(id):
#     if id == '0':
#         return set()
    
#         # if id not in dependences_set:
#         #     dependences_set[id] = set()  
#         # dependences_set[id].add(cid)

#     deps = set()

#     for d in dependences[id]:
#         deps.add(d)
#         deps.update(countDeps(d))

#     return deps

    
# def countTotalTime(id):
#     if id == '0':
#         return 0
#     total_time = id_time[id]
#     for d in dependences[id]:
#         t = countTotalTime(d)
#         total_time += t
#     return total_time


# for line in lines:
#     line = line.split(",")
#     id_time[line[0]] = int(line[1])
#     dependences[line[0]] = line[2].split(";")

# for line in lines:
#     line = line.split(",")
#     s = countDeps(line[0])
#     print(line[0], *s)
#     total_time = id_time[line[0]]
#     for x in s:
#         if x == '0':
#             continue
#         total_time += id_time[x]
#     print(total_time)
#     print("-------------------")

# # for key in dependences_set:
# #     print(key, dependences_set[key])
