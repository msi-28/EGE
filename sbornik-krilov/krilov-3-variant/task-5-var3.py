for N in range(1,10_000):
    R = bin(N)[2:]
    if N % 4 == 0:
        R += R
    else:
        R += R[::-1]
    R = int(R,2)
    if R >= 544:
        print(N)
        break
# ans -> 17