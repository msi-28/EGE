with open('09_17550.txt') as file:
    arr = [list(map(int, i.split())) for i in file]

cnt = 0
for ls in arr:
    rep = [i for i in ls if ls.count(i) == 3]
    not_rep = [i for i in ls if ls.count(i) == 1]
    if len(rep) == 3 and len(not_rep) == 3:
        if sum(rep)**2 > sum(not_rep)**2:
            cnt += 1

print(cnt)
# asn -> 19