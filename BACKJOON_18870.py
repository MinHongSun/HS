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
            return mid
    return 0


n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))

a = list(dict.fromkeys(li))
a.sort()

for j in range(len(li)):
    print(df(li[j],a), end=' ')