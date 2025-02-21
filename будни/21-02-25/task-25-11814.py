from fnmatch import fnmatch as fn
from string import digits as d

for i in range(2100068079 - 2100068079%1777, 10**10, 1777):
    if fn(str(i), '21???68?79'):
        print(i, i//1777)