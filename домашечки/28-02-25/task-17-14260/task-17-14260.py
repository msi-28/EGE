ls = [int(i) for i in open('17_14260.txt')]

minn = min([i for i in ls if i > 0 and len(str(abs(i))) == 4 and str(i)[-1] == str(i)[-2]])
ans = []
for i in range(len(ls) - 2):
    num1, num2, num3 = ls[i:i+3]
    c1 = [len(str(abs(i))) for i in [num1,num2,num3]] == [3,3,3]
    c2 = (num1 + num2 + num3) > minn
    if c1 and c2:
        ans.append(num1+num2+num3)
print(len(ans), max(ans))

# ans -> 8 1958