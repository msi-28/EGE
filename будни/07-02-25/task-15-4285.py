from itertools import combinations as cb

def f(x):
    P = 25 <= x <= 240
    Q = 175 <= x <= 300
    R = 270 <= x <= 340
    A = A1 <= x <= A2
    return (Q <= P) or ((not A) <= R)

line = [25, 175, 240, 270, 300, 340]
ans = []
for A1, A2 in cb(line,2):
    if all(f(x) for x in line):
        ans.append(A2 - A1)
print(min(ans))

# ans -> 30