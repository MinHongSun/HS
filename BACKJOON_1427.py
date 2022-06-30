n = int(input())
li = list(map(int, str(n)))
li.sort(reverse=True)
a = ""
for i in range(len(li)):
    a += str(li[i])
print(a)

