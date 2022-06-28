import math

n = int(input())

for i in range(n):
    ht = list(map(int, input().split()))
    x = math.ceil(ht[2]/ht[0])
    if ht[2]%ht[0] == 0:
        y = str(ht[0])
    else:
        y = str(ht[2]%ht[0])

    if x < 10 :
        x = str(0) + str(x)
    else:
        x = str(x)
    print(y+x)