a = input().upper()
b = sorted(a)
c = []
for i in range(26):
    c.append(0)
    for j in range(len(b)):
        if chr(i+65) == b[j]:
            c[i] = c[i] + 1


if c.count(max(c)) > 1:
    print("?")
else:
    print(chr(c.index(max(c))+65))
