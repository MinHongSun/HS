def df(a,b):
    if a % b == 0:
        return b
    else:
        c = b
        b = a % b
        return df(c,b)



n= int(input())
for _ in range(n):
    a, b = map(int, input().split())
    s = df(max(a, b), min(a, b))

    print(int(a*b/s))


