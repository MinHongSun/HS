a = input()
b = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
cnt = 0

for i in range(len(b)):
    if b[i] in a:
        #cnt = cnt + a.count(b[i])
        a = a.replace(b[i], "0")



print(len(a))