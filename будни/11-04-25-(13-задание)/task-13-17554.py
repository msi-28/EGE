from ipaddress import *

net = ip_network('112.160.0.0/255.240.0.0', 0)
cnt  = 0
for ip in net:
    ip = f'{int(ip):032b}'
    if sum(map(int, ip)) % 3 != 0:
        cnt += 1

print(cnt)
# ans -> 699050