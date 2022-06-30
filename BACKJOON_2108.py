import sys
n = int(sys.stdin.readline())

li = []
cnt = 0
for _ in range(n):
    li.append(int(sys.stdin.readline()))

li.sort()

avg = round(sum(li)/len(li))
mid = li[int(len(li)/2)]

a = [0]*8001

for i in range(len(li)):
    a[li[i]+4000] += 1

if a.count(max(a)) > 1 :
    a[a.index((max(a)))] -= max(a)
    cnt = a.index(max(a))-4000
else:
    cnt = a.index(max(a))-4000

rng = max(li) - min(li)

print(avg)
print(mid)
print(cnt)
print(rng)