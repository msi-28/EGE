import re

# Положительные ретроспективные проверки

text = 'abcabccbabaccab'
pattern = r'(?<=cba)\w+'
matches = re.findall(pattern, text)
print(matches)

# ===========================================================
# Отрицательные ретроспективные проверки

text = 'AB AC DC BB CA AD'
pattern = r'((?<!A)\w){2}'
matches = re.findall(pattern, text)
print(matches)