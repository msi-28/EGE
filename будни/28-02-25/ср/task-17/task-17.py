ls = [int(i) for i in open('17_12450.txt').readlines()]

m = min([i for i in ls if i % 52 == 0])
ans = []
for i in range(len(ls) - 2):
    num1, num2, num3 = ls[i:i+3]
    if (num1%113 + num2%113 + num3%113) == m :
        ans.append(num1 + num2 + num3)

print(len(ans), max(ans))