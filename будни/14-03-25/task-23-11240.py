def f(s, e, c=0):
    if s == e: return 1
    if s > e:  return 0
    if c == 0:
        return f(s + 2, e) + f(s ** 2, e, 1) + f(s * 3, e)
    return f(s + 2, e) + f(s * 3, e)

print(f(2, 64))

# ans -> 55