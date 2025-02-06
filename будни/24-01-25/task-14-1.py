from string import digits, ascii_uppercase

alf = digits + ascii_uppercase

for x in alf[:22]:
    num1 = int(f'A23{x}AC0', 22)
    num2 = int(f'GB{x}21670', 22)
    eq = num1 + num2
    if eq % 21 == 0:
        print(eq/22)