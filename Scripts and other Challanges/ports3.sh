#!/usr/bin/bash
addreses=$(cat networks.txt)
for ip in $addreses
do
    if ping -c1 -w1 $ip
    then
    nmap $ip -sU --max-rtt-timeout 150ms --initial-rtt-timeout 100ms --max-retries 2  -p- -T4> ../Allp/hostUDP${ip}.txt
    cat ../Allp/hostUDP${ip}.txt | grep -e open -e unfiltered -e "open|filtered" | awk -F/ '{print $1}' ORS=',' >> ../Discovery/portsUDP$ip.txt
    ((i=i+1))
    fi
done

echo "scan terminated"
