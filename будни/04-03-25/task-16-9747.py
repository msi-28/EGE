from functools import lru_cache

@lru_cache(None)
def f(n):
    if n < 11: return n
    return n + f(n - 1)

for i in range(2025):
    f(i)
print(f(2024) - f(2021))

# ans -> 6069