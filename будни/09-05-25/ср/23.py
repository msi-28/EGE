def f(s, e, c = 0):
    if s == e and c == 0: return 1
    if s > e: return 0
    return f(s + 2, e) + f(s + 5, e) + f(s ** 2, e, 1)

print(f(4, 36))

# ans -> 319