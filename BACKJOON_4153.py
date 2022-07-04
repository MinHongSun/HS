

while True:
    li = list(map(int, input().split()))
    li.sort()

    if li[0] == li[1] == li[0] == 0:
        break
    elif li[2]**2 == li[0]**2 + li[1]**2:
        print("right")
    else:
        print("wrong")
