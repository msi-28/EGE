def f(s, e):
    if s == e: return 1
    if s < e or s == 12: return 0
    return f(s - 2, e) + f(s // 2, e)

print(f(42, 26) * f(26, 1))

# ans -> 51