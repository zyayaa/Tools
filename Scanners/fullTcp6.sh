#!/bin/bash
mkdir nmap
path=nmap/tcp6_$1-top10000
nmap -6 -sV -sS -A -T4 -v --reason -oA $path $2
xsltproc $path.xml -o $path.html
path=nmap/tcp6_$1-full
nmap -6 -sV -sS -A -T4 -p- -v --reason -oA $path $2
xsltproc $path.xml -o $path.html
