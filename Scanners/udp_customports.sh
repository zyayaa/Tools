#!/bin/bash
mkdir nmap
path=nmap/udp_$1
nmap -sU -sC -sV -A -T4 -p $3 -v --reason -oA $path $2
xsltproc $path.xml -o $path.html
