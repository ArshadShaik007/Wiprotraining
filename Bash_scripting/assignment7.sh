#!/bin/bash

if [ "$#" -ne 3 ]; then
    echo "Usage: $0 <file> <oldtext> <newtext>"
    exit 1
fi

file="$1"
oldtext="$2"
newtext="$3"

sed -i "s/${oldtext}/${newtext}/g" "$file"