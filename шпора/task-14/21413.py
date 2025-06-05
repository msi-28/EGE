from string import printable

alf = printable[:21]
for x in alf:
    num1 = int(f'82934{x}2', 21)
    num2 = int(f'2924{x}{x}7', 21)
    num3 = int(f'67564{x}8', 21)
    num = num1 + num2 + num3
    if num % 20 == 0:
        print(num//20)