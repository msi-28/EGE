with open('24_20909.txt') as file:
    st = file.readline()
ans = []
st = st.split('AB')
for i in range(len(st) - 100):
    ans.append('AB'.join(st[i:i+101]))
print(len(max(ans, key=len)) + 2)
# ans -> 750