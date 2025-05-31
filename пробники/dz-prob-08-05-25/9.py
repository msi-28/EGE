with open('9_18134.txt') as file:
    data = [list(map(int, i.split())) for i in file]
cnt = 0
for ls in data:
    n1, n2, n3, n4, n5, n6 = ls
    rep = [i for i in ls if ls.count(i) == 2]
    disrep = [i for i in ls if ls.count(i) == 1]
    if len(rep) == 4 and len(disrep) == 2:
        if max(rep) ** 2 > disrep[0] * disrep[1]:
            cnt += 1
print(cnt)