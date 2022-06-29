n, m = map(int, input().split())
li = list(map(int,input().split()))
s = 0
li.sort()
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1, n):
            if li[i]+li[j]+li[k] > m or li[i]+li[j]+li[k] < s:
                continue
            s = li[i]+li[j]+li[k]


print(s)
