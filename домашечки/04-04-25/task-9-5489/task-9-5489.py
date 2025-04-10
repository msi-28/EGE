with open('9_5489.txt') as file:
    ls = [list(map(int, i.split())) for i in file]
cnt = 0
for arr in ls:
    c1 = len(set(arr)) == len(arr)
    c2 = len([i for i in arr if i%2 == 0]) > len([i for i in arr if i%2 != 0])
    c3 = sum([i for i in arr if i%2 == 0]) < sum([i for i in arr if i%2 != 0])
    if c1 and c2 and c3:
        cnt += 1
print(cnt)
# ans -> 241

