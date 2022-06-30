n = int(input())
li = []
for _ in range(n):
    li.append(input())


for i in range(50):
    a= []
    for j in range(n):
        if len(li[j]) == i and  li[j] not in a:
            a.append(li[j])
    if len(a) != 0:
        a.sort()
        for k in range(len(a)):
            print(a[k])
