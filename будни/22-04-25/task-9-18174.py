with open('9_18174 (2).txt') as file:
    ls = [list(map(int, i.split())) for i in file]
cnt = 0
for arr in ls:
    c1 = len([i for i in arr if arr.count(i) == 2]) == 2
    c2 = abs(sum(i for i in arr if i < 0)) > sum(i for i in arr if i > 0)
    if c1 and c2:
        cnt += 1
print(cnt)

# ans -> 22