ans = []
for N in range(1, 1000):
    R = bin(N)[2:]
    if N%2 == 0:
        R = '1' + R + '0'
    else:
        R = '11' + R + '11'
    R = int(R, 2)
    if R > 52:
        ans.append(R)
print(min(ans))

# ans -> 56