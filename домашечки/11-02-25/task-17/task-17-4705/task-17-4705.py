ls = [int(i) for i in open('17_4705.txt')]

ans = []
m =  max([i for i in ls if abs(i)%10 == 3])
for i in range(len(ls) - 1):
    num1,num2 = ls[i:i+2]
    c1 = (abs(num1) % 10 == 3) ^ (abs(num2) % 10 == 3)
    c2 = (num1**2 + num2**2) >= m**2
    if c1 and c2:
        ans.append(num1**2 + num2**2)
print(len(ans), max(ans))

# ans -> 180 190360573