with open('26_4205.txt') as file:
    N = int(file.readline())
    place = [list(map(int, i.split())) for i in file]

place = sorted(place, key = lambda x: (-x[0], x[1]))
free_gap = []

row, col = 0, 0
for tree1, tree2 in zip(place, place[1:]):
    if tree1[0] == tree2[0]:
        if tree2[1] - tree1[1] - 1 == 13:
            row = tree1[0]
            col = tree1[1] + 1
            print(row, col)