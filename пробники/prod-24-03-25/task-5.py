def f(num, q):
    ans = ''
    while num:
        ans += str(num % q)
        num //= q
    return ans[::-1]


ans = []
for N in range(1, 10000):
    R = f(N, 4)
    if sum(map(int, R)) % 2 == 0:
        R = R + R[-2:]
    else:
        R = '2' + R + '0'

    R = int(R, 4)
    if R > 120 and R % 2 == 0:
        ans.append(R)

print(min(ans))
# ans -> 136