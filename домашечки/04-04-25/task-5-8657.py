def f(num, q):
    ans = ''
    while num:
        ans += str(num%q)
        num //= q
    return ans[::-1]

for N in range(1, 1000):
    R = f(N,3)
    if N%5 == 0:
        R += R[:-3]
    else:
        R += f(N%5 * 5,3)
    R = int(R, 3)
    if R <5496:
        print(N)

# ans -> 606