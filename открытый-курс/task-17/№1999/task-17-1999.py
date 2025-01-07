with open('17_1999.txt') as file:
    ls = [int(i) for i in file]

cnt = 0
min_arithmetic_mean = 100_000_000
for i in range(len(ls) - 2):
    arithmetic_mean = (ls[i] + ls[i + 1] + ls[i + 2])/3
    c1 = ls[i] % 12 == 0 or ls[i + 1] % 12 == 0 or ls[i + 2] % 12 == 0
    c2 = ls[i] % 3 == 0 and ls[i + 1] % 3 == 0 and ls[i + 2] % 3 == 0
    if c1 and c2:
        cnt += 1
        if arithmetic_mean < min_arithmetic_mean:
            min_arithmetic_mean = arithmetic_mean
print(cnt, min_arithmetic_mean)