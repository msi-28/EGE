from string import printable
alf = printable[:12]
def f(num, q):
    ans = ''
    while num:
        ans += alf[num%q]
        num //= q
    return ans [::-1]

ans = []
for N in range(1, 10000):
    R = f(N, 12)

    if N % 3 == 0:
        R = '1' + R + 'b'
    else:
        R = '2' + R + '0'
    R = int(R, 12)
    if R < 1996:
        ans.append(R)
print(max(ans))

# ans -> 1991