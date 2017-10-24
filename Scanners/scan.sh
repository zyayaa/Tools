#!/bin/bash
nmap -sS -A -T4 -p- -v --webxml -oX $1 $2
