from ipaddress import *

for mask in range(33):
    net1 = ip_network(f'118.187.59.255/{mask}', 0)
    net2 = ip_network(f'118.187.65.115/{mask}', 0)
    if (net1.network_address != net2.network_address and
            ip_address('118.187.59.255') != net1.broadcast_address and
            ip_address('118.187.65.115') != net2.broadcast_address):
        print(mask)

# ans -> 21