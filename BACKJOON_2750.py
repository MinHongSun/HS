#시간복잡도o(n^2) 정렬 알고리즘
n = int(input())
li = []
for i in range(n):
    a = int(input())
    li.append(a)

for j in range(n):
    for k in range(j+1,n):
        key = li[j]
        if li[k] < key:
            key = li[k]
            li[k] = li[j]
            li[j] = key


for l in range(n):
    print(li[l])


#sort 함수
n = int(input())
li = []
for i in range(n):
    li.append(int(input()))

li.sort()

for j in range(n):
    print(li[j])