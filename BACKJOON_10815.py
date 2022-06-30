import sys
def df (n,li):
    low, high = 0,len(li)-1
    while low <= high:
        mid = (low+high)//2
        if li[mid] < n:
            low = mid +1
        elif li[mid] > n:
            high = mid -1
        else:
            return 1
    return 0

n = int(sys.stdin.readline())
li_1 = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
li_2 = list(map(int, sys.stdin.readline().split()))

li_1.sort()


for i in range(m):
    print(df(li_2[i],li_1),end=' ')
