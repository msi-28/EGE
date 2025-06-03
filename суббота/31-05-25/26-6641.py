with open('26_6641.txt') as file:
    N, L = map(int, file.readline().split())
    items = [[int(i.split()[0]),i.split()[1]]  for i in file]

M = L
items = sorted(items)
total = []
cnt_S = []
cnt_W = []

for cost, type in items.copy():
    if cost <= M:
        M -= cost
        if type == 'S':
            cnt_S.append(cost)
        else:
            cnt_W.append(cost)
        items.remove([cost, type])
    else:
        break

for cost, type in items:
    if type == 'S' and M + cnt_W[-1] - cost >= 0:
        M += cnt_W[-1] - cost
        cnt_S.append(cost)
        cnt_W.pop()

print(len(cnt_S), L - (sum(cnt_S) + sum(cnt_W)))

# ans -> 393 4