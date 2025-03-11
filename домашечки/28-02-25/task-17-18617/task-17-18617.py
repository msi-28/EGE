ls = [int(i) for i in open('17_18617.txt')]

maxx = max(ls)%3
minn = min(ls)%7
ans = []
for i in range(len(ls) - 1):
    num1,num2 = ls[i:i+2]
    c1 = num1%3 == maxx or num2%3 == maxx
    c2 = num1%7 == minn or num2%7 == minn
    if c1 and c2:
        ans.append(num1 + num2)
print(len(ans), max(ans))

# ans -> 1467 197700