from decimal import Decimal


n = int(input())

for _ in range(n):
    x1,y1,r1,x2,y2,r2 = map(int, input().split())
    l = Decimal(((x1-x2)**2 + (y1-y2)**2)**0.5)

    if (x1 == x2 and y1 == y2 and r1 == 0 and r2 == 0) or (l==r1 and r2 == 0) or (l==r2 and r1 == 0):
        print(1)

    elif x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)

    elif l > r1+r2 or l+r1 < r2 or l+r2 < r1:
        print(0)

    elif l == r1+r2 or l + r1 <= r2 or l + r2 <= r1:
        print(1)

    else:
        print(2)

