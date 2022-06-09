#2256
s = list(map(int, open('27_A (3).txt').readlines()))
s = list(map(int, open('27_B (2).txt').readlines()))

# Количество делящихся на пять кратное трём
count_5 = 0
for i in s:
    if i % 5 == 0:
        count_5 += 1
print(count_5)
count_5 = count_5 // 3 * 3

# sn = [Число, индекс]
sn = []
for i in range(len(s)):
    if s[i] % 5 == 0:
        sn.append([s[i], i])

sum1 = sum(s[:sn[count_5+1][1]])
sum2 = sum(s[sn[0][1]+1:sn[-1][1]])
sum3 = sum(s[sn[1][1]+1:])
print(sum1, sum2, sum3)
