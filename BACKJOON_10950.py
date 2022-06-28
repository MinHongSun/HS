import sys

n = int(sys.stdin.readline())
add = []

for i in range(n):
    add.append(list(map(int, sys.stdin.readline().split())))

for j in range(n):
    print(add[j][0] + add[j][1])