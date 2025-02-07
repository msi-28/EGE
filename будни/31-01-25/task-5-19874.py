def convert(num, q):
    ans = ''
    while num:
        ans += str(num % q)
        num //= q
    return ans[::-1]

ans = []
for N in range(10, 1000):
    R = convert(N, 3)
    if N % 4 == 0:
        R += R[-3:]
    else:
        R = '1' + R + '20'
    R = int(R, 3)
    if R > 423:
        ans.append(R)
print(min(ans))

# ans -> 438