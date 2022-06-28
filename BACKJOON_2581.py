a = int(input())
b = int(input())
li = []
for i in range(a,b+1):
    if i == 2:
        li.append(2)
        continue
    for j in range(i-1,1,-1):

        if i%j == 0:
            break
        if j == 2:
            li.append(i)
if len(li) > 0 :
    print(sum(li))
    print(min(li))
else:
    print(-1)
