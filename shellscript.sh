#!/bin/bash -x

symbol=$1
start=$2
end=$3

# echo "Retrieving frame for $symbol, starting from $start"
nix-shell --run "python symbol-frame.py $symbol $start $end"

echo "Opening retreived data with vd"
nix-shell --command "vd $symbol.csv"
