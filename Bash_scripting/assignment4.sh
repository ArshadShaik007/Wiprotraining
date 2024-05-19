#!/bin/bash

mkdir -p TestDir

for i in {1..10}; do
    fname="TestDir/File${i}.txt"
    echo "File${i}.txt" > "$fname"
done