ans = 0
for x in range(1, 5769):
    num = 9**2025 + 9**1000 - x
    cnt = 0
    while num:
        if num % 9 == 0:
            cnt += 1
        num //= 9
    if cnt == 1026:
        ans = x
print(ans)

# 5768 <- ответ