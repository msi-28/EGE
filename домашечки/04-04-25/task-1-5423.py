from itertools import *

graph = 'АБ БД ДЕ ЕЗ ЗЖ ЖВ ВГ ГА АД ВЗ'.split()
matrix = '245 15 478 35 1246 58 38 367'.split()

print(*range(1, 9))
for i in permutations('АБВГДЕЖЗ'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x,y in graph):
        print(*i)

# г -> З
# 6 -> 1 = 6 -> 5 -> 1 = 1 + 4 = 5
# ans = 5