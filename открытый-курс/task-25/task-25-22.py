def div(x):
    ans = set()
    for i in range(2, round(x**0.5) + 1):
        if x%i == 0:
            ans |= {i, x//i}
    return ans
for i in range(174457, 174506):
    if len(div(i)) == 2:
        print(' '.join(map(str, sorted(div(i)))))

# ans:
# 3 58153
# 7 24923
# 59 2957
# 13 13421
# 149 1171
# 5 34897
# 211 827
# 2 87251