from itertools import permutations

graph = 'AB AD AF DE EB EG GC CF BF'.split() #все возможные ребра
matrix = '37 367 125 56 34 247 126'.split() #пересечения в рамках матрицы

print(*range(1, 8))
for i in permutations('ABCDEFG'): #в perm. передаем вс возможные вершины
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x,y in graph):
        print(*i) #возвращает соотвествие ребер с матрицей. остальное руками