# def f(x, y, s):
#     if x + y >= 131: return s % 2 == 0
#     if s == 0: return False
#     h = [f(x + 2, y, s - 1), f(x, y + 2, s - 1),
#          f(x * 2, y, s - 1), f(x, y * 2, s - 1)]
#     return any(h) if (s + 1) % 2 == 0 else all(h)
#
# print('19)', min([s for s in range(1, 123) if f(11, s, 2)])) # ans -> 300
#
# print('20)', [s for s in range(1, 123) if f(11, s, 2) and not f(11, s, 1)]) # ans -> 30
#
# print('21)', [s for s in range(1, 123) if f(11, s, 4)and not f(11, s, 2)]) # ans -> 30
#
#
# def f(x, s):
#     if x <= 12: # условие
#         return s%2 == 0 # игрок
#
#     if s == 0: return False # конец игры
#     h = [f(x//3, s -1), f(x - 12, s -1)]
#     return any(h) if(s-1) % 2 == 0 else all(h)
#
# print('19)', [s for s in range(1000, 13, -1) if f(s, 2)])
# print('20)', [s for s in range(1000, 13, -1) if f(s, )])
# print('19)', [s for s in range(1000, 13, -1) if f(s, 2)])


def f(x, s):
    if x <= 19: return s % 2 == 0  # Условие меняется в зависимости от задачи
    if s == 0: return False

    # Действия меняются в зависимости от задачи
    h = [f(x - 2, s - 1), f(x - 5, s - 1), f(int(x / 3), s - 1)]
    return any(h) if (s - 1) % 2 == 0 else all(h)


print('19)', [s for s in range(20, 100) if f(s, 2)])
print('20)', [s for s in range(20, 100) if f(s, 3) and not f(s, 1)])
print('21)', [s for s in range(20, 100) if f(s, 4) and not f(s, 2)])

# 19) [60, 61]
# 20) [62, 63, 65, 66]
# 21) [64, 67, 68]