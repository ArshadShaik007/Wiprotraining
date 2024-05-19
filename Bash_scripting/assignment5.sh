#!/bin/bash

DIR="TestDir"

create_files() {
    if [ -d "$DIR" ]; then
        echo "Directory already exists"
        return 1
    fi

    mkdir "$DIR"
    if [ $? -ne 0 ]; then
        echo "Failed to create directory"
        return 1
    fi

    for i in {1..10}; do
        fname="$DIR/file${i}.txt"
        echo "file${i}.txt" > "$fname"
    done
    echo "files created successfully"
}

DEBUG=true

if [ "$DEBUG" = true ]; then
    set -x
fi

create_files

if [ "$DEBUG" = true ]; then
    set +x
fi
