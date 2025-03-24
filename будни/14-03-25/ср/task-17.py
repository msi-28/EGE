ls = [int(i) for i in open('17_14952.txt').readlines()]

m = max([i for i in ls if abs(i)%1000 == 121])
ans = []
for i in range(len(ls) - 2):
    num1,num2,num3 = ls[i:i+3]
    c1 = len([j for j in [num1,num2,num3] if len(str(abs(j))) == 4 and abs(j)%2 == 0]) <= 1
    c2 = num1+num2+num3 <= m
    if c1 and c2:
        ans.append(num1+num2+num3)

print(len(ans), max(ans))