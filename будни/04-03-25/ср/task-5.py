def f(num, q):
    ans = ''
    while num:
        ans += str(num%q)
        num //= q
    return ans[::-1]

for N in range(1, 1001):
    R  = f(N, 7)
    if N%2 == 0:
        R = '1' + R + '52'
    else:
        R = R[-1] + R[1:len(R)-1] + R[0] + '15'
    R = f(int(R, 7), 7)
    if len(R) == 4:
        print(N)

# ans -> 721