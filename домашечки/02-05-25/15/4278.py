def f(x):
    return (A%12 == 0) and ((530%x == 0) <= ((A%x != 0) <= (170%x != 0)))

cnt = 0
for A in range(1, 1000):
    if all(f(x) for x in range(1, 10000)):
        cnt += 1
print(cnt)

# ans -> 16