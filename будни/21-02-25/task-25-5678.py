from itertools import product
ans = []
for r in range(3):
    for l in range(3):
        for q1 in product('0123456789', repeat = r):
            for q2 in product('0123456789', repeat=l):
                q1 = ''.join(q1)
                q2 = ''.join(q2)
                num = int(f'124{q1}5{q2}79')
                if num <= 10**8 and num % sum(map(int, [i for i in str(num) if int(i)%2!=0])) == 0:
                    ans.append([num, sum(map(int, str(num)))])

for i in sorted(ans):
    print(*i)

# ans:
# 1249579 37
# 12409579 37
# 12452979 39
# 12456179 35