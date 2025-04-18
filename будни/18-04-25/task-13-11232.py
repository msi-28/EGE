from ipaddress import ip_network

net = ip_network('192.168.31.80/255.255.255.240', 0)
m = 0
for ip in net:
    ip = f'{int(ip):032b}'
    if ip.count('1') > m:
        m = ip.count('1')

print(m)

# ans -> 16