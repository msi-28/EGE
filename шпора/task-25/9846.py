from fnmatch import fnmatch

for i in range(123405 - 123405%2025, 10**8, 2025):
    st = '12*34?5'
    if fnmatch(str(i), st):
        print(i, i//2025)
# ans:
# 1253475 619
# 12103425 5977
# 12593475 6219
# 12913425 6377