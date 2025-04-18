from re import *

pattern = '^((\\+7|7|8)+([0-9]){10})$' # маска объекта (номера)

'''
функция fullmatch() проверяет соответсвие строки(первый аргумент) паттерну (второй аргумент)
fullmatch() возвращает объект типа re.match, поэтому выглядеть это может странно и страшно
но фактически если строка пододит -> выводится что-то непонятное, если нет -> None
'''
print('1)')
print(fullmatch(pattern, '+79143970728')) # <re.Match object; span=(0, 12), match='+79143970728'>
print(fullmatch(pattern, '+522657')) # None

'''
для пущей наглядности все можно завернуть в буленовский тип данных (True/False)
тогда если строка подойдет -> True, иначе -> False
'''
print('2)')
print(bool(fullmatch(pattern, '+79143970728'))) # True
print(bool(fullmatch(pattern, '+522657'))) # False