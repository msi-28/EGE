def f(s,e):
    if s > e: return 0
    if s == e: return 1
    return f(s + 2, e) + f(s * 3, e) + f(s * 2, e)

print(f(13, 15) * f(17, 45))
print(f(13, 45))
print(f(13, 16), f(16, 45))