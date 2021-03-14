import hashlib
import string

def Dizzy_Land(ch):
    data=hashlib.md5(ch.encode()).hexdigest()
    for i in range(1000):
        if i%2==0:
            data=hashlib.sha1(data.encode()).hexdigest()
        elif i%7==0:
            data=hashlib.sha256(data.encode()).hexdigest()
        elif i%3==0:
            data=hashlib.sha512(data.encode()).hexdigest()
        elif i%11==0:
            data=hashlib.md5(data.encode()).hexdigest()
        elif i%5==0:
            data=hashlib.sha384(data.encode()).hexdigest()
    return hashlib.sha512(data.encode()).hexdigest()

with open('Flag','r')as f:
    hashes=f.read().split('\n')[:-1]
    flag=[0]*len(hashes)
    a=string.printable
    a_hashes=[]
    for i in a:
        res=Dizzy_Land(i)
        a_hashes.append(res)
    for j in range(len(flag)):
        flag[j]=a[a_hashes.index(hashes[j])]
    print(''.join(flag))
