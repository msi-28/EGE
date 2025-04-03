with open('17_12735.txt') as file:
    ls = list(map(int, file.readlines()))

m = max([i for i in ls if i%100 == 9])
ans = []
for i in range(len(ls) - 2):
    num1, num2, num3 = ls[i:i+3]
    c1 = sum([1 for i in [num1, num2, num3] if i%7 == 0]) == 2
    c2 = num1 + num2 + num3 < m
    if c1 and c2:
        ans.append(num1*num2*num3)

print(len(ans), min(ans))
# ans -> 300 8820