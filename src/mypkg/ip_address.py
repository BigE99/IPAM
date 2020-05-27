import ipaddress
import re 


def get_ip(ip_in, mask=""):
    if mask == "":
        try:
            return ipaddress.ip_address(ip_in)
        except ValueError:
            print("Invaild Ip address")
            return False
    else:
        if re.search("^(((255\.){3}(255|254|252|248|240|224|192|128|0+))|((255\.){2}(255|254|252|248|240|224|192|128|0+)\.0)|((255\.)(255|254|252|248|240|224|192|128|0+)(\.0+){2})|((255|254|252|248|240|224|192|128|0+)(\.0+){3}))$", mask):
            mask = "/" + str(ipaddress.IPv4Network('0.0.0.0/255.255.255.0').prefixlen)
        elif(mask[0] != "/"):
            mask = "/" + mask
        ip = ip_in + mask
        try:
            return ipaddress.ip_interface(ip)
        except ValueError:
            print("IP address of netmask is invaild")
            return False

print(get_ip("3"))