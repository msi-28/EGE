def f(n, q):
    ans = ''
    while n:
        ans += str(n%q)
        n //= q
    return ans[::-1]

for N in range(1, 1000):
    R = f(N,3)
    if N%3 == 0:
        R = '1' + R + '02'
    else:
        R = R + f(N%3 * 4, 3)
    R = int(R, 3)
    if R < 199:
        print(N)