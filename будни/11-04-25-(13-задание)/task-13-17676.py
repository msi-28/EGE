from ipaddress import ip_network

net = ip_network('115.192.0.0/255.192.0.0', 0)
cnt = 0

for ip in net:
    ip = f'{int(ip):032b}'
    if sum(map(int, ip)) % 3 != 0:
        cnt += 1
print(cnt)

# ans -> 2796202