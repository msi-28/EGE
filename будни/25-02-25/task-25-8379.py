from itertools import product
ans = []
for r in range(7):
    for i in product('0123456789', repeat=r):
        i = ''.join(i)
        num = int(f'1234{i}')
        if num % 137 == 0 and int(i) % sum(map(int, i))**3 == 0:
            ans.append(num)
for i in sorted(ans):
    print(i)

# ans:
# 12340001
# 123400010
# 123437000
# 1234000100
# 1234370000