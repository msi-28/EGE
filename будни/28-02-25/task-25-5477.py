from pygame.examples.video import answer


def f(x):
    for i in range(2, int(x**0.5) + 1):
        if x%i == 0:
            return 0
    return 1

cnt = 0
for i in range(600_000, 700_000):
    if i%6 == 0 and f(i-1) and f(i+1):
        print(i-1, i+1)
        cnt += 1
        if cnt == 6:
            break

# ans
# 600071 600073
# 600167 600169
# 600239 600241
# 600317 600319
# 600359 600361
# 600401 600403