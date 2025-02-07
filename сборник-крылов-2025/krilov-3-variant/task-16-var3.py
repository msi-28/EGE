from functools import lru_cache

@lru_cache(None)
def f(n):
    if n == 1: return 1
    if n > 1: return n + f(n - 1)

for n in range(-10000, 30000):
    f(n)
print(f(3000) - f(2000))

# ans -> 2500500