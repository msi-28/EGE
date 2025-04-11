from string import ascii_uppercase as alf, digits as d

with open('24.txt') as file:
    st = file.readline()

for i in (d+alf)[12:]:
    st = st.replace(i, ' ')

st = st.split()
for i in range(len(st)):
    st[i] = st[i].lstrip('0')
    st[i] = st[i].rstrip('13579B')
print(len(max(st, key=len)))

# ans -> 19