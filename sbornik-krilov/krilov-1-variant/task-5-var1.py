for N in range(1, 10_000):
    R = bin(N)[2:]
    if N % 2 == 0:
        R  = R.replace('1', '11')
    else:
        R  = R.replace('0', '00')
    R = int(R, 2)
    if R > 70:
        print(N)
        break

# 14 <- ответ