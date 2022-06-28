n, k = map(int, input().split())
data = list(map(int, input().split()))

for i in range(n):
    if data[i] < k:
        print(data[i], end=' ')