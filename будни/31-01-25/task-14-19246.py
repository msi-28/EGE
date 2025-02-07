from string import printable

alf = printable[:25]
for x in alf:
    num1 = int(f'11353{x}12', 25)
    num2 = int(f'135{x}21', 25)
    eq = num1 + num2
    if eq % 24 == 0:
        print(eq//24)

# ans -> 266249847