ls = [int(i) for i in open('17_18582.txt')]

ans = []
m = abs(min(ls))%10
for i in range(len(ls) - 2):
    num1, num2, num3 = ls[i:i+3]
    c1 = ((num1 < 0) + (num2 < 0) + (num3 < 0)) > ((num1 > 0) + (num2 > 0) + (num3 > 0))
    c2 = abs(num1 + num2 + num3)%10 == m
    if c1 and c2:
        ans.append(abs(num1 + num2 + num3))
print(len(ans), max(ans))

# 440 210834