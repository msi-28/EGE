def convert(num, q):
    ans = ''
    while num:
        ans += str(num % q)
        num //= q
    return ans[::-1]

ans = 0
for N in range(1, 10_000):
    R = convert(N, 4)
    if N % 4 == 0:
        R = '2' + R + '03'
    else:
        R = R + convert((N % 4) * 5, 4)
    if int(R, 4) < 567:
        ans = N
print(ans)