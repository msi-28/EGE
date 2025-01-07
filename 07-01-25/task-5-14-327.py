def convert(num, q):
    ans = ''
    while num:
        ans += str(num % q)
        num //= q
    return ans[::-1]

ans = 0
for N in range(9, 10):
    R = convert(N, 8)
    if N % 2 == 0:
        R = R + max(R)
    else:
        R = R + convert(int(min(R)) * 2, 8)
    R = int(R, 8)
    print(N, R)
#     if R < 313:
#         ans = N
# print(ans)