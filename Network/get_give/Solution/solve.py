import scapy.all as sc 

fi = sc.rdpcap('filtered.pcapng')
coll = b''
for i in fi :
	if sc.ICMP in i :
		if len((i[sc.ICMP][sc.Padding].load)) == 400 :
			coll += ((i[sc.Padding].load))


with open('test1' ,'wb') as f :
	f.write(coll)
