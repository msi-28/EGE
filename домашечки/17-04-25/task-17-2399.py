with open('17_2399.txt') as file:
    ls = [int(i) for i in file]

summ = sum(sum(map(int, str(i))) for i in ls if i%35 == 0)
ans = []

for i in range(len(ls) - 1):
    n1, n2 = ls[i:i+2]
    c1 = n1 > summ and hex(n2)[-2:] == 'ef' and n2 <= summ
    c2 = n2 > summ and hex(n1)[-2:] == 'ef' and n1 <= summ
    if c1^c2:
        ans.append(n1 + n2)
print(len(ans), min(ans))

# ans -> 15 6410