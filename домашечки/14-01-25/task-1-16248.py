from itertools import permutations

graph = 'BA AD DF FG GE EC CB CA CD DE FE'.split()
matrix = '347 3456 1245 1237 236 25 14'.split()

print(*range(1,8))
for i in permutations('ABCDEFG'):
    if all([str(i.index(x) + 1) in matrix[i.index(y)] for x,y in graph]):
        print(*i)

# ans -> 42