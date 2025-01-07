with open('17_2016.txt') as file:
    ls = [int(i) for i in file]
max_num = 0
min_num = 20_000
cnt = 0

for i in ls:
    c1 = i % 13 == 7
    c2 = i % 11 != 0
    c3 = i % 7 != 0
    if c1 and c2 and c3:
        cnt += 1
        if i < min_num:
            min_num = i
        if i > max_num:
            max_num = i
print(max_num - min_num, cnt)