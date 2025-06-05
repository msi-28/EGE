from ipaddress import ip_network, ip_address

ip1 = ip_address('95.24.2.9')
ip2 = ip_address('95.24.3.10')

for mask in range(1, 31):
    net1 = ip_network(f'{ip1}/{mask}', 0)
    net2 = ip_network(f'{ip2}/{mask}', 0)
    if net1 != net2 and ip1 in net1.hosts() and ip2 in net2.hosts():
        cnt = 0
        for ip in net1:
            ip = int(f'{int(ip):032b}')
            if ip%10 == 0:
                cnt += 1
        print(cnt)
# ans -> 128