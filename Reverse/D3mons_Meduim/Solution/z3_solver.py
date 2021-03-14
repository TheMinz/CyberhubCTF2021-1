import z3
import string
charset = string.lowercase+string.uppercase+string.digits+'_'
charset= [ord(i)for i in charset]
s = z3.Solver()
input_length=26
goal=[65,45,17,18,18,49,105,5,31,29,38,97,14,55,45,44,37,73,123,46,3,108,79,32,18,118]
flag = [z3.BitVec("x{}".format(i), 8) for i in range(input_length)]
flag_full = z3.Concat(*flag)
for i in range(26):
    s.add(z3.Or([flag[i] == j for j in charset]))
for i in range(26):
    s.add((flag[i]^flag[(i+1)%26]^flag[(i+2)%26]^flag[(i+3)%26]^flag[(i+4)%26]^flag[(i+5)%26])==goal[i])
s.add(flag[0]==95)
s.add(flag[5]==104)
s.add(flag[10]==116)
s.add(flag[15]==100)
s.add(flag[20]==48)
s.add(flag[25]==95)
print('checking : ',s.check())
m = s.model()
solution = ''.join([chr(m[i].as_long()) for i in flag])
print('Secret Text : %s'%solution)
