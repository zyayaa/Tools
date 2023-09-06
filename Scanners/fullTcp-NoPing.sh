#!/bin/bash
mkdir -p nmap
path=nmap/tcp_$1-top1000-Pn
nmap -Pn -sV -sS -A -T4 -v --reason -oA $path $2
xsltproc $path.xml -o $path.html
path=nmap/tcp_$1-full-Pn
nmap -Pn -sV -sS -A -T4 -p- -v --reason -oA $path $2
xsltproc $path.xml -o $path.html
