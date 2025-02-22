st = ''.join([i for i in open('24-1.txt')])

while '++' in st or '**' in st or '*+' in st or '+*' in st:
    st = st.replace('++', ' ').replace('**', ' ').replace('+*', ' ').replace('*+', ' ')

st = st.split()
for i in range(len(st)):
    st[i] = st[i].strip('+').strip('*')
print(len(max([i for i in st if eval(i) == 0], key=len)))