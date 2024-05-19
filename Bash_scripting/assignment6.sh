#!/bin/bash

grep "ERROR" logfile.txt | while read -r line; do
    date=$(echo "$line" | awk '{print $1}')
    time=$(echo "$line" | awk '{print $2}')
    message=$(echo "$line" | awk '{$1=""; $2=""; print $0}')
    echo "Date= $date, Time= $time, Error= $message"
done