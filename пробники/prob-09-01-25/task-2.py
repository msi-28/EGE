print('x y z w f')

for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = (x or (not y)) and (x != z) and w
                if f:
                    print(x, y, z, w, f)

# ans -> zyxw