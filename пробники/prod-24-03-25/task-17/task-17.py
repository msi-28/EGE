ls = [int(i) for i in open('1706.txt')]
m = min([i for i in ls if abs(i)%100 == 19 and len(str(abs(i))) == 3])**2
ans = []
for i in range(len(ls) - 2):
    num1,num2,num3 = ls[i:i+3]
    c1 = sum([1 for n in [num1,num2,num3] if abs(n)%100 == 19 and len(str(abs(n))) == 5]) >= 1
    c2 = sum([num1,num2,num3]) > m
    if c1 and c2:
        ans.append(sum([num1,num2,num3]))

print(len(ans), min(ans))