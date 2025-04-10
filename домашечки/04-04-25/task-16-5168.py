from functools import lru_cache

@lru_cache(None)
def f(n):
    if n >= 10_000: return n
    if n < 10_000 and n%2 == 0: return f(n+1) + n**2 - 3*(n - 1)
    if n < 10_000 and n%2 != 0: return f(n+2) + 5*n - (n - 1)

for i in range(1, 10_001):
    f(i)
print(f(90) - f(99))