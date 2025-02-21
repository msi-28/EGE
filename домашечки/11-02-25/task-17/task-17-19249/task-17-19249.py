ls = [int(i) for i in open('17_19249.txt')]

m = max([i for i in ls if abs(i) % 100 == 43])
ans = []

for i in range(len(ls) - 2):
    num1, num2, num3 = ls[i:i+3]
    c1 = ((len(str(abs(num1))) == 5 and abs(num1) % 100 == 43)
          or (len(str(abs(num2))) == 5 and abs(num2) % 100 == 43)
          or (len(str(abs(num3))) == 5 and abs(num3) % 100 == 43))
    c2 = (num1**2 + num2**2 + num3**2) <= m**2
    if c1 and c2:
        ans.append(num1**2 + num2**2 + num3**2)

print(len(ans), min(ans))

# ans -> 92 838850571
