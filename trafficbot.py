import webbrowser
import time
import ipaddress




x=1
while True:
    # initialize an IPv4 Address
    ip = ipaddress.IPv4Address("192.168.1.1")

    # print True if the IP address is global
    print("Is global:", ip.is_global)

    # print Ture if the IP address is Link-local
    print("Is link-local:", ip.is_link_local)

    # ip.is_reserved
    # ip.is_multicast

    # next ip address
    print(ip + 1)

    # previous ip address
    print(ip - 1)

    # initialize an IPv4 Network
    network = ipaddress.IPv4Network("192.168.1.0/24")

    # get the network mask
    print("Network mask:", network.netmask)

    # get the broadcast address
    print("Broadcast address:", network.broadcast_address)

    # print the number of IP addresses under this network
    print("Number of hosts under", str(network), ":", network.num_addresses)

    # iterate over all the hosts under this network
    print("Hosts under", str(network), ":")
    for host in network.hosts():
        print(host)

    # iterate over the subnets of this network
    print("Subnets:")
    for subnet in network.subnets(prefixlen_diff=2):
        network.overlaps(ipaddress.IPv4Network("192.168.0.0/16"))

    webbrowser.open('https://direct-link.net/428541/dealing-with-deals')
    time.sleep(5)
    x+=1