from itertools import *

graph = 'АВ ВД ДЗ ЗЖ ЖГ ГА АБ БВ БГ ГД ДЕ ЕЖ ЕЗ'.split()
matrix = '256 1458 478 237 126 15 348 2367'.split()

print(*range(1, 9))
for i in permutations('АБВГДЕЖЗ'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x,y in graph):
        print(*i)

# ans - > 1357