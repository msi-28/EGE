def f(num, q):
    ans = ''
    while num:
        ans += str(num % q)
        num //= q
    return ans[::-1]

ans = []
for N in range(1, 1000):
    R = f(N, 3)
    if sum(map(int, R)) % 2 == 0:
        R = '1' + R + '2'
    else:
        R = '2' + R + '0'

    R = int(R, 3)
    if R > 100:
        ans.append(R)

print(min(ans))

# ans -> 113