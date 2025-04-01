def f(x, s):
    if 36 <= x <= 85: return s%2 == 0
    if x > 85: return s%2
    if s == 0: return False
    h = [f(x + 2, s - 1), f(x * 3, s -1)]
    return any(h) if (s - 1)%2 == 0 else all(h)

print('19)', [s for s in range(1, 100) if f(30, s)])
print('19)', [s for s in range(1, 100) if f(32, s)])
print('20)', [s for s in range(1, 10) if f(8, s)])
print('20)', [s for s in range(1, 10) if f(10, s)])
print('21)', [s for s in range(1, 10) if f(6, s)])

# ans:
# 19) Петя Ваня
# 20) Петя Ваня
# 21) Ваня