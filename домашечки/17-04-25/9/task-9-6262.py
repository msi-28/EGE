with open('9_6262.txt') as file:
    ls = [list(map(int, i.split())) for i in file]

cnt = 0
for i in ls:
    c1 = len(set(i)) != len(i)
    c2 = len([j for j in i if j%2 != 0]) == 3
    if c1 and c2:
        cnt += 1
print(cnt)

# ans -> 307