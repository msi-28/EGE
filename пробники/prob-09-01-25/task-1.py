from itertools import permutations

graph = 'AE EH HG GC CF AF ED DF DB HB BG'.split()
matrix = '367 568 18 58 247 127 156 234'.split()

print(*range(1, 9))
for i in permutations('ABCDEFGH'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x,y in graph):
        print(*i)

# C->G + H->E
# 3->1 + 7->5
print(19 + 27)

# ans -> 46