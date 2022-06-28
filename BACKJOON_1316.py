n = int(input())
eng = []

for q in range(26):
    eng.append(0)

for i in range(n):
    for q in range(26):
        eng[q] = 0

    n_past = n

    a = input()

    for j in range(len(a)):
        eng[ord(a[j])-97] = eng[ord(a[j])-97] + 1

    for k in range(len(a)):
        if eng[ord(a[k])-97] == 1:
            continue
        else:
            for l in range(1,eng[ord(a[k])-97]):
                if a[k] == a[k+l]:
                    eng[ord(a[k]) - 97] = eng[ord(a[k]) - 97] - 1
                else:
                    n = n - 1
                    break
            if n_past != n:
                n_past = n
                break

print(n)
