def f(x):
    return (A%12 == 0) and (530%x == 0) <= ((A%x != 0) <= (170%x != 0))

ox = range(1, 1000)
cnt = 0
for A in ox:
    if all(f(x) for x in ox):
        cnt += 1
print(cnt)

# ans -> 16