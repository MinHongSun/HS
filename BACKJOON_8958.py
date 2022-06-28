n = int(input())
data = []
result = []
for i in range(n):
    data.append(list(input()))
    result.append(0)



for j in range(n):
    a = 0
    for k in range(len(data[j])):
        if data[j][k] == "O":
            a += 1
            result[j] += int(a)
        elif data[j][k] == "X":
            a = 0

    print(result[j])


