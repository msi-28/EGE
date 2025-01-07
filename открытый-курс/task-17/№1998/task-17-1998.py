with open('17_1998.txt') as file:
    ls = [int(i) for i in file]
cnt = 0
max_sum = -100_000_000
for i in range(len(ls) - 2):
    sum = ls[i] + ls[i + 1] + ls[i + 2]
    mult = ls[i] * ls[i + 1] * ls[i + 2]
    c1 = abs(mult) % 7 == 0
    c2 = abs(sum) % 10 == 5
    if c1 and c2:
        cnt += 1
        if sum > max_sum:
            max_sum = sum
print(cnt, max_sum)