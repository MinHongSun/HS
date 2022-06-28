data = input().split('-')

result = sum(list(map(int, data[0].split("+"))))
k = []

for i in range(1,len(data)):
    if "+" in data[i]:
        k = list(map(int, (data[i].split("+"))))
        if len(data) == 1:
            result += sum(k)
        else:
            result -= sum(k)
    else:
        result -= int(data[i])

print(result)


