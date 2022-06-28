n = int(input())
data = []
result = []

for i in range(n):
    data.append(list(map(int, input().split())))

for i in range(n):
    print("Case #%d: %d" %(i+1,data[i][0]+data[i][1]))