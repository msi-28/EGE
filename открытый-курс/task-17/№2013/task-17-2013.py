with open('17_2013.txt') as file:
    ls = [int(i) for i in file]

cnt = 0
min_num = 20_000
for i in ls:
    c1 = i % 10 == 2 or i % 10 == 7
    c2 = i % 3 == 0
    c3 = i % 11 == 0
    if c1 and c2 and c3:
        cnt += 1
        if i < min_num:
            min_num = i
print(cnt, min_num)