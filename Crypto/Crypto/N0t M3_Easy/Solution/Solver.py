import binascii
from Crypto.Util.number import inverse
p=0xEF76DD9531E336D84E9B942019921555
q=0x9031F6A4EF9B31C67D557BC7AA639BBB
e=0x10001
n=0x86E1991AD6D2D141565FD25ECB4403E15155EAE995D0E607DEC0F4A9D27F0C17
c=25161232102640471912225957662963112298846413548283470138268726899733058517741
phi=(p-1)*(q-1)
d=inverse(e,phi)
m=pow(c,d,n)
print(bytes.fromhex(hex(m)[2:]).decode('utf-8'))
