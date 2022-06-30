'''def df(li):
    left = []
    right = []
    result = []
    if len(li) <= 1:
        return li
    for i in range(1,len(li)):
        if li[0] < li[i]:
            right.append(li[i])

        else:
            left.append(li[i])

    result = df(left)
    result.append(li[0])
    result = result + df(right)

    return result

n = int(input())
li = []
result = []
for i in range(n):
    li.append(int(input()))

result = df(li)

for j in range(n):
    print(result[j])'''


import sys

n = int(sys.stdin.readline())
li = []
for i in range(n):
    li.append(int(sys.stdin.readline()))

li.sort()

for j in range(n):
    print(li[j])