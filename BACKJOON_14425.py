n, m = map(int, input().split())
li_1 = []
li_2 = []
for _ in range(n):
    li_1.append(input())
for _ in range(m):
    li_2.append(input())

cnt = 0
for i in range(m):
    if li_2[i] in li_1:
        cnt += 1
print(cnt)