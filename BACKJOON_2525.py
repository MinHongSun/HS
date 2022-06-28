h, m = map(int, input().split())
need_time = int(input())

m += need_time

if m >= 60:
    for i in (range(m//60)):
            m -= 60
            h += 1

if h >= 24:
    h -= 24

print(h,m)
