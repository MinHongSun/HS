import math

n = list(map(int, input().split()))

print(math.ceil((n[2]-n[0])/(n[0]-n[1]))+1)

'''k = a*n - b*n +a

k = (a-b)n + a

k-a = (a-b)n

(k-a)/(a-b)=n'''