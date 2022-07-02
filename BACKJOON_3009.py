sq = []

for _ in range(3):
    sq.append(list(map(int, input().split())))

if sq[0][0] == sq[1][0]:
    x = sq[2][0]
elif sq[1][0] == sq[2][0]:
    x = sq[0][0]
else:
    x = sq[1][0]

if sq[0][1] == sq[1][1]:
    y = sq[2][1]
elif sq[1][1] == sq[2][1]:
    y = sq[0][1]
else:
    y = sq[1][1]

print(x,y)