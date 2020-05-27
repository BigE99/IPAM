import pytest
import ipaddress
import mypkg.ip_address

'''
@pytest.mark.parametrize(('ip', 'mask'), [("10.0.0.1", ""), ("10.0.0.1", "24"), ("10.0.0.1", "/24"), ("10.0.0.1", "255.255.255.0"), ("10.0.0.0", "")])
def test_get_ip_ipv4(ip, mask):
	pytest.assume(ipaddress.ip_address(ip) == get_ip(ip))
	pytest.assume(ipaddress.ip_interface(ip, "/" + mask) == get_ip(ip, mask))
	pytest.assume(ipaddress.ip_interface(ip, mask) == get_ip(ip, mask))
	pytest.assume(ipaddress.ip_interface(ip, "/" + str(ipaddress.IPv4Network('0.0.0.0/' + mask).prefixlen)) == get_ip(ip, mask))
	pytest.assume(not get_ip(ip))
	
def test_get_ip_ipv6(ip, mask):
	return 0'''
@pytest.mark.parametrize(('x', 'y'), [(1, 1), (1, 0), (0, 1)])
def test_simple_assume(x, y):
    with pytest.assume:
        assert x == y
        assert True
        assert False