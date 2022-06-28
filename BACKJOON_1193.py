n = int(input())

cnt, k = 2, 1

#cnt가 홀수면 분자부터 짝수면 분모부터
if n == 1:
    print("1/1")
else:
    while True:
        if k < n <= k + cnt:
            if cnt%2 == 1:
                print(str(1 + (k + cnt - n))+"/"+str(cnt - (k + cnt - n)))
                break
            else:
                print(str(cnt - (k + cnt - n)) + "/" + str(1 + (k + cnt - n)))
                break
        else:
            k = k + cnt
            cnt = cnt + 1
