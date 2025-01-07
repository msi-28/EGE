with open('17_1993.txt') as file:
    ls = [int(i) for i in file]
cnt = 0
max_sum = -100_000
for i in range(len(ls) - 1):
    sum = ls[i] + ls[i + 1]
    mult = ls[i] * ls[i + 1]
    c1 = sum % 3 == 0
    c2 = sum % 6 != 0
    c3 = abs(mult) % 10 == 8
    if c1 and c2 and c3:
        cnt += 1
        if sum > max_sum:
            max_sum = sum
print(cnt, max_sum)