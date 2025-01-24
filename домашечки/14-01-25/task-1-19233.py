from itertools import permutations

graph = 'AG GD DB BC CH HF FA GF DE EH BE'.split()
matrix = '234 157 147 138 268 58 23 456'.split()

print(*range(1,9))
for i in permutations('ABCDEFGH'):
    if all([str(i.index(x) + 1) in matrix[i.index(y)] for x,y in graph]):
        print(*i)

# A -> G + D -> E
# 6 -> 8 + 4 -> 1
# 4 + 7 = 11
# ans -> 11
