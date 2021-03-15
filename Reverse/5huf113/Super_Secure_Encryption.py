import random
encrypted=''
data=input('Hello enter the string you want to encrypt: \n')
if len(data)==40:
    for i in range(40):
        encrypted+=chr(ord(data[i])^(i<<3))
    simp=[encrypted[i:i+8]for i in range(0,len(data),8)]
    random.shuffle(simp)
    with open('data.enc','w', encoding="utf-8")as file:
        file.write(''.join(simp))
else:
    print('We Only Encrypt Strings with legnth = 40')
