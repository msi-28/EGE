from itertools import permutations

graph = 'АБ АВ БГ ГЕ ЕЗ ЗД ДВ БВ'.split()
matrix = '67 567 456 35 234 123 12'.split()

print(*range(1, 8))
for i in permutations('АБВГДЕЗ'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x,y in graph):
        print(*i) # может выдать больше 2х последовательностей