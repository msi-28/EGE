def tr(n, m, k):
    if max(n,m,k) < n+m+k - max(n,m,k):
        return True
    return False

def f(x):
    return tr(A, 7, x) <= ((max(x + 5, 14) <= 27) == (not(tr(36, 21, x))))

r = range(1, 1000)
ans = 0
for A in r:
    if all(f(x) for x in r):
        ans = A
print(ans)

# ans -> 50