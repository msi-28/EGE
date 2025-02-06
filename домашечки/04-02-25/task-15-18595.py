from itertools import combinations as cb

from openpyxl.drawing.geometry import AdjPoint2D


def f(x):
    C = 48 <= x <= 94
    J = 83 <= x <= 100
    A = A1 <= x <= A2
    return (not C and (not J)) <= (not A)

ans = []
line = [x for x in range(40, 110)]
for A1, A2 in cb(line, 2):
    if all(f(x) for x in line):
        ans.append(A2 - A1)
print(max(ans))

# ans -> 52