def f(x):
    ans = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x%i == 0:
            ans |= {i, x//i}
    if ans:
        return sum(ans)//len(ans)
    return 0

cnt = 0
for i in range(700_000, 1, -1):
    if f(i)%1000 == 313:
        print(i, f(i))
        cnt += 1
        if cnt == 7:
            break

# ans:
# 698196 43313
# 697664 31313
# 696525 22313
# 695940 33313
# 695606 31313
# 695533 18313
# 695526 28313