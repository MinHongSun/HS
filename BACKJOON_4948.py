def sosu(m,n):
    li = []
    result = []
    for i in range(0, n+1):
        li.append(True)

    for j in range(0, int((n+1)**0.5)+1):
        if j == 0 or j == 1:
            li[j] = False
            continue
        elif li[j] == False:
            continue
        for k in range(j+j, n+1, j):
            li[k] = False

    for l in range(len(li)):
        if l == 1:
            continue
        if li[l] == True and l >=m:
            #print(l)
            result.append(l)
    return result

while True:
    n = int(input())
    if n == 0:
        break
    sosu_li = sosu(n+1,n*2)

    print(len(sosu_li))











'''li = []
while True:
    n = int(input())
    if n == 0:
        break
    cnt = 0
    for i in range(n+1, n*2):
        if i == 1:
            continue

        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                break
        else:
            print(i)

    print(cnt)'''
