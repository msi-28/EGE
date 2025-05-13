from string import ascii_uppercase as asc, digits as d

alf = (d + asc)[:16]

for x in alf:
    for y in alf:
        num1 = int(f'27A{x}23', 16)
        num2 = int(f'8{y}E5D2', 16)
        num = num1 + num2
        if num % 5 == 0:
            print(int(x, 16) + int(y, 16))
