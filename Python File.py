from random import randint

file = open('c2.txt')
count = int(file.readline())
displays = []



size = 6
runs = 1000000
for e in range(1, runs):
    if e % 100 == 0:
        print(e)
    dis = [[0, 1, 0, 1, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 0, 1, 1, 0], [1, 0, 1, 0, 0, 1], [1, 0, 1, 1, 1, 1], [0, 1, 1, 1, 1, 0]]
    s = dis
    steps = []
    for _ in range(100):
        x = randint(0, size - 1)
        y = randint(0, size - 1)
        if sum([sum(sm) for sm in s]) != 0:
            for row in range(size):
                if s[y][row] == 0:
                    s[y][row] = 1
                elif s[y][row] == 1:
                    s[y][row] = 0

            for col in range(size):
                if s[col][x] == 0:
                    s[col][x] = 1
                elif s[col][x] == 1:
                    s[col][x] = 0

            if s[y][x] == 1:
                s[y][x] = 0
            elif s[y][x] == 0:
                s[y][x] = 1

            steps.append([y, x])
        else:
            if steps:
                print(steps)
                break
