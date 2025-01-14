from itertools import permutations

graph = 'AD DF FC FC CE EF EG BG AB'.split()
matrix = '247 145 456 123 23 37 16'.split()

print(*range(1, 8))
for i in permutations('ABCDEFG'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x,y in graph):
        print(*i)

# C -> F + A -> D
# 4 -> 2 + 3 -> 5
print(10 + 19) # ans -> 29