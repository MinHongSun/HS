data = []
rest = []
count = 1

for i in range(10):
    data.append(int(input()))

for j in range(len(data)):
    rest.append(int(data[j]%42))

rest.sort()

for k in range(len(rest)):
    if k == 0:
        continue
    if rest[k] != rest[k-1]:
        count += 1
    else:
        continue

print(count)