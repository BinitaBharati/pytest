#!/bin/bash
if [ $# -eq 0 ]
  then
    echo "No arguments supplied; you need to supply a CSV file"
    exit
fi
python3 main.py $1
