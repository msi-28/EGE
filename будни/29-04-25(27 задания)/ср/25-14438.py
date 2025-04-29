from fnmatch import fnmatch

for i in range(1746008 - 1746008%86513, 10**12, 86513):
    m = sum(map(int, str(i)))**0.5
    if fnmatch(str(i), '17*46??8') and i%86513 == 0 and (m == int(m)):
        print(i, i//86513)
