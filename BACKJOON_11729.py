#1단계 n-1개 만큼 b번에 도착
#2단계 n개째를 c번에 도착
#3단계 n-1를 다시 c번에 도착

def df(n, start, end):
    if n == 1:
        print(start,end)
        return

    df(n-1,start,6-start-end)
    print(start,end)
    df(n-1,6-start-end,end)

n = int(input())
print(2*n-1)
df(n,1,3)
