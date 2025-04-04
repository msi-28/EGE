with open('9_9740.txt') as file:
    ls = [list(map(int, i.split())) for i in file]

cnt = 0
for i in ls:
    if [i.count(j) for j in i].count(3) == 3 and [i.count(j) for j in i].count(1) == 4:
        if sum([j for j in i if i.count(j) == 1])/4 <= [j for j in i if i.count(j) > 1][0]:
            cnt += 1
print(cnt)

# ans -> 36