from itertools import permutations

graph = 'АБ БД ДК КЕ ЕВ ВА АГ ГБ ВГ ГД ДЕ'.split()
matrix = '246 1345 25 1267 237 147 456'.split()

print(*range(1, 8))
for i in permutations('АБВГДЕК'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x,y in graph):
        print(*i)

# Из В в Е => из 7 в 5 = 36 <— ответ