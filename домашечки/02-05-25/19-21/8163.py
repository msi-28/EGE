def f19(x, s):
    if x >= 348: return s%2 == 0
    if s == 0: return False
    h = [f19(x + 2, s - 1),
         f19(x + 4, s - 1),
         f19(x * 3, s - 1)]
    return any(h)

def f(x, s):
    if x >= 348: return s%2 == 0
    if s == 0: return False
    h = [f19(x + 2, s - 1),
         f19(x + 4, s - 1),
         f19(x * 3, s - 1)]
    return any(h) if (s - 1)%2 == 0 else all(h)

print('19)', [s for s in range(1, 348) if f19(s, 2) and not(f19(s, 1))])
print('20)', [s for s in range(1, 348) if f(s, 3) and not(f(s, 1))])
print('21)', [s for s in range(1, 348) if f(s, 4) and not(f(s, 2))])

# ans:
# 19) 39
# 20) 13 14
# 21) 11