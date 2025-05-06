from itertools import *
cnt = 0
for s in product(sorted('ЦАПЛЯ'), repeat=5):
    s = ''.join(s)
    c1 = s.count('А') <= 1
    c2 = s.count('Ц') == 2
    c3 = 'Л' not in s
    cnt += 1
    if c1 and c2 and c3:
        print(cnt, s)

# ans -> 319