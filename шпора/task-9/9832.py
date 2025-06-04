with open('9_9832.txt') as file:
    arr = [list(map(int, i.split())) for i in file]

for ls in arr:
    rep = [i for i in ls if ls.count(i) == 2]
    not_rep = [i for i in ls if ls.count(i) == 1]
    if len(set(rep)) == 2 and len(not_rep)==3:
        if ls.count(max(ls)) == 1:
            print(sum(ls))
            break

# ans -> 261