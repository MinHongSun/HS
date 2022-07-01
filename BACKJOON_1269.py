n, m = map(int, input().split())
li1 = list(map(int, input().split()))
li2 = list(map(int, input().split()))

print(len(set(li1)-set(li2))+len(set(li2)-set(li1)))