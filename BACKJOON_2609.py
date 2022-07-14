li = list(map(int, input().split()))
li.sort()

for i in range(li[0],0,-1):
    if li[0]%i == 0 and li[1]%i == 0:
        print(i)
        break

for j in range(li[1],10000*10000,li[1]):
    if j%li[0] == 0 and j%li[1]==0:
        print(j)
        break
