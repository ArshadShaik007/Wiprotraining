#!/bin/bash

fname="myfile.txt"

if [ -e "$fname" ]; then
    echo "File exists"
else
    echo "File not found"
fi
