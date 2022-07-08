w, h, x, y, p = map(int,input().split())
r = h//2
cnt = 0
for _ in range(p):
    dx, dy = map(int, input().split())
    if x <= dx <= x+w and y <= dy <= y+h:
        cnt = cnt + 1
    elif ((dx-x)**2 + (dy-r-y)**2 <= r**2) or ((dx-w-x)**2 + (dy-r-y)**2 <= r**2):
        cnt = cnt + 1

print(cnt)