n = int(input())
a = []

for i in range(n):
    result = ''
    a = list(map(str, input().split()))
    for j in range(len(a[1])):
        result = result + a[1][j]*int(a[0])
    print(result)