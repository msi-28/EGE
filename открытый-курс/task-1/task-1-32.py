from itertools import permutations

graph = 'АБ БВ ВГ ГА ДГ ГЕ ЕЖ'.split()
matrix = '26 15 67 6 26 13457 36'.split()

print(*range(1, 8))
for i in permutations('АБВГДЕЖ'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x,y in graph):
        print(*i)

# Из Е в Ж => из 3 в 7 —> 14