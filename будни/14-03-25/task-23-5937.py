def f(s, e, c=0):
    if s == e and c <= 15: return 1
    if s > e: return 0
    c += not(s%2)
    return f(s + 2, e, c) + f(s + 3, e, c) + f(s * 2 + 1, e, c)

print(f(1, 55))
# ans -> 4197234