with open('17_18932.txt') as file:
    ls = [int(i) for i in file]

cnt_ch = len([i for i in ls if i % 2 == 0])
ans = []
for i in range(len(ls) - 1):
    num1, num2 = [ls[i], ls[i+1]]
    c1 = num1 > 0 or num2 > 0
    c2 = num1 + num2 < cnt_ch
    if c1 and c2:
        ans.append(num1**2 + num2**2)
print(len(ans), max(ans))