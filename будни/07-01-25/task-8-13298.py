from itertools import product

cnt = 0
final_cnt = 0
for s in product(sorted('ПРИВЫЧКА'), repeat=5):
    s = ''.join(s)
    cnt += 1
    c1 = ''.join(set(s)) == s
    c2 =  'И' not in s and 'Ы' not in s and 'А' not in s

    if cnt%5 != 0:
        final_cnt += 1
        if c1 and c2:
            print(final_cnt)
