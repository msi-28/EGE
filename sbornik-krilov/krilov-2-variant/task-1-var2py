from itertools import permutations

graph = 'AB BD DF FG GE EC AC BC DE AG'.split()
matrix = '245 137 256 156 134 347 26'.split()

print(*range(1, 8))
for i in permutations('ABCDEFG'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x,y in graph):
        print(*i)

# A -> G + B -> D
# 1 -> 2 + 4 -> 6
# 5 + 20 = 25 <- ответ