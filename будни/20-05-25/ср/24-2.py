with open('24_19489.txt') as file:
    st = file.readline()

st = st.replace('WSFWW', 'WSFW SFWW')
st = st.split()

ans = []
maxi = 0
for i in st:
    if i.count('WWF') <= 120:
        ans.append(i)
    else:
        if len(i) > maxi:
            i.split('*')
            for j in range(len(i) - 120):
                ps = 'WWF'.join(i[j:j+121])
                maxi = max(maxi, len(ps))

print(len(max(ans, key=len)))
# ans -> 3080