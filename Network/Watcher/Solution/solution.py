from scapy.all import *
#import base64
pkts = rdpcap('chall2.pcapng')
flag= ''
for i in range(len(pkts)) :
    j = pkts[i].op
    flag = flag + chr(j)
print(flag)
