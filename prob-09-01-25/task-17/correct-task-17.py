with open('17_11949.txt') as file:
    ls = [int(i) for i in file]

max_68 = max([i for i in ls if abs(i) % 100 == 68])
cnt = 0
max_ans = -100_000_000
for i in range(len(ls) - 3):
    n1, n2, n3, n4 = ls[i:i+4]
    summ  = n1 + n2 + n3 + n4

    c1 = len(str(abs(n1))) == 2
    c2 = len(str(abs(n2))) == 2
    c3 = len(str(abs(n3))) == 2
    c4 = len(str(abs(n4))) == 2

    f1 = c1 + c2 + c3 + c4 == 1 or c1 + c2 + c3 + c4 == 4
    f2 = summ >= max_68

    if f1 and f2:
        cnt += 1
        if summ >= max_ans:
            max_ans = summ
print(cnt, max_ans)

# ans -> 75 247177