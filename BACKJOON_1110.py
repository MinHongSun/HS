n = int(input())
count = 0
i = n
while True:
    k = i%10 + i//10
    i = (i%10)*10 + k%10
    count += 1
    if i == n:
        break

print(count)