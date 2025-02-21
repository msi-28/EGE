def f(num, q):
    ans = ''
    while num: ans += str(num%q); num //= q
    return ans[::-1]
ans = []
for N in range(1, 1000):
    R = f(N, 4)
    if N % 4 == 0:
        R += R[-2:]
    else:
        R += f(N%4 * 2, 4)
    R = int(R, 4)
    if R < 261:
        ans.append(N)
print(max(ans))

# asn -> 61