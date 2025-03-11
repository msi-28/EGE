from functools import lru_cache

@lru_cache(None)
def f(n):
    if n < 100: return n**2
    if n > 99 and n%2 == 0: return 0.5*f(n - 1)
    if n > 99 and n%2 != 0: return 2*f(n - 1)

for i in range(16385):
    f(i)

print(1000 * f(16384)//f(7777))

# ans -> 500