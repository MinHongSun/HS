n = int(input())
k = 10
li = []
result = 0
for i in range(6):
    if int(n/(10**i)) > 0:
        k = i

for j in range(n,0,-1):
    li = list(map(int,str(j)))
    if n == j + sum(li):
        result = j

print(result)

