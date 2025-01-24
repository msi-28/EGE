from itertools import product

cnt = 0
for s in product('123456', repeat=4):
    s = ''.join(s)
    c0 = s[0] != '0'
    c1 = s.count('3') == 1
    c2 = s.count('2') + s.count('4') + s.count('6') <= s.count('1') + s.count('3') + s.count('5')
    if c0 and c1 and c2:
        cnt +=1

print(cnt)
# ans -> 392