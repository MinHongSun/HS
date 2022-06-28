data = []
count = 0

while True:
    data.append(list(map(int, input().split())))
    if data[count][0] == data[count][1] == 0:
        break
    count += 1

for i in range(count):
    print(data[i][0] + data[i][1])