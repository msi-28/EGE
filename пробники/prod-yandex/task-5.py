ans = []
for N in range(26, 1000):
    R = bin(N)[2:]
    if N % 2 == 0:
        R = '10' + R[2:] + '1'
    else:
        R = R[:-2] + '10'

    R = int(R, 2)
    ans.append(R)

print(min(ans))

# ans -> 26