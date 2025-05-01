cnt = 0
for N in range(1, 10_000):
    R  = hex(N)[2:]
    if R.count('b')%2 == 0:
        R = '1' + R
    else:
        R += '1'
    R = int(R, 16)
    if len(str(R)) == 2:
        cnt += 1
        print(N, R)
print(cnt)

# ans -> 14