def convert(num, q):
    ans = ''
    while num:
        ans += str(num%q)
        num //= q
    return ans[::-1]

ls = []
for N in range(1, 10_000):
    R = convert(N, 3)
    if N%3 == 0:
        R = R + R[-2:]
    else:
        R = R + convert(sum(map(int, R)), 3)
    R = int(R, 3)
    if R > 220 and R % 2 == 0:
        ls.append(R)
print(min(ls))
