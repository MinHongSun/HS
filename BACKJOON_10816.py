import sys
from collections import Counter

n = int(sys.stdin.readline())
li_1 = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
li_2 = list(map(int, sys.stdin.readline().split()))

counter = Counter(li_1)

for i in range(m):

    print(counter[li_2[i]], end=' ')