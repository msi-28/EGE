from itertools import *

graph = 'AE EB BH HC CF FA AB CG GD DH'.split()
matrix = '248 157 456 136 23 34 28 17'.split()

print(*range(1, 9))
for i in permutations('ABCEFGDH'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x,y in graph):
        print(*i)

# c -> g + h -> b
# 2->7 + 1->4
print(21 + 2)
# ans - > 23