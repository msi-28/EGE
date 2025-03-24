from functools import lru_cache

@lru_cache(None)
def f(n):
    if n <= 3: return n
    if n > 3: return (n - 2) * f(n - 2)

for i in range(1025):
    f(i)

print((f(1024) + 2 * (f(1022) - f(1021)))//f(1020))

# ans -> 1044403