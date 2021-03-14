from itertools import permutations
with open('flag.enc','rb')as f:
    x=f.read().decode('utf-8')
    simp=[x[i:i+8]for i in range(0,len(x),8)]
    for i in permutations(simp):
        data=''.join(i)
        dec=''
        for j in range(40):
            dec+=chr(ord(data[j])^(j<<3))
        if 'CYBERHUB' in dec and dec.endswith('}'):
            print(dec)       
    
