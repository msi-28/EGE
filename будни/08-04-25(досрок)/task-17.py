with open('17.txt') as file:
    ls = [int(i) for i in file]
ans = []
s = sum([i for i in ls if i < 0])
for i in range(len(ls) - 2):
    num1, num2, num3 = ls[i:i+3]
    if max([num1, num2, num3]) * min([num1, num2, num3]) > s:
        ans.append(abs(num1+num2+num3))

print(len(ans), max(ans))

# ans -> 10007 28854