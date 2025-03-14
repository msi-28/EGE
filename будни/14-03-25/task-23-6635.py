def f(s, c):
    if s < 0 and c == 13: return [s]
    if c > 13: return []
    return f(s - 3, c+1) + f(s * (-3), c+1)

print(len(set(f(333, 0))))

# ans -> 2224