ls = [int(i) for i in open('17_17873.txt')]

m = min(ls)
ans = []

for i in range(len(ls) - 1):
    num1,num2 = ls[i:i+2]
    if num1 % 16 == m or num2 % 16 == m:
        ans.append(num1 + num2)

print(len(ans), max(ans))

# ans -> 1214 176024