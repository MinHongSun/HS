def df():
    cnt = 0
    n = int(input())
    for i in range(1,n+1):
        if i < 100:
            cnt = cnt + 1
        if i >= 100 :
            str_i = str(i)
            if int(str_i[2]) - int(str_i[1]) == int(str_i[1]) - int(str_i[0]):
                cnt = cnt + 1
    print(cnt)

df()