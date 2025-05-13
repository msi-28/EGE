from itertools import *

graph = 'АБ БВ ВГ ГД ДЕ ЕБ БЖ ЖА БД ДВ'.split()
matrix = '346 45 16 12567 27 1347 46'.split()

print(*range(1, 8))
for i in permutations('АБВГДЕЖ'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x,y in graph):
           print(*i)

# в -> д: 1 -> 6: 47