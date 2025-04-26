def f(num, q):
    ans = ''
    while num:
        ans += str(num % q)
        num //= q
    return ans[::-1]

for N in range(3, 1000):
    R = f(N, 3)
    if N%3 == 0:
        R += R[-2:]
    else:
        R += f(N%3 * 3, 3)

    R = int(R, 3)
    if R <= 150:
        print(N)