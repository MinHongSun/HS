import sys
li = []
n = int(input())
for _ in range(n):
    li.append(list(map(int, input().split())))

li.sort(key=lambda x: (x[0],x[1]))

for i in range(n):
    print(li[i][0],li[i][1])