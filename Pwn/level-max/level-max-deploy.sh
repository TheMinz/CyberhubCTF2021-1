#!/bin/bash

mkdir /chal/
apt update
echo '##done updating##'

sleep 5
apt install -y docker.io

echo '##done installing docker##'
cat <<EOF > /chal/Dockerfile
FROM ubuntu:16.04
VOLUME /chal
WORKDIR /chal
RUN apt update &&  apt install -y socat
EXPOSE 31337
USER nobody
CMD ["socat","TCP4-LISTEN:31337,reuseaddr,fork","EXEC:/chal/level-max,stderr"]
EOF

cat <<EOF > /chal/flag.txt
CYBERHUB{y0u_kn0w_y0ur_PLT_@nd_GOT}
EOF

echo '##dockerfile and flag created##'
wget http://lol.lminzarl.xyz/a03ec0f6da5b8257ea7ae91594776d89 -O /chal/level-max

chmod +x /chal/level-max

echo '##challenge binary downloaded##'
docker build /chal -t level-max

echo '##docker image built##'
docker run -d -v /chal:/chal -p 31337:31337 level-max
echo "##let the hacking begin!##"
