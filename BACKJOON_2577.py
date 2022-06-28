data = []
k = []
for i in range(3):
    data.append(int(input()))

result = data[0] * data[1] * data[2]

k = list(map(int, str(result)))

for a in range(10):
    count = 0
    for b in range(len(k)):
        if a == k[b]:
            count += 1
    print(count)