from math import ceil

with open('2600.txt') as file:
    N = int(file.readline())
    trucks = [list(map(int, i.split())) for i in file]
    for i in range(len(trucks)):
        trucks[i].append(ceil((trucks[i][1]/10)))
        trucks[i].append(trucks[i][0] + trucks[i][2])

trucks = sorted(trucks, key=lambda x: (x[0], x[2]))

place = [[0,0]]
for start, val, stand, end in trucks:
    if place[-1][1] <= start:
        place.append([start, end, val])

print(place)

print(len(place)-1, sum([place[i][1] for i in range(len(place))]))
# ans -> 68 49929
