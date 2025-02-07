def convert(num, q):
    ans = ''
    while num:
        ans += str(num % q)
        num //= q
    return ans[::-1]

ans = []
for N in range(1, 1000):
    R = convert(N, 3)
    if sum(map(int, R)) % 3 == 0:
        R += '212'
    else:
        R += convert(sum(map(int, R)) * 2, 3)
    R = int(R, 3)
    if R > 490:
        ans.append(R)
print(min(ans))