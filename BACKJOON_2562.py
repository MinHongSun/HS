data = []
k = 0
max_value = 0
for i in range(9):
    data.append(int(input()))
    '''if i == 0:
        max_value = data[i]
    else:
        if data[i] > data[i-1]:
            max_value = data[i]
            k = i+1

print(max_value)
print(k)'''

print(max(data))
print(data.index(max(data))+1)
