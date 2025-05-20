with open('17_5882.txt') as file:
    data = [int(i) for i in file]
ls = []
for i in range(len(data)-1):
    num1, num2 = data[i:i+2]
    if (abs(num1)%10 == 3) ^ (abs(num2)%10 == 3):
        ls.append(min([num1, num2]))
m = sum([int(i)**2 for i in str(abs(min(ls)))])
ans = []
for i in data:
    c1 = '3' in str(i)
    c2 = i >= m
    if c1 and c2:
        ans.append(i)
print(len(ans), min(ans))

# ans -> 893 237