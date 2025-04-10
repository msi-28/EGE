with open('9.txt') as file:
    ls = [list(map(int, i.split())) for i in file]
cnt = 0
for arr in ls:
    if len([i for i in arr if arr.count(i) == 3]) == 6 and len([i for i in arr if arr.count(i) == 1]) == 1:
        if max([i for i in arr if arr.count(i) == 3]) > [i for i in arr if arr.count(i) == 1][0]:
            cnt += 1

print(cnt)

# ans -> 1