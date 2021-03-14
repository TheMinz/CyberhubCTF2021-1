from Crypto.Cipher import ARC4
with open('flag.txt.encx','rb')as f:
    enc=f.read()
for i in range(100000):
    key="3asy"
    x="%05d"%i
    key+=x
    cipher = ARC4.new(key.encode())
    ciphertext = cipher.encrypt(enc)
    if b'CYBERHUB' in ciphertext:
        print("KEY: %s"%key)
        print(ciphertext.decode())
        break
