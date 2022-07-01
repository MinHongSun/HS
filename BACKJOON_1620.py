import sys
n, m = map(int, sys.stdin.readline().split())
li = {}
dic = {}

for i in range(n):
    li[i] = sys.stdin.readline()
for j in range (n):
    dic[li[j]] = j

for _ in range(m):
    dap = sys.stdin.readline()
    try:
        print(li[int(dap)-1].strip())
        pass
    except:
        print(int(dic[dap])+1)