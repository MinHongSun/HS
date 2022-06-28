n = int(input())
li = []
i = 2
while True:
    if i > n:
        break
    if n%i == 0:
        n = int(n/i)
        li.append(i)
    else:
        i = i + 1

for j in range(len(li)):
    print(li[j])