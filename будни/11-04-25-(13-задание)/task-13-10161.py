from ipaddress import ip_network

for mask in range(33):
    net1 = ip_network(f'211.115.61.154/{mask}', 0)
    net2 = ip_network(f'211.115.59.137/{mask}', 0)
    if net1.network_address == net2.network_address:
        print(net1.netmask)

# ans -> 248