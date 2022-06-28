'''def sosu(m,n):
    li = []
    for i in range(m,n+1):
        if i == 1:
            continue

        for j in range(2,int(i**0.5)+1):
            if i%j == 0:
                break
        else:
                li.append(i)
    return (li)

m,n = map(int, input().split())

sosu = sosu(m,n)

for a in range(len(sosu)):
    print(sosu[a])'''



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


m ,n = map(int, input().split())
s = sosu(m,n)

for a in range(len(s)):
    print(s[a])


