'''n = int(input())
li = []
for i in range(n):
    li.append(int(input()))

cnt = [0]*10001

for j in range(len(li)):
    cnt[li[j]] += 1

for k in range(1,len(cnt)):
    cnt[k] += cnt[k-1]

result = [0]*len(li)

for l in range(len(li)):
    result[cnt[li[l]]-1] = li[l]
    cnt[li[l]] -= 1

print(result)'''

import sys
n = int(sys.stdin.readline())
result = [0] * 10001

for i in range(n):
    result[int(sys.stdin.readline())] += 1
for j in range(10001):
    for k in range(result[j]):
        print(j)