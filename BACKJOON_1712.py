li = list(map(int, input().split()))

if li[1] >= li[2]:
    print(-1)
else:
    n = int(li[0]/(li[2]-li[1]))
    print(n+1)
