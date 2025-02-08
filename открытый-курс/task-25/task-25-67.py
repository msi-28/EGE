def div(x):
    ans = set()
    for i in range(2, round(x**0.5) + 1):
        if x % i == 0:
            ans |= {i, x//i}
    return sorted(ans)

for i in range(81234, 134690):
    if len(div(i)) == 3:
        print(' '.join(map(str, (div(i)))))

# ans:
# 17 289 4913
# 19 361 6859