from itertools import permutations

graph = 'AB BD DF FG GE EC BC DE BC AG'.split()
matrix = '237 167 156 567 34 234 124'.split()

print(*range(1, 8))
for i in permutations('ABCDEFG'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x,y in graph):
        print(*i)

# A -> B + C -> E
# 1 -> 7 + 2 -> 6
# 9 + 15 = 24 <- ОТВЕТ