st = '1' * 2025
while '1111' in st or '5555' in st:
    if '1111' in st:
        st = st.replace('1111', '55')
    else:
        st = st.replace('5555', '5')
print(st)

# ans -> 51