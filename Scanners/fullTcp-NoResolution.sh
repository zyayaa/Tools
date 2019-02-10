#!/bin/bash
mkdir nmap
path=nmap/tcp_$1-top10000
nmap -n -sC -sV -sS -A -T4 -v --open --reason -oA $path $2
xsltproc $path.xml -o $path.html
path=nmap/tcp_$1-full
nmap -n -sC -sV -sS -A -T4 -p- -v --open --reason -oA $path $2
xsltproc $path.xml -o $path.html
