ans = set()
for N in range(100, 1000):
    R = bin(N)[2:]
    R = R.replace('0', '')
    R = int(R, 2)
    ans |= {R}
print(len(ans))