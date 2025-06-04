with open('09_9778.txt') as file:
    arr = [list(map(int, i.split())) for i in file]
cnt = 0
for ls in arr:
    rep = [i for i in ls if ls.count(i) == 2]
    not_rep = [i for i in ls if ls.count(i) == 1]
    cnt += 1
    if len(rep) == 2 and len(not_rep) == 4:
        if sum(rep)/2 >= (sum(not_rep)/len(not_rep)):
            print(cnt)
            break
# ans -> 34