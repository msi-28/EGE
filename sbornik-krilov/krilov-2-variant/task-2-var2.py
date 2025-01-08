print('z y w x f')

for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                f = int((y <= z) and (w == (x <= y)) and (not(x)))
                if f:
                    print(z, y, w, x, f)

# yzwx <- ответ