import sys

n, m = map(int, sys.stdin.readline().split())
dic1=set()
dic2=set()
dic3=[]
for _ in range(n):
    dic1.add(sys.stdin.readline())
for _ in range(m):
    dic2.add(sys.stdin.readline())
dic3=sorted(list(dic1 & dic2))

print(len(dic3))
dic3.sort()
for j in range(len(dic3)):
    print(dic3[j].rstrip())








