from re import *
with open('24-333.txt') as file:
    st = file.readline()
# st = 'alex@@s..ch@gmail.com.runet@yandex.rubo@yandex.ru'

name = r'\w+(\.\w+)+'
serv = r'yandex.ru|gmail.com'
pattern = rf'{name}@{serv}'

match = finditer(pattern, st)
ans = []

for i in match:
    print(i.group())
    ans.append(i.group())

print(len(max(ans, key=len)))
print(max(ans, key=len))

# ans -> 118