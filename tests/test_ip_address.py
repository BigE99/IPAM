import pytest
import ipaddress

from mypkg.ip_address import *

def test_is_ip_normal():
	assert(get_ip("192.168.0.1") == ipaddress.ip_address("192.168.0.1"))
