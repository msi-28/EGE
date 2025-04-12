from re import *

text = open('24_1866.txt').readline()
pattern = r'(?<=ad|da)\w+?(?=ad|da)'
match = findall(pattern, text)
print(len(max(match, key=len)) + 2)

# ans -> 2252