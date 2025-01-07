from itertools import permutations

graph = 'АБ БВ ВД ДЕ ЕК КГ КВ ВА ВГ'.split()
matrix = '56 47 46 236 16 13457 26'.split()

print(*range(1, 8))
for i in permutations(sorted('АБВДЕКГ')):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x,y in graph):
        print(*i)

# кратчайший путь между В и Е:
# В —> 6; Е —> 2
# 1) 6 —> 7 —> 2 = 20 + 15 = 35
# 2) 6 —> 3 —> 4 —> 2 = 10 + 10 + 5 = 25
# ответ: 25