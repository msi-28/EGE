for x in range(111):
    num1 = x*111**3 + 3*111**2 + 2*111**1 + 1
    num2 = 1*211**3 + 7*211**2 + x*211**1 + 4
    num = num1 + num2
    if num % 111 == 0:
        print(num//111)

# ans -> 297262