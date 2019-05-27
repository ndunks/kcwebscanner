#!/bin/bash
echo "Build from source.txt"
./build.py source.txt | sort | uniq > words.txt
echo "Clean for sub domain brute"
egrep -v '[\. _#]' words.txt > names.txt
echo "OK"
read -n 1
