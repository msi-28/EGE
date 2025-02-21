from string import digits as d
from fnmatch import fnmatch as fn

for i in range(85016 - 85016%21025, 10**9, 2658):
    if fn(str(i), '85?16*'):
        print(i, i//2658)