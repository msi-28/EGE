with open('26_11956.txt') as file:
    N = [int(i) for i in file.readline().split()]
    ls = [i[:-1].split() for i in file.readlines()]


for i in range(len(ls)):
    for j in range(2):
        ls[i][j] = int(ls[i][j])

ls = sorted(ls)
print(N)

max_skill = 0
max_lev = 0
skill = N[1]
lev = 0

maxx = []
for i in range(len(ls)):
    print(ls[i][0], ls[i][1])
    if int(ls[i][0]) <= skill:
        skill += int(ls[i][1])
        lev += 1
        print(lev, skill)
        print('\n')

    else:
        if lev > max_lev:
            maxx.append(str(lev) + ' ' + str(skill))
print(maxx)
