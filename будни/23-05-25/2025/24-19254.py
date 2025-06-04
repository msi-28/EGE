with open('24_19254.txt') as file:
    st = file.readline()
ans = []
st = st.split('FSRQ')
for i in range(len(st) - 80):
    ans.append('FSRQ'.join(st[i:i+81]))
print(len(max(ans, key=len)) + 6)

# ans -> 2739