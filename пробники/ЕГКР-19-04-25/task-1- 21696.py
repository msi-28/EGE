from itertools import *

graph = 'AF FC CG GH HE EA ED DF DB HB BG'.split()
matrix = '23 168 158 578 347 27 456 234'.split()

print(*range(1,9))
for i in permutations('ABCDEFGH'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x,y in graph):
        print(*i)

# ans -> 31