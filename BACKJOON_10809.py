m = str(input())
for i in range(26):
    c = chr(97+i)
    a = -1
    for j in range(len(m)):
        if c == m[j]:
            a = j
            break
    print(a)

