def f(n, q):
    ans = ''
    while n:
        ans += str(n%q)
        n //= q
    return ans[::-1]

ans = []
for N in range(1, 1000):
    R = f(N, 3)
    if N%3 == 0:
        R += R[-2:]
    else:
        R += f(N%3*5, 3)
    R = int(R, 3)
    if R > 133:
        ans.append(R)
print(min(ans))
# ans -> 141