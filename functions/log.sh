#! /bin/sh

while true
 do
     python3 NXP.py> 2>&1 | tee -a ./logs/log.txt
     sleep 1
 done
