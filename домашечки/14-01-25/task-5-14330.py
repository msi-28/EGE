for N in range(10**4, 10**5):
    sq_sum = (int(max(str(N))) + int(min(str(N))))**2
    mult = 1
    for i in str(N):
        if int(i) % 2 == 0:
            mult = mult * int(i)
    if sq_sum > mult:
        R = str(sq_sum) + str(mult)
    else:
        R = str(mult) + str(sq_sum)

    if R == '12116':
        print(N)
        break

# ans -> 22229