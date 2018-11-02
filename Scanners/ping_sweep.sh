#/bin/sh
for i in `seq 1 255`; do ping -c 1 $1.$i | tr \n ' ' | awk '/1 packets received/ {print $2}' ; done
