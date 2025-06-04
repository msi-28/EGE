with open('9_21408.txt') as file:
    arr = [list(map(int, i.split())) for i in file]

cnt = 0
for ls in arr:
    rep = [i for i in ls if ls.count(i) == 3]
    not_rep = [i for i in ls if ls.count(i) == 1]
    if len(rep) == 6 and len(not_rep) == 1:
        if max(rep) > not_rep[0]:
            cnt += 1
print(cnt)
# ans -> 1