st = open('2418.txt').readline()
ans = []

st = st.replace('+', '*')

while '**' in st:
    st = st.replace('**', ' ')

st = st.split()

for i in range(len(st)):
    st[i] = st[i].strip('*')

for i in range(len(st)):
    stb = st[i].split('*')
    if all(int(stb[j])%2 == 0 for j in range(len(stb))):
        ans.append(len(st[i]))

print(max(ans))
# ans -> 127