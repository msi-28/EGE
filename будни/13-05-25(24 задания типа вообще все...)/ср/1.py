from itertools import *

graph = 'АБ БД ДГ ГЖ ЖЗ ЗЕ ЕВ ВА БВ ДЕ ДЖ ЖЕ'.split()
matrix = '3578 346 1258 26 13 248 18 1367'.split()

print(*range(1, 9))
for i in permutations('АБВГДЕЖЗ'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x,y in graph):
        print(*i)

# ans -> 15