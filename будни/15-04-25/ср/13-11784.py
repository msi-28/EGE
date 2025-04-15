from ipaddress import ip_network

for A in range(256):
    net = ip_network(f'248.112.{A}.35/255.255.255.240', 0)
    for ip in net:
        if f'{int(ip):032b}'[:16].count('0') > f'{int(ip):032b}'[16:].count('0'):
            break
    else:
        print(A)

# ans -> 224