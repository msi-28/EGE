with open('09_9778.txt') as file:
    ls = [list(map(int, i.split())) for i in file]
cnt = 0
for i in ls:
    cnt += 1
    if [i.count(j) for j in i].count(2) == 2 and [i.count(j) for j in i].count(1) == 4:
        if [j for j in i if i.count(j) > 1][0] >= sum([j for j in i if i.count(j) == 1])/4:
            print(cnt)
            break

# ans -> 34