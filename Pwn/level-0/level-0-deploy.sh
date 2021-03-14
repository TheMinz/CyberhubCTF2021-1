#!/bin/bash

mkdir /chal/
apt update
echo '##done updating##'

sleep 5
apt install -y docker.io

echo '##done installing docker##'
cat <<EOF > /chal/Dockerfile
FROM i386/ubuntu:16.04
VOLUME /chal
WORKDIR /chal
RUN apt update &&  apt install -y socat
EXPOSE 31337
USER nobody
CMD ["socat","TCP4-LISTEN:31337,reuseaddr,fork","EXEC:/chal/level-0,stderr"]
EOF

cat <<EOF > /chal/flag.txt
CYBERHUB{W3lc0m3_to_0x41414141}
EOF

echo '##dockerfile and flag created##'
wget http://lol.lminzarl.xyz/bda2a6301fbe5a3980fb94f73d354012 -O /chal/level-0

chmod +x /chal/level-0

echo "kernel.randomize_va_space = 0" > /etc/sysctl.d/01-disable-aslr.conf
echo 0 > /proc/sys/kernel/randomize_va_space 
echo '##challenge binary downloaded##'
docker build /chal -t level-0

echo '##docker image built##'
docker run -d -v /chal:/chal -p 31337:31337 level-0
echo "##let the hacking begin!##"
