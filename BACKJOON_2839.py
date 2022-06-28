n = int(input())
k = 0

a = int(n/5)

for i in range(a,-1,-1):
    if (n-(5*i))%3 == 0:
        k = int(i + (n-(5*i))/3)
        break

if k == 0:
    print(-1)
else:
    print(k)
