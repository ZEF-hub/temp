# #-----------19-----------
# def f(x, y ,p):
#     if x + y >= 69 and p == 3:
#         return True
#     else:
#         if x + y < 69 and p == 3:
#             return False
#     return f(x+1, y, p+1) or f(x, y+1, p+1) or\
#            f(x*2, y, p+1) or f(x, y*3, p+1)
#
# for i in range(1, 59):
#     if f(10, i, 1):
#         print(i)
#         break
#
#
# #-----------20-----------
# def f(x, y ,p):
#     if x + y >= 69 and p == 4:
#         return True
#     else:
#         if x + y < 69 and p == 4:
#             return False
#         else:
#             if x + y >= 69:
#                 return False
#     if p % 2 == 1:
#         return f(x+1, y, p+1) or f(x, y+1, p+1) or\
#                f(x*2, y, p+1) or f(x, y*3, p+1)
#
#     return f(x+1, y, p+1) and f(x, y+1, p+1) and\
#            f(x*2, y, p+1) and f(x, y*3, p+1)
#
# for i in range(1, 59):
#     if f(10, i, 1):
#         print(i)
#
#
# #-----------21-----------
# def f(x, y ,p):
#     if x + y >= 211 and (p == 3 or p == 5):
#         return True
#     else:
#         if x + y < 211 and p == 5:
#             return False
#         else:
#             if x + y >= 211:
#                 return False
#     if p % 2 == 0:
#         return f(x+1, y, p+1) or f(x, y+1, p+1) or\
#                f(x*2, y, p+1) or f(x, y*2, p+1)
#     else:
#         return f(x+1, y, p+1) and f(x, y+1, p+1) and\
#                f(x*2, y, p+1) and f(x, y*2, p+1)
#
# for i in range(1, 150):
#     if f(17, i, 1):
#         print(i)
#
#
# def f(x, y ,p):
#     if x + y >= 211 and p == 3:
#         return True
#     else:
#         if x + y < 211 and p == 3:
#             return False
#         else:
#             if x + y >= 211:
#                 return False
#     if p % 2 == 0:
#         return f(x+1, y, p+1) or f(x, y+1, p+1) or\
#                f(x*2, y, p+1) or f(x, y*2, p+1)
#     else:
#         return f(x+1, y, p+1) and f(x, y+1, p+1) and\
#                f(x*2, y, p+1) and f(x, y*2, p+1)
#
# for i in range(1, 150):
#     if f(17, i, 1):
#         print(i, '-')








from math import ceil
# #-----------19-----------
# def f(x, y ,p):
#     if x + y <= 40 and p == 3:
#         return True
#     else:
#         if x + y > 40 and p == 3:
#             return False
#     return f(x-1, y, p+1) or f(x, y-1, p+1) or\
#            f(ceil(x/2), y, p+1) or f(x, ceil(y/2), p+1)
#
# for i in range(100, 20, -1):
#     if f(20, i, 1):
#         print(i)
#         break


# #-----------20-----------
# def f(x, y ,p):
#     if x + y <= 40 and p == 4:
#         return True
#     else:
#         if x + y > 40 and p == 4:
#             return False
#         else:
#             if x + y <= 40:
#                 return False
#     if p % 2 == 1:
#         return f(x - 1, y, p + 1) or f(x, y - 1, p + 1) or \
#                f(ceil(x/2), y, p+1) or f(x, ceil(y/2), p+1)
#     else:
#         return f(x - 1, y, p + 1) and f(x, y - 1, p + 1) and \
#                f(ceil(x/2), y, p+1) and f(x, ceil(y/2), p+1)
#
# for i in range(1000, 20, -1):
#     if f(20, i, 1):
#         print(i)



# #-----------21-----------
# def f(x, y ,p):
#     if x + y <= 40 and (p == 3 or p == 5):
#         return True
#     else:
#         if x + y > 40 and p == 5:
#             return False
#         else:
#             if x + y <= 40:
#                 return False
#     if p % 2 == 0:
#         return f(x - 1, y, p + 1) or f(x, y - 1, p + 1) or \
#                f(ceil(x / 2), y, p + 1) or f(x, ceil(y / 2), p + 1)
#     else:
#         return f(x - 1, y, p + 1) and f(x, y - 1, p + 1) and \
#                f(ceil(x / 2), y, p + 1) and f(x, ceil(y / 2), p + 1)
#
# for i in range(100, 20, -1):
#     if f(20, i, 1):
#         print(i)
#
#
# def f(x, y ,p):
#     if x + y <= 40 and p == 3:
#         return True
#     else:
#         if x + y > 40 and p == 3:
#             return False
#         else:
#             if x + y <= 40:
#                 return False
#     if p % 2 == 0:
#         return f(x - 1, y, p + 1) or f(x, y - 1, p + 1) or \
#                f(ceil(x / 2), y, p + 1) or f(x, ceil(y / 2), p + 1)
#     else:
#         return f(x - 1, y, p + 1) and f(x, y - 1, p + 1) and \
#                f(ceil(x / 2), y, p + 1) and f(x, ceil(y / 2), p + 1)
#
# for i in range(100, 20, -1):
#     if f(20, i, 1):
#         print(i, '-')
