with open('26_3230.txt') as file:
    N = int(file.readline())
    trees = [list(map(int, i.split())) for i in file]

trees = sorted(trees, key=lambda x: (-x[0], x[1]))

for tree1, tree2 in zip(trees, trees[1:]):
    row1, col1 = tree1
    row2, col2 = tree2
    if row1 == row2:
        if col2 - col1 - 1 == 11:
            print(row1, col1 + 1)
            break

# ans -> 2261 5087