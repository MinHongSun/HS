n = int(input())
li = []
dx,dy =[],[]
cnt = [0]*5
for l in range(6):
    li.append(list(map(int,input().split())))
    cnt[li[l][0]] += 1
for i in range(6):
    if int(li[i][0]) <= 2 :
        dx.append(li[i][1])
    else:
        dy.append((li[i][1]))

if (cnt[4] == 1 and cnt[2] == 1) or (cnt[3] == 1 and cnt[1] == 1):
    x = dx[dx.index(max(dx)) - 2]
    y = dy[dy.index(max(dy)) - 1]
else:
    x = dx[dx.index(max(dx)) - 1]
    y = dy[dy.index(max(dy)) - 2]



s_1 = int(max(dx))*int(max(dy))*n
s_2 = int(x)*int(y)*n
print(s_1-s_2)




'''4 = 1 2 = 1
x = max - 2
y = max - 1

3 = 1 2 = 1
x = max - 1
y = max - 2

3 = 1 1 = 1
x = max - 2
y = max - 1

4 = 1 1 = 1
x = max - 1
y = max - 2
'''
