for N in range(1, 1000):
    R = bin(N)[2:]
    R = R.replace('1', '*').replace('0', '1').replace('*', '0')
    R = '1' + R
    if R.count('1')%2 == 0:
        R += '1'
    else:
        R +='0'
    R = int(R, 2)
    if R > 180:
        print(N)
        break

# ans -> 32