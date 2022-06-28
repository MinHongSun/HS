a,b = map(str, input().split())
cnt = 0
li = []
s = ""
if len(a) >= len(b):
    for i in range(len(a)-1,-1,-1):
        li.append(int(a[i])+int(b[i-len(a)+len(b)]))
        if i-len(a)+len(b) == 0:
            i = cnt
            break
    if len(a) != len(b):
        for j in range(cnt,-1,-1):
            li.append(int(a[j]))
else:
    for i in range(len(b)-1,-1,-1):
        li.append(int(b[i])+int(a[i-len(b)+len(a)]))
        if i-len(b)+len(a) == 0:
            i = cnt
            break
    if len(a) != len(b):
        for j in range(cnt, -1, -1):
            li.append(int(a[j]))

for k in range(len(li)-1):
    if li[k] >= 10:
        li[k+1] = li[k+1] + 1
        li[k] = li[k] - 10

if li[len(li)-1] >= 10:
    li[len(li)-1] = li[len(li)-1] - 10
    li.append(1)

for l in range(len(li)-1,-1,-1):
    s = s + str(li[l])

print(s)