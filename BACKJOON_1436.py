n = int(input())
li = []
cnt = 666
while True:
    if "666" in str(cnt):
        li.append(cnt)

    if len(li) == n:
        break
    cnt += 1

print(max(li))
