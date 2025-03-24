from itertools import groupby

with open('26_17643.txt') as file:
    N = int(file.readline())
    products = [list(map(int, i.split())) for i in file]

sr = sum([i[1] for i in products])/len(products)
expensive = sorted([i for i in products if i[1] > sr])
max_stat = 0
for art, val in groupby(expensive, lambda x: x[0]):
    val = list(val)
    cnt = 0
    for j in range(len(val)):
        if val[j][2] == 0:
            cnt += 1
    if cnt == 51 and val[0][1] == 856:
        cnt_stat = 0
        for j in range(len(val)):
            if val[j][2] == 1:
                cnt_stat += 1
        print(art, cnt * val[0][1], cnt_stat)

# ans ->  43656 36