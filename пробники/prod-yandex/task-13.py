from ipaddress import *

net = ip_network('10.112.0.0/255.248.0.0', 0)

ans = 0
for ip in net:
    ip = bin(int(ip))[2:]
    if sum(map(int, ip)) % 3 == 0:
        ans += 1
print(ans)