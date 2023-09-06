#!/bin/bash
mkdir -p nmap
path=nmap/$1
nmap -R -sC -sV -sS -A -T4 -p- -v --reason -oA $path $2
xsltproc $path.xml -o $path.html
