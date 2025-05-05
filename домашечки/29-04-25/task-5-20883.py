def f(q, num):
    ans = ''
    while num:
        ans += str(num%q)
        num //= q
    return ans[::-1]

for N in range(1, 1000):
    R = f(5, N)
    if len(R)%2 == 0:
        R = R[len(R)//2:] + R[:len(R)//2]
    else:
        R += str(N%5)
        R = R[len(R) // 2:] + R[:len(R) // 2]

    R = int(R, 5)
    if R > 50:
        print(N)
        break

# ans -> 26