with open('17_2015.txt') as file:
    ls = [int(i) for i in file]

cnt = 0
min_num = 20_000
max_num = 0
for i in ls:
    c1 = i % 10 == 5 or i % 10 == 7
    c2 = i % 9 != 0
    c3 = i % 11 != 0
    if c1 and c2 and c3:
        cnt += 1
        if i < min_num:
            min_num = i
        if i > max_num:
            max_num = i
print(cnt, min_num + max_num)