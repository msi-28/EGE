with open('17_1994.txt') as file:
    ls = [int(i) for i in file]
cnt = 0
min_mult = 100_000_000
for i in range(len(ls) - 1):
    sum = ls[i] + ls[i + 1]
    mult = ls[i] * ls[i + 1]
    c1 = mult > 0
    c2 = sum % 7 == 0
    if c1 and c2:
        cnt += 1
        if mult < min_mult:
            min_mult = mult
print(cnt, min_mult)