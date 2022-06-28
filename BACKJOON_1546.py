n = int(input())
data = list(map(int, input().split()))
max_data = max(data)
new_data = [0]*n

for i in range(n):
    new_data[i] = data[i]/max_data*100


print(sum(new_data)/n)