ls = [int(i) for i in open('17_12249.txt')]

ans = []
m = max([i for i in ls if len(str(abs(i))) == 5 and abs(i)%10 == 3])
for i in range(len(ls) - 2):
    nums = ls[i: i + 3]
    c1 = len([i for i in nums if abs(i)%10 == 3]) >= 1
    c2 = sum(nums) <= m
    if c1 and c2:
        ans.append(sum(nums))

print(len(ans), max(ans))

# ans -> 1767 99081