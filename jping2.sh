#!/bin/bash

fping -agsq 192.168.155.0/24 > output.csv

echo "[" > output.list

while read ip; 
do
	echo "['$ip','ios','switch']," >>output.list
done <  output.csv

echo "]" >> output.list

