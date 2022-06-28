n = list(map(int, input().split()))
n.sort()
result = 0

if n[0] == n[1] == n[2]:
    result = 10000 + n[0] * 1000

elif n[0] == n[1]:
    result = 1000 + n[0] * 100

elif n[1] == n[2]:
    result = 1000 + n[1] * 100

else:
    result = n[2] * 100

print(result)