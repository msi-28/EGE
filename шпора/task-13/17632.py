from ipaddress import ip_network, ip_address

cnt = 0
net = ip_network('112.160.0.0/255.240.0.0', 0)
for ip in net:
    ip = f'{int(ip):032b}'
    if ip.count('1')%5 == 0:
        cnt += 1
print(cnt)
# ans -> 215766