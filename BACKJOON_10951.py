data = []
count = 0
n = int(input())
while True:
    try:
        for i in range(n):
            data.append(list(map(int, input().split())))
            print(data[i][0] + data[i][1])
            count += 1
    except:
        break
