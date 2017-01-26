import socket
import binascii as b
import sys

s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.IPPROTO_IP)
s.bind(("lo",0x0800))

#s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

#s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

a = ''
while 1:
    val = s.recvfrom(65565)
    val = val[0][42:]
    if a != val:
        sys.stdout.write(val.replace('}',''))
        a = val

sys.stdout.flush()
#s.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
