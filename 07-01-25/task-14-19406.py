from collections import Counter
from string import ascii_uppercase, digits
alf = digits + ascii_uppercase

def cnt(num):
    max_cnt = 0
    max_num = 0
    for i in set(str(num)):
        if str(num).count(i) > max_cnt:
            max_cnt =  str(num).count(i)
            max_num = int(i)
    return max_num

ans = 0
for x in alf[1:35]:
    num1 = int(f'6{x}QR{x}', 35)
    num2 = int(f'{x}59SH', 35)
    num3 = int(f'PH{x}69YW', 35)
    eq = num1 + num2 + num3
    digit = int(sorted(Counter(str(eq)).most_common(), key=lambda x: (-x[1], -int(x[0])))[0][0])
    if eq % digit**2 == 0:
        ans = eq //cnt(eq)**2
print(ans)

# жесть ответ: 46926015711

