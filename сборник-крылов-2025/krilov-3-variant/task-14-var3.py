for x in range(1,1000):
    num = 6**2025 + 6**25 - x
    cnt = 0
    while num:
        if num % 6 == 0:
            cnt += 1
        num //= 6
    if cnt == 2002:
        print(x)

# ans -> 972