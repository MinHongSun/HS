n = int(input())

cnt = 1
room_num = 1

while True:
    if n > room_num:
        room_num = (cnt * 6) + room_num
        cnt = cnt + 1

    else:
        break

print(cnt)

