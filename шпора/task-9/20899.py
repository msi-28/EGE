with open('9_20899.txt') as file:
    arr = [list(map(int, i.split())) for i in file]

cnt = 0
for ls in arr:
    c1 = max(ls) < sum(ls) - max(ls)
    c2 = len([i for i in ls if ls.count(i) == 2]) == 2
    if c1 and c2:
        cnt += 1
print(cnt)
# ans -> 138