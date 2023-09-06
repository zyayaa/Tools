#!/bin/bash
mkdir -p nmap
path=nmap/snmp_$1
nmap -sU -sV -A -T4 -p 161 -v --reason -oA $path $2
xsltproc $path.xml -o $path.html
