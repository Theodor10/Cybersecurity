#! /bin/bash
i=0
for file in ../Discovery/*
do
  if [ -f "$file" ]; then
  ports=$(cat ${file})
  fi
    for port in $ports
    do
      readarray -t ips <networks.txt 
      nmap -p${port} -sV -sC -sS -O -T4 -v ${ips[$i]} >  ../Discovery/finalTCP${ips[i]}.txt
     ((i=i+1))
   done
done 

echo "scan terminated"


