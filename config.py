"""
Contains configuration variables such as IP address and paths
"""

import requests

def get_ip():
    url = "http://checkip.dyndns.org"
    request = requests.get(url)
    clean = request.text.split(': ', 1)[1]
    your_ip = clean.split('</body></html>', 1)[0]
    return your_ip

my_ip = get_ip()
#print(my_ip)

usr = "pi"
ip_local = # LOCAL IP GOES HERE
ip_global = # PUBLIC IP GOES HERE

if my_ip == ip_global:
    addr = usr+"@"+ip_local
else:
    addr = usr+"@"+ip_global
