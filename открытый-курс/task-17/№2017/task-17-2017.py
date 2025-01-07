with open('17_2017.txt') as file:
    ls = [int(i) for i in file]

cnt = 0
sum = 0
for i in ls:
    c1 = hex(i)[2:][-1:] == 'b'
    c2 = i % 7 == 0
    c3 = i % 6 != 0
    c4 = i % 13 != 0
    c5  = i % 19 != 0
    if c1 and c2 and c3 and c4 and c5:
        cnt += 1
        sum += i
print(sum, cnt)