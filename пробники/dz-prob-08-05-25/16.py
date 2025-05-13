from functools import lru_cache

@lru_cache(None)
def f(n):
    if n > 3000: return 1
    if n <= 3000 and n%2 == 0: return f(n + 1) - n + 1
    if n <= 3000 and n%2 != 0: return f(n + 2) - 2*n + 2

for i in range(1,500):
    f(i)

# print(2*f(39) -  2 *f(34))