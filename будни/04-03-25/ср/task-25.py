from itertools import product
from string import digits

digits += ' '
ans = set()
for s1 in product(digits, repeat=3):
    for s2 in product(digits, repeat=3):
        for q in range(10):
            s1 = ''.join(s1)
            s2 = ''.join(s2)
            s = f'1{q}3{s1}5{s2}954'
            s = ''.join(s.split())
            if int(s)%6437 == 0 and int(s) <= 10**10:
                ans |= {str(s + ' ' + str(int(s)//6437))}
for i in sorted(ans):
    print(i)

ans:
1035339954 160842
1537425954 238842
1730535954 268842
1833527954 284842
1936519954 300842
