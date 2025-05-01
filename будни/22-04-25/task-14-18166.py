m = 0
ans = 0
for x in range(2, 2026):
    num = 5**2025 + 5**200 - x
    cnt = 0
    while num:
        if num%5 == 4:
            cnt += 1
        num //= 5
    if cnt > m:
        ans = x
print(ans)