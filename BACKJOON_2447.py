n = int(input())

def rf(i):
    data = []
    result = []
    if i == 3:
        data = ["***", "* *", "***"]
        return data

    k = rf(i//3)
    result = [[0]*i for j in range(i)]
    for x in range(i):
        for y in range(i):
            if x//(i//3) == 1 and y//(i//3) == 1:
                result[x][y] = " "
                print(x, x % (i // 3), y, y % (i // 3), result[x][y])
            else:
                result[x][y] = k[x%(i//3)][y%(i//3)]
                print(x,x%(i//3),y,y%(i//3),result[x][y])

    return result

fin = rf(n)

for x in range(n):
    for y in range(n):
        print(fin[x][y], end="")
    print(end='\n')




