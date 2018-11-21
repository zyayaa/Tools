#!/bin/bash
mkdir nmap
path=nmap/$1-top10000
nmap -sC -sV -sS -A -T4 -v --open --reason -oA $path $2
xsltproc $path.xml -o $path.html
path=nmap/$1-full
nmap -sC -sV -sS -A -T4 -p- -v --open --reason -oA $path $2
xsltproc $path.xml -o $path.html
