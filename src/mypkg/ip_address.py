import ipaddress
import re 

def is_mask(mask):
    re.search("^(((255\.){3}(255|254|252|248|240|224|192|128|0+))|((255\.){2}(255|254|252|248|240|224|192|128|0+)\.0)|((255\.)(255|254|252|248|240|224|192|128|0+)(\.0+){2})|((255|254|252|248|240|224|192|128|0+)(\.0+){3}))$", mask)

def is_ip(ip_in, mask=""):
    if mask == "":
        try:
            return True
            #return ipaddress.ip_address(ip_in)
        except ValueError: 
            try:
                return ip_interface(ip_in)
            except:
                return 0
    else:
        return 0
is_mask("255.255.255.1")