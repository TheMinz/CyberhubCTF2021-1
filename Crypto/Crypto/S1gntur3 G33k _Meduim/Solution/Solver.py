#python 2
import string
import sympy
import hashlib
from Crypto.Util.number import long_to_bytes

q = 1157962076533010980101494567430013859734265641597
r1 = 18654062491937287313427816862270633565918024325
s1 = 640509775348981148815694802803590271304880323352
k = 1333333333333333333333333333333337
r1_inv=int(sympy.invert(r1, q))

m1="Some Secret Message that has no value"
m1=int(hashlib.sha1(m1).hexdigest(), 16)

x=(r1_inv*((s1*k)-m1))%q
print("Private Key Value : %d"%x)
print("Flag : %s"%long_to_bytes(x))
