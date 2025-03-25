from itertools import *

graph = 'FG GE EH HC CF FA CA ED DH BD AD CB BH'.split()
matrix = '458 568 567 17 1238 2378 346 1256'.split()

print(*range(1, 9))
for i in permutations('ABCDEFGH'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x,y in graph):
        print(*i)

# A -> D + B -> H
# 3-> 5 + 2 -> 8
print(18 + 22)
# ans -> 40