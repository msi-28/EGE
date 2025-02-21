ans = []

for q1 in '0123456789':
    for q2 in '0123456789':
        for ch1 in '2468':
            for ch2 in '02468':
                for nch in '13579':
                    num = int(f'{ch1}9{q1}23{q2}23{nch}{ch2}')
                    if num%1984 == 0:
                        ans.append([num, num//1984])

for i in sorted(ans):
    print(*i)

# ans:
# 2902302336 1462854
# 4912342336 2475979
# 6922382336 3489104
# 6932302336 3494104
# 8912332352 4492103
# 8942342336 4507229