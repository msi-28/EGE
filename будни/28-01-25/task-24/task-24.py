with open('24_14510.txt') as file:
    st = file.readline()
# * - gl
# & - sogl

for i in st:
    if i in 'AEIOUY':
        st = st.replace(i, '*')
    else:
        st = st.replace(i, '&')

ans = []
minn = 1000000
for i in range(len(st) - 499):
    s = st[i:i+500]
    l = sum(len(k) for k in st)
    if minn > l:
        minn = l
print(min(ans))