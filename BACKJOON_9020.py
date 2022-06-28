def sosu(m,n):

    li = [True] * (n+1)
    result = []
    li[0] = False
    li[1] = False

    for i in range(2, int(n**0.5)+1):

        if li[i] == False:
            continue
        else:
            for j in range(i*2, n+1, i):
                li[j] = False

    for l in range(len(li)):
        if li[l] == True and l >= m:
            result.append(l)

    return result

n = int(input())

for i in range(n):
    m = int(input())
    s = sosu(0,m)
    for j in range(int(m / 2) ,1,-1):
        if j in s and m - j in s:
            print(j, m-j)
            break




'''def sosu(max):
    primes = [True] * (max + 1)
    primes[0] = False
    primes[1] = False
    for i in range(2, int(max**0.5) + 1):
        if primes[i]:
            for j in range(i * 2, max + 1, i):
                primes[j] = False
    return primes

isPrimes = sosu(10000)
n = int(input())
for i in range(n):
    m = int(input())
    for j in range(m // 2, 1, -1):
        if isPrimes[j] and isPrimes[m - j]:
            print(j, m - j)
            break'''