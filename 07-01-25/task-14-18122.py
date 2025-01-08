for x in range(5555):
    cnt = 0
    num = 5**150 + 5**135 - x
    while num:
        if num % 5 == 4:
            cnt += 1
        num //= 5

    if cnt == 134:
        print(x)