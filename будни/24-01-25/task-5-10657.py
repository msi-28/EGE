def convert(num, q):
    ans = ''
    while num:
        ans += str(num%q)
        num //= q
    return ans[::-1]
ans = 0
for N in range(1, 1000):
    R = convert(N, 3)
    if sum(map(int, R)) % 3 == 0:
        R += '20'
    else:
        R += '10'
    R = int(R, 3)
    if R < 100:
        ans = N
print(ans)