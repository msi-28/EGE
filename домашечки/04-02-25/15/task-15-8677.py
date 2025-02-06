from itertools import combinations as cb

def f(x):
    B = 80 <= x <= 100
    return (x % 17 == 0) <= ((not B) or (A < x + 30))

ans = []
for A in range(1, 1000):
    if all(f(x) for x in range(1, 1000)):
        ans.append(A)
print(max(ans))

# ans -> 114