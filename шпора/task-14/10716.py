for x in range(149, 1, -1):
    num1 = 5*150**4 + 1*150**3 + x*150**2 + 2*150 + 9
    num2 = x*150**3 + 0 + 2*150 + 3
    num = num1 + num2
    if num%149 == 0:
        print(num//149)
        break
# ans -> 20157588