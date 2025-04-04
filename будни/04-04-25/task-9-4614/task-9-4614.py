with open('9_4614.txt') as file:
    ls = [list(map(int, i.split())) for i in file]

cnt = 0
for i in ls:
    c1 = max(i) < sum(i) - max(i)
    c2 = [str(list(map(str, i)).count(j)) for j in list(map(str, i))].count('2') == 2
    if c1 and c2:
        cnt += 1
print(cnt)

# ans - > 133
