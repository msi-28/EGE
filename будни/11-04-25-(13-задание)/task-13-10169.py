from ipaddress import ip_network

for mask in range(33):
    net1 = ip_network(f'157.127.182.76/{mask}', 0)
    net2 = ip_network(f'157.127.190.80/{mask}', 0)
    if net1.network_address != net2.network_address:
        print(mask)

# ans -> 21