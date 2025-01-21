def f(x,y):
    return (x < A) or (y < A) or (x + y*2 > 50)

for A in range(1, 1000):
    if all(f(x,y) for x in range(1, 1000) for y in range(1, 1000)):
        print(A)
        break

# ans -> 17