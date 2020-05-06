import pytest

from mypkg.ip_address import *

def test_is_ip():
	assert(is_ip("192.168.0.1") == True)
