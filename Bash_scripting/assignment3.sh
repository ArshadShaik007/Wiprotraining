#!/bin/bash

count_lines() {
    local fname="$1"
    if [ -f "$fname" ]; then
        local lns=$(wc -l < "$fname")
        echo "$filename has $lns lines"
    else
        echo "File not found"
    fi
}

count_lines "$1"