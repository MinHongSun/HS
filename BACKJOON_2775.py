a = int(input())
li = []
for i in range(a):
    n = int(input())
    k = int(input())


    for f in range(k+1):
        li.append(0)

    for b in range(n):
        if b == 0:
            for c in range(1,k+1):
                li[c] = c
                continue
        for d in range(k,0,-1):
            for e in range(d-1,0,-1):
                li[d] = li[d] + li[e]

    print(li[k])





