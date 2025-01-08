def f(s, e):
    if s < e: return 0
    if s == e: return 1
    return f(s - 2, e) + f(s // 2, e)

print(f(50, 11) * f(11, 2))