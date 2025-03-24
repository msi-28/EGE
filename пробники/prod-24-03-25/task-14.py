def f(num, q):
    ans = ''
    while num:
        ans += str(num % q)
        num //= q
    return ans[::-1]

ans = []
for x in range(1, 2031):
    num = f(2**2025 + 2**2024 - 2**2021 - x, 4)
    ans.append([num.count('0'), x])

print(max(ans))
# ans -> 1024