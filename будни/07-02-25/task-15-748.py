from itertools import combinations as cb

def f(x):
    P = 44 <= x <= 49
    Q = 28 <= x <= 53
    A = A1 <= x <= A2
    return (A <= P) or Q

ans = []
line = [x for x in range(20, 60)]
for A1, A2 in cb(line, 2):
    if all(f(x) for x in line):
        ans.append(A2 - A1)
print(max(ans))

# ans  -> 25