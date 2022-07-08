from decimal import Decimal
n = int(input())


for i in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    m = int(input())
    cnt = 0
    for j in range(m):
        dx, dy, r = map(int, input().split())
        if ((x1-dx)**2 + (y1-dy)**2 < r**2) or ((x2-dx)**2 + (y2-dy)**2 < r**2):
            cnt = cnt + 1
        if ((x1 - dx) ** 2 + (y1 - dy) ** 2 < r ** 2) and ((x2 - dx) ** 2 + (y2 - dy) ** 2 < r ** 2):
            cnt = cnt - 1
        '''if (dx - r <= x1 <= dx + r and dy - r <= y1 <= dy + r ) or (dx - r <= x2 <= dx + r and dy - r <= y2 <= dy + r ):
            cnt = cnt + 1
        if (dx - r < x1 < dx + r and dy - r < y1 < dy + r ) and (dx - r < x2 < dx + r and dy - r < y2 < dy + r ):
            cnt = cnt - 1
        if (dx - r == x1 == dx + r and dy - r == y1 == dy + r ) or (dx - r == x2 == dx + r and dy - r == y2 == dy + r ):
            cnt = cnt - 1
        print(dx,dy,r,cnt)'''
    print(cnt)


