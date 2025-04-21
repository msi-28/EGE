from ipaddress import ip_network, ip_address

for mask in range(32, 1, -1):
    net = ip_network(f'153.202.16.37/{mask}', 0)
    if ip_address('153.202.16.32') in net:
        print(net.netmask)
print(255+248)