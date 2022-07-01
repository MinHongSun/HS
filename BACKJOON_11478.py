li = input()
li2 = []
for i in range(len(li)):
    for j in range(i+1,len(li)+1):
        li2.append(li[i:j])
print(len(set(li2)))