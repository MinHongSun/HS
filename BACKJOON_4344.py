n = int(input())
data = []

for i in range(n):
    data = list(map(int, input().split()))
    avg = (sum(data) - data[0])/(len(data)-1)
    cnt = 0
    for j in range(len(data)):
        if j == 0:
            continue
        if data[j] > avg:
            cnt = cnt + 1
    result = (cnt / (len(data)-1))*100
    print(f'{result:.3f}%')


