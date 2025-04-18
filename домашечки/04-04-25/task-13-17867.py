from ipaddress import ip_network

net = ip_network('172.16.168.0/255.255.248.0', 0)
cnt = 0
for ip in net:
    ip = f'{int(ip):-32b}'
    if ip.count('1')%5!= 0:
        cnt += 1
print(cnt)

# ans -> 1663