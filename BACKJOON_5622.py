a = list(input())
b = ['','ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ','']
t = 0
for i in range(len(a)):
    for j in range(len(b)):
        if a[i] in b[j]:
            t = t + j + 2
print(t)