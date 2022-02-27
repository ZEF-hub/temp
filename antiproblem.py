from random import randint

file = open('c2.txt')
count = int(file.readline())
displays = []

# for i in range(count):
#     size = int(file.readline())
#     display = []
#     for row in range(size):
#         display.append(list(map(int, file.readline().split())))
#     displays.append(display)
# print(displays)
#
# runs = 100000
# for dis in displays:
#     size = len(dis)
#     best_steps = []
#     for q in range(1, runs):
#         count+=1
#         # if q % int(str(runs)[:-1]) == 0:
#         #     print('ready to ' + str(q)[0:2] + '%')
#         s = dis
#         steps = []
#         for _ in range(10):
#             x = randint(0, size-1)
#             y = randint(0, size-1)
#             if sum([sum(sm) for sm in s]) != 0:
#                 for row in range(size):
#                     if s[y][row] == 0:
#                         s[y][row] = 1
#                     elif s[y][row] == 1:
#                         s[y][row] = 0
#
#                 for col in range(size):
#                     if s[col][x] == 0:
#                         s[col][x] = 1
#                     elif s[col][x] == 1:
#                         s[col][x] = 0
#
#                 if s[y][x] == 1:
#                     s[y][x] = 0
#                 elif s[y][x] == 0:
#                     s[y][x] = 1
#
#                 steps.append([y, x])
#             else:
#                 if steps:
#                     print(steps)
#                     # if best_steps:
#                     #     if len(steps) < len(best_steps):
#                     #         best_steps = steps
#                     # else:
#                     #     best_steps = steps
#                     break
#     print('------------------', count)
#     # print(best_steps)
#
#
#
#
# # print(sum([sum(sm)for sm in s]))


# [[[0, 0, 1, 0], [0, 0, 1, 0], [1, 1, 1, 1], [0, 0, 1, 0]], [[0, 1, 1, 0], [1, 1, 0, 1], [1, 0, 1, 1], [0, 1, 1, 0]], [[1, 1, 0], [1, 0, 1], [0, 1, 1]]]
# [[[0, 1, 0, 0], [1, 0, 1, 0], [1, 0, 1, 0], [1, 1, 1, 1]], [[0, 0, 1, 1], [0, 1, 1, 0], [1, 0, 1, 0], [1, 1, 0, 1]], [[0, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 0], [0, 1, 1, 0]]]
# [[[0, 1, 1, 1, 0], [1, 1, 0, 1, 0], [1, 0, 0, 0, 0], [1, 0, 0, 1, 1], [0, 1, 0, 0, 0]], [[1, 1, 0, 0, 0], [0, 1, 0, 0, 1], [0, 0, 0, 1, 1], [1, 0, 1, 1, 1], [0, 0, 1, 0, 1]], [[0, 1, 0, 1, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 0, 1, 1, 0], [1, 0, 1, 0, 0, 1], [1, 0, 1, 1, 1, 1], [0, 1, 1, 1, 1, 0]], [[0, 0, 1, 0, 0, 0, 1], [0, 0, 0, 0, 1, 0, 1], [1, 1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1, 0], [1, 0, 1, 1, 1, 0, 0], [1, 1, 1, 1, 1, 1, 0], [0, 1, 1, 0, 1, 1, 0]], [[1, 1, 0, 1, 0, 1, 0, 1], [1, 1, 0, 1, 0, 1, 0, 1], [0, 0, 1, 0, 1, 0, 0, 0], [0, 1, 0, 1, 0, 1, 1, 1], [1, 1, 1, 1, 1, 1, 0, 1], [0, 1, 0, 1, 0, 1, 1, 1], [1, 1, 0, 1, 0, 1, 0, 1], [0, 0, 1, 0, 1, 0, 0, 0]], [[1, 1, 0, 1, 1, 1, 1, 1], [1, 0, 0, 0, 1, 1, 1, 1], [1, 0, 0, 0, 1, 1, 1, 1], [1, 1, 0, 0, 1, 1, 0, 1], [1, 1, 0, 0, 1, 1, 0, 1], [1, 1, 0, 0, 0, 1, 1, 1], [0, 0, 0, 1, 1, 0, 0, 0], [0, 0, 1, 1, 0, 0, 0, 0]], [[1, 1, 0, 1, 0, 0, 1, 0, 1, 0], [1, 0, 0, 1, 1, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 1, 1, 1, 0, 0], [0, 1, 0, 1, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 0, 0, 0, 1, 0], [1, 0, 1, 0, 1, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 1, 0, 1, 0, 1], [0, 1, 0, 0, 0, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 0, 0, 0, 1]]]


# dis = [[0, 0, 1, 0], [0, 0, 1, 0], [1, 1, 1, 1], [0, 0, 1, 0]]
# size = len(dis)
# runs = 1000
# for _ in range(1, runs):
#     s = dis
#     print(s, dis)
#     steps = []
#     for _ in range(10):
#         x = randint(0, size - 1)
#         y = randint(0, size - 1)
#         if sum([sum(sm) for sm in s]) != 0:
#             for row in range(size):
#                 if s[y][row] == 0:
#                     s[y][row] = 1
#                 elif s[y][row] == 1:
#                     s[y][row] = 0
#
#             for col in range(size):
#                 if s[col][x] == 0:
#                     s[col][x] = 1
#                 elif s[col][x] == 1:
#                     s[col][x] = 0
#
#             if s[y][x] == 1:
#                 s[y][x] = 0
#             elif s[y][x] == 0:
#                 s[y][x] = 1
#
#             steps.append([y, x])
#         else:
#             if steps:
#                 print(steps)
#                 break
