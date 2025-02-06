for x in range(1, 2006):
    num = 43**56 + 113**841 - x
    cnt = 0
    num_b = str(num)
    while num:
        if num % 4 == 2:
            cnt += 1
        num //= 4
    for i in num_b:
        if int(i) % 2 == 0:
            num_b = num_b.replace(i, '0')
        else:
            num_b = num_b.replace(i, '1')
    if cnt <= 712 and num_b.count('0') % 2 == 0 and num_b.count('1') % 2 == 0:
        print(x)
