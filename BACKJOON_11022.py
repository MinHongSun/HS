n = int(input())
data = []

for i in range(n):
    data.append(list(map(int, input().split())))

for i in range(n):
    print("Case #%d: %d + %d = %d" %(i+1, data[i][0], data[i][1], data[i][0]+data[i][1]))