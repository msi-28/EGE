from pygame.examples.video import answer


def f(x):
    for i in range(2, int(x**0.5) + 1):
        if x%i == 0:
            return 0
    return 1
cnt = 0
for i in range(194441, 196500+1):
    if f(i) and i%100 == 93:
        cnt += 1
        print(cnt, i)

# ans
# 1 195193
# 2 195493
# 3 195593
# 4 195893
# 5 196193