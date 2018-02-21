import os
import struct
from ctypes import *

host = "192.168.0.187"

class IP(Structure):
  fields = {

	("ihl",	 c_ubyte, 4),
	("version", c_ubyte, 4),
	("tos", c_ubyte),
	("len", c_ushort),
	("id", c_ushort),
	("offset", c_ushort),
	("ttl", c_ubyte),
	("protocol_num", c_ubyte),
	("sum", c_ushort),
	("src", c_ulong),
	("dst", c_ulong)

    }

  def __new__(self, socket_buffer=None):
      return self.from_buffer_copy(socket_buffer)
