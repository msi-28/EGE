from sys import setrecursionlimit
setrecursionlimit(3000)
def f(n):
    if n == 1: return 1
    if n > 1: return (n - 1)*f(n-1)
print((f(2024) + 2*f(2023))//f(2022))
# ans -> 4094550