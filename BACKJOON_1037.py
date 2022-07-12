n = int(input())
li = list(map(int, input().split()))

if n == 1:
    print(li[0]**2)
else:
    li.sort()
    print(li[0]*li[n-1])