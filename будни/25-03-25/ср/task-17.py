from itertools import combinations

with open('17 (2)_7718.txt') as file:
    ls = [int(i) for i in file]

ans = []
for num1, num2 in combinations(ls, 2):
    c1 = (num1 + num2) % 18 == 0
    c2 = (num1 * num2) % 18 == 0
    if c1 ^ c2:
        ans.append(num1+num2)

print(len(ans), max(ans))