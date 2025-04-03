def f(x):
    ans = set()
    for i in range(2, int(x**0.5) + 1):
        if x%i == 0:
            ans |= {x//i, i}

    if ans:
        return sum(ans)
    return 0
cnt = 0
for i in range(1_273_547, 2_000_000):
    if f(f(i)%100_000) == 0 and f(i) != 0:
        print(i, f(i))
        cnt += 1
        if cnt == 5:
            break

# ans:
# 1273566 1637537
# 1273570 1139869
# 1273578 1287317
# 1273582 651769
# 1273590 2225609