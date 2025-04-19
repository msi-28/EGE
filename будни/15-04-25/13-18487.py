from ipaddress import ip_network

for A in range(256):
    net = ip_network(f'192.214.{A}.184/255.255.255.224', 0)
    for ip in net:
        ip = f'{int(ip):032b}'
        if ip.count('1') <= 15:
            break
    else:
        print(A)

# ans -> 127