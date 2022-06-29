n, m = map(int, input().split())
li = ['' for i in range(n)]
cnt = 0
result = 0
for i in range(n):
    li[i] = input()
for j in range(n-8+1):
    for k in range(m-8+1):
        cnt_W = 0
        cnt_B =0
        for x in range(j,j+8,2):
            for y in range(k,k+8,2):
                if li[j][k] != li[x][y]:
                    cnt_B += 1
                else:
                    cnt_W += 1

                if li[j][k] == li[x][y+1]:
                    cnt_B += 1
                else:
                    cnt_W += 1

                if li[j][k] == li[x+1][y]:
                    cnt_B += 1
                else:
                    cnt_W += 1

                if li[j][k] != li[x+1][y+1]:
                    cnt_B += 1
                else:
                    cnt_W += 1

        if cnt_W > cnt_B:
            cnt = cnt_B
        else:
            cnt = cnt_W

        if j+k == 0:
            result = cnt
        elif result > cnt:
            result = cnt

print(result)