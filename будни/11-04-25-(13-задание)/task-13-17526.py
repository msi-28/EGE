from ipaddress import *

net = ip_network('172.16.128.0/255.255.192.0', 0)
cnt = 0
for ip in net:
    ip = f'{int(ip):032b}'
    if sum(map(int, ip))%2 != 0:
        cnt += 1

print(cnt)

# ans -> 8192