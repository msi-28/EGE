def convert(num, q):
    ans = ''
    while num:
        ans += str(num % q)
        num //= q
    return ans[::-1]

max_N = 0
for N in range(1, 10_000):
    R = oct(N)[2:]
    if N % 2 == 0:
        R = R + max(R)
    else:
        R = R + oct(int(min(R)) * 2)[2:]
    R = int(R, 8)
    if R < 313:
        max_N = N
print(max_N)