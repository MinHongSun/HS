n = int(input())
li = list(map(int, input().split()))
cnt = 0
k = n
for i in range(n):
    if li[i] == 1:
        k = k-1
        continue
    for j in range(li[i]-1,1,-1):
        if li[i]%j == 0:
            k = k - 1
            break

print(k)